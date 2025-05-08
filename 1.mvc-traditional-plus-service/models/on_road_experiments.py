# models/on_road_experiment.py
class OnRoadExperiment(Base):
    __tablename__ = "on_road_experiments"
    
    id = Column(String, primary_key=True)
    status = Column(String, nullable=False)
    name = Column(String, nullable=False)

    # Relationship to run_assignments
    run_assignments = relationship("RunAssignment", back_populates="experiment")

    def __init__(self, id, name, status="pending"):
        self.id = id
        self.name = name
        self.status = status


# feedback from team: this could be our pydantic models instead of DB models
