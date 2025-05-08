from fastapi import APIRouter
from src.on_road_experiment_templates.service import create_template

router = APIRouter()

@router.post("/on_road_experiment_template")
def create_template(data: dict):
    template = create_template(data)
    return {"status": "ok", "detail": f"Template created {template.id}"}
