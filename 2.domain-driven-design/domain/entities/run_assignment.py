class RunAssignment:
    def __init__(self, assignment_id: str, status: str, experiment_id: str):
        self.assignment_id = assignment_id
        self.status = status
        self.experiment_id = experiment_id

    def mark_complete(self):
        self.status = "complete"