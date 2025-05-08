class OnRoadExperiment:
    def __init__(self, experiment_id: str, status: str, run_assignments: list = None):
        self.experiment_id = experiment_id
        self.status = status
        self.run_assignments = run_assignments or []

    def is_all_assignments_complete(self) -> bool:
        """Return True if every run assignment in this experiment is complete."""
        return all(a.status == "complete" for a in self.run_assignments)

    def mark_complete(self):
        """Set status to 'complete' if domain rules allow."""
        self.status = "complete"