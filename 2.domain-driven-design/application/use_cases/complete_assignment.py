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

    # 5. We also need the full set of run_assignments
    #    (the repository could load them or they might be lazy loaded, 
    #     or we do a separate call to get them all)
    all_assignments = RunAssignmentRepository.get_by_experiment_id(experiment.experiment_id)

    # 6. Update the experiment entity’s “run_assignments” 
    experiment.run_assignments = all_assignments

    # 7. Domain logic to see if experiment is done
    if experiment.is_all_assignments_complete():
        experiment.mark_complete()
        OnRoadExperimentRepository.save(experiment)