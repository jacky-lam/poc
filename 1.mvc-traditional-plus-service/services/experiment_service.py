# services/experiment_service.py

from my_app.repositories.run_assignment_repository import RunAssignmentRepository
from my_app.repositories.on_road_experiment_repository import OnRoadExperimentRepository

class ExperimentService:
    @staticmethod
    def check_and_mark_experiment_as_complete(experiment_id: str):
        # Fetch the experiment
        experiment = OnRoadExperimentRepository.get_by_id(experiment_id)
        if not experiment:
            return  # or raise, depending on your rules

        # Fetch all assignments
        assignments = RunAssignmentRepository.get_by_experiment_id(experiment_id)

        # If all are "complete", update experiment
        if all(a.status == "complete" for a in assignments):
            experiment.status = "complete"
            OnRoadExperimentRepository.save(experiment)