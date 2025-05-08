from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from src.database import Base

class OnRoadExperiment(Base):
    __tablename__ = "on_road_experiments"

    id = Column(String, primary_key=True)
    status = Column(String, nullable=False)
    name = Column(String, nullable=False)

    run_assignments = relationship("RunAssignment", back_populates="experiment")

class OnRoadExperimentBranches(Base):
    __tablename__ = "on_road_experiment_branches"

    id = Column(String, primary_key=True)
    status = Column(String, nullable=False)
    name = Column(String, nullable=False)

    run_assignments = relationship("RunAssignment", back_populates="experiment")

# this should be pydantic models

"""
Debate is branches should live inside experiment
- sit inside on_road_experiments because it doesn't have its own endpoint (logic isn't quite big)
- once branches has its own endpoint, then we should split it out

"""