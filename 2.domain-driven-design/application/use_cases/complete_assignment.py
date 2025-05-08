from my_app.domain.entities.run_assignment import RunAssignment
from my_app.domain.entities.on_road_experiment import OnRoadExperiment
from my_app.infrastructure.repositories.run_assignment_repository import RunAssignmentRepository
from my_app.infrastructure.repositories.on_road_experiment_repository import OnRoadExperimentRepository

def complete_assignment(assignment_id: str):
    # 1. Fetch the run assignment from DB
    assignment = RunAssignmentRepository.get_by_id(assignment_id)
    if not assignment:
        raise ValueError("Assignment not found")

    # 2. Mark the assignment as complete (domain behavior)
    assignment.mark_complete()

    # 3. Persist changes
    RunAssignmentRepository.save(assignment)

    # 4. Now check the parent experiment
    experiment = OnRoadExperimentRepository.get_by_id(assignment.experiment_id)
    if not experiment:
        raise ValueError("Parent experiment not found")

    # 7. Domain logic to see if experiment is done
    if experiment.is_all_assignments_complete():
        experiment.mark_complete()
        OnRoadExperimentRepository.save(experiment)


# FleetOps currently does this
# - team felt its easy to lose track 
# - might not be easy to understand separation the logic between "domain" + "application" + "repository"
# - q: is it we're not use to it?
    # a: there seems to be duplication in domain layer (from a few people)
    # a: old video-transcoder had similar issue
