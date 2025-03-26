from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from src.database import Base

class OnRoadExperiment(Base):
    __tablename__ = "on_road_experiments"

    id = Column(String, primary_key=True)
    status = Column(String, nullable=False)
    name = Column(String, nullable=False)

    run_assignments = relationship("RunAssignment", back_populates="experiment")
