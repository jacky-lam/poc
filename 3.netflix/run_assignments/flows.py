# on_road_experiments/service.py

from src.on_road_experiments.models import OnRoadExperiment
from src.run_assignments.models import RunAssignment
from src.database import SessionLocal

def get_experiment_by_id(experiment_id: str) -> OnRoadExperiment:
    session = SessionLocal()
    try:
        return session.query(OnRoadExperiment).filter(OnRoadExperiment.id == experiment_id).first()
    finally:
        session.close()

def save_experiment(experiment: OnRoadExperiment):
    session = SessionLocal()
    try:
        session.add(experiment)
        session.commit()
    finally:
        session.close()

def is_all_assignments_complete(experiment: OnRoadExperiment) -> bool:
    return all(a.status == "complete" for a in experiment.run_assignments)

def mark_experiment_complete(experiment_id: str):
    experiment = get_experiment_by_id(experiment_id)
    if not experiment:
        raise ValueError("Experiment not found")

    experiment.status = "complete"
    save_experiment(experiment)
