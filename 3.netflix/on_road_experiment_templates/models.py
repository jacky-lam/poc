from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from src.database import Base

class OnRoadExperimentTemplate(Base):
    __tablename__ = "on_road_experiment_template"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)

    routes = relationship("Routes")

# this should be pydantic models