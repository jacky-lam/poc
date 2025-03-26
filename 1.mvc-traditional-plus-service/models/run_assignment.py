# models/run_assignment.py
class RunAssignment(Base):
    __tablename__ = "run_assignments"

    id = Column(String, primary_key=True)
    experiment_id = Column(String, ForeignKey("on_road_experiments.id"), nullable=False)
    status = Column(String, nullable=False)

    experiment = relationship("OnRoadExperiment", back_populates="run_assignments")

    def __init__(self, id, experiment_id, status="pending"):
        self.id = id
        self.experiment_id = experiment_id
        self.status = status