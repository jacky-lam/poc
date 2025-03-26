# run_assignments/routers.py

from fastapi import APIRouter
from src.run_assignments.flows import complete_assignment_flow

router = APIRouter()

@router.post("/assignments/{assignment_id}/complete")
def complete_assignment(assignment_id: str):
    complete_assignment_flow(assignment_id)
    return {"status": "ok", "detail": f"Assignment {assignment_id} marked complete if found"}
