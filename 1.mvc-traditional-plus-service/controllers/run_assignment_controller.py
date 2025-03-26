# controllers/run_assignment_controller.py
# (In e.g., Flask or FastAPI style)

from fastapi import APIRouter
from my_app.services.assignment_service import AssignmentService

router = APIRouter()

@router.post("/assignments/{assignment_id}/complete")
def complete_assignment(assignment_id: str):
    AssignmentService.complete_assignment(assignment_id)
    return {"message": "Assignment completed if found. Experiment possibly updated."}