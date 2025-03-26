# services/assignment_service.py

from my_app.repositories.run_assignment_repository import RunAssignmentRepository
from my_app.repositories.on_road_experiment_repository import OnRoadExperimentRepository
from my_app.services.experiment_service import ExperimentService

class AssignmentService:
    @staticmethod
    def complete_assignment(assignment_id: str):
        # 1. Get the assignment
        assignment = RunAssignmentRepository.get_by_id(assignment_id)
        if not assignment:
            raise Exception("Assignment not found")

        # 2. Mark it complete
        assignment.status = "complete"
        RunAssignmentRepository.save(assignment)

        # 3. We check if we need to complete the experiment
        ExperimentService.check_and_mark_experiment_as_complete(assignment.experiment_id)

