from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base

class RunAssignment(Base):
    __tablename__ = "run_assignments"

    id = Column(String, primary_key=True)
    status = Column(String, nullable=False)
    experiment_id = Column(String, ForeignKey("on_road_experiments.id"), nullable=False)
    experiment = relationship("OnRoadExperiment", back_populates="run_assignments")

# this should be pydantic models