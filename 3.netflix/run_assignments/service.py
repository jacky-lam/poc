# run_assignments/service.py

from src.run_assignments.models import RunAssignment
from src.database import SessionLocal

def get_assignment_by_id(assignment_id: str) -> RunAssignment:
    session = SessionLocal()
    try:
        return session.query(RunAssignment).filter(RunAssignment.id == assignment_id).first()
    finally:
        session.close()

def save_assignment(assignment: RunAssignment):
    session = SessionLocal()
    try:
        session.add(assignment)
        session.commit()
    finally:
        session.close()

def complete_assignment(assignment_id: str) -> RunAssignment:
    """Mark an assignment as complete. Return the updated assignment object."""
    assignment = get_assignment_by_id(assignment_id)
    if not assignment:
        raise ValueError(f"No assignment found for id {assignment_id}")
    
    assignment.status = "complete"
    save_assignment(assignment)
    return assignment
