# run_assignments/flows.py

from src.run_assignments import service as assignment_service
from src.on_road_experiments import service as experiment_service

def complete_assignment_flow(assignment_id: str):
    """Flow that handles the entire logic of completing a RunAssignment 
    and possibly completing the experiment."""
    # 1. Mark the assignment complete
    assignment = assignment_service.complete_assignment(assignment_id)

    # 2. Check if the experiment is now all complete
    experiment = experiment_service.get_experiment_by_id(assignment.experiment_id)
    if experiment and experiment_service.is_all_assignments_complete(experiment):
        # 3. Mark the experiment complete
        experiment_service.mark_experiment_complete(experiment.id)
    
        # 4. Optionally send Slack notification or trigger plugin
        # dispatch_slack_message(...), etc.

# team seemed to like this structure
# 
