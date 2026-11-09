"""Enterprise Knowledge Base & Retrieval-Augmented Generation (RAG) Engine.

Provides:
1. Document ingestion and text extraction (TXT, MD, PDF, DOCX).
2. Overlapping text chunking.
3. Relevance search retriever over DocumentChunk models.
4. Source citation context formatting for AI agent prompts.
"""

import os
import re
from typing import List, Dict, Any, Tuple

from .models import Document, DocumentChunk


def _extract_docx(file_path: str) -> str:
    """Extract plain text from a .docx file using standard library zipfile and XML parsing."""
    try:
        import zipfile
        import xml.etree.ElementTree as ET
        with zipfile.ZipFile(file_path) as zf:
            xml_content = zf.read('word/document.xml')
            tree = ET.fromstring(xml_content)
            texts = [node.text for node in tree.iter() if node.tag.endswith('}t') and node.text]
            return "\n".join(texts)
    except Exception:
        return ""


def _extract_pdf(file_path: str) -> str:
    """Extract plain text from a .pdf file using pypdf or text stream regex parsing."""
    try:
        import pypdf
        reader = pypdf.PdfReader(file_path)
        pages_text = []
        for page in reader.pages:
            text = page.extract_text()
            if text:
                pages_text.append(text)
        return "\n\n".join(pages_text)
    except Exception:
        try:
            with open(file_path, 'rb') as f:
                content = f.read().decode('latin-1', errors='ignore')
                text_blocks = re.findall(r'BT(.*?)ET', content, re.DOTALL)
                extracted = []
                for block in text_blocks:
                    strings = re.findall(r'\((.*?)\)', block)
                    if strings:
                        extracted.append(" ".join(strings))
                return "\n\n".join(extracted)
        except Exception:
            return ""


def extract_text(file_path: str, file_type: str) -> str:
    """Extract plain text from a file path based on its extension."""
    if not os.path.exists(file_path):
        return ""

    file_type = file_type.lower().strip('.')

    if file_type == 'docx':
        return _extract_docx(file_path)

    if file_type == 'pdf':
        return _extract_pdf(file_path)

    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read()
    except Exception:
        return ""


def chunk_text(text: str, chunk_size: int = 500, overlap: int = 100) -> List[Dict[str, Any]]:
    """Split text into overlapping chunk dictionaries with word boundaries preserved."""
    cleaned = re.sub(r'\r\n|\r', '\n', text).strip()
    if not cleaned:
        return []

    chunks = []
    start = 0
    length = len(cleaned)
    chunk_index = 1

    while start < length:
        end = min(start + chunk_size, length)
        
        if end < length:
            last_space = cleaned.rfind(' ', start, end)
            if last_space > start + (chunk_size // 2):
                end = last_space

        chunk_str = cleaned[start:end].strip()
        if chunk_str:
            words = set(re.findall(r'\b[a-zA-Z0-9]{3,}\b', chunk_str.lower()))
            chunks.append({
                'chunk_index': chunk_index,
                'content': chunk_str,
                'page_number': max(1, (start // 2000) + 1),
                'tokens_count': len(chunk_str.split()),
                'keywords': list(words)[:20],
            })
            chunk_index += 1

        if end >= length:
            break

        start = max(start + 1, end - overlap)

    return chunks


def ingest_document(document: Document) -> int:
    """Ingest a Document instance: extract text, chunk it, and save DocumentChunk rows."""
    if not document.file:
        return 0

    file_path = document.file.path
    extracted = extract_text(file_path, document.file_type)
    
    if not extracted:
        return 0

    document.chunks.all().delete()

    chunks_data = chunk_text(extracted)
    chunk_instances = []

    for c in chunks_data:
        chunk_instances.append(DocumentChunk(
            document=document,
            chunk_index=c['chunk_index'],
            content=c['content'],
            page_number=c['page_number'],
            tokens_count=c['tokens_count'],
            keywords=c['keywords'],
        ))

    DocumentChunk.objects.bulk_create(chunk_instances)
    
    chunk_count = len(chunk_instances)
    document.chunk_count = chunk_count
    document.file_size = os.path.getsize(file_path) if os.path.exists(file_path) else 0
    document.save(update_fields=['chunk_count', 'file_size'])

    return chunk_count


def retrieve_context(query: str, max_results: int = 3) -> List[Tuple[DocumentChunk, float]]:
    """Retrieve top-K matching DocumentChunk instances scored by keyword relevance."""
    query_terms = set(re.findall(r'\b[a-zA-Z0-9]{3,}\b', query.lower()))
    if not query_terms:
        return []

    stopwords = {'the', 'and', 'for', 'that', 'this', 'with', 'from', 'have', 'what', 'where', 'how', 'you', 'are', 'was'}
    query_terms = {t for t in query_terms if t not in stopwords}
    if not query_terms:
        return []

    chunks = DocumentChunk.objects.select_related('document').all()
    scored_chunks = []

    for chunk in chunks:
        chunk_words = set(re.findall(r'\b[a-zA-Z0-9]{3,}\b', chunk.content.lower()))
        intersection = query_terms.intersection(chunk_words)
        if intersection:
            score = len(intersection) / (len(query_terms) ** 0.5)
            scored_chunks.append((chunk, score))

    scored_chunks.sort(key=lambda x: x[1], reverse=True)
    return scored_chunks[:max_results]


def format_rag_prompt(query: str, retrieved_chunks: List[Tuple[DocumentChunk, float]]) -> str:
    """Format retrieved document chunks into cited markdown context for agent prompts."""
    if not retrieved_chunks:
        return ""

    formatted_docs = []
    for chunk, _score in retrieved_chunks:
        formatted_docs.append(
            f"--- DOCUMENT SOURCE: {chunk.document.title} (Page {chunk.page_number}) ---\n"
            f"{chunk.content}\n"
            f"CITATION KEY: [Source: {chunk.document.title}, Page {chunk.page_number}]\n"
        )

    context_block = "\n".join(formatted_docs)
    return (
        "\n\n[RELEVANT ENTERPRISE KNOWLEDGE BASE DOCUMENTS]:\n"
        f"{context_block}\n"
        "INSTRUCTION: Base your response on the enterprise documents above whenever applicable. "
        "Always cite your sources using the CITATION KEY (e.g., [Source: Document Title, Page X]) "
        "in your reply when quoting or using document facts.\n"
    )
