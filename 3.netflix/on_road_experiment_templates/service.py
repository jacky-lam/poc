from src.on_road_experiment_templates.models import OnRoadExperimentTemplate
from src.database import SessionLocal

def create_template(data: dict) -> OnRoadExperimentTemplate:
    session = SessionLocal()
    template = OnRoadExperimentTemplate({'name': 'abc'})
    try:
        session.add(template)
        session.commit()
        return template
    finally:
        session.close()
