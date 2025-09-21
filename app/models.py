from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    age = Column(Integer, nullable=True)
    gender = Column(String, nullable=True)

    appointments = relationship(
        "Appointment",
        back_populates="patient",
        cascade="all, delete",
        passive_deletes=True
    )

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime(timezone=True), server_default=func.now())
    description = Column(String, nullable=True)
    patient_id = Column(Integer, ForeignKey("patients.id", ondelete="CASCADE"))

    patient = relationship("Patient", back_populates="appointments")
