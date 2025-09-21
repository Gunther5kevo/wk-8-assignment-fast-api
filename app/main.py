from fastapi import FastAPI
from . import models, database
from .routers import patients, appointments

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Hospital CRUD API", version="1.0")

# Routers
app.include_router(patients.router)
app.include_router(appointments.router)

@app.get("/")
def root():
    return {"message": "Welcome to Hospital CRUD API"}
