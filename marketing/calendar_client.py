"""Google Calendar & Interview Scheduling Tool Client for HR Agent (Elena)."""

import datetime
from typing import Dict, Any


def schedule_interview(candidate_name: str, candidate_email: str, job_title: str, date_str: str, time_str: str) -> Dict[str, Any]:
    """Generate an interview event invitation and .ics summary."""
    event_id = f"evt_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
    summary = f"Interview: {candidate_name} for {job_title}"
    start_datetime = f"{date_str} T {time_str}"
    
    ics_content = (
        f"BEGIN:VCALENDAR\nVERSION:2.0\nBEGIN:VEVENT\n"
        f"SUMMARY:{summary}\nDESCRIPTION:Candidate interview with HR and engineering team.\n"
        f"ORGANIZER;CN=Elena (HR):mailto:hr@aiworkforce.local\n"
        f"ATTENDEE;CN={candidate_name}:mailto:{candidate_email}\n"
        f"END:VEVENT\nEND:VCALENDAR"
    )
    
    return {
        'status': 'scheduled',
        'event_id': event_id,
        'summary': summary,
        'candidate': f"{candidate_name} <{candidate_email}>",
        'datetime': start_datetime,
        'ics_preview': ics_content,
    }


def list_calendar_events(count: int = 5) -> Dict[str, Any]:
    """Return mock upcoming calendar events for workspace schedules."""
    events = [
        {'id': 'evt_101', 'title': 'Candidate Screening - Senior Full-Stack Engineer', 'time': 'Tomorrow at 10:00 AM'},
        {'id': 'evt_102', 'title': 'Weekly HR & Operations Check-in', 'time': 'Wednesday at 02:00 PM'},
        {'id': 'evt_103', 'title': 'Engineering Standup & Sprint Planning', 'time': 'Thursday at 09:30 AM'},
    ]
    return {'status': 'ok', 'events': events[:count]}
