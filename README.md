#  Hospital CRUD API (FastAPI)

##  Overview
A simple hospital management API built with **FastAPI**.  
It manages:
- **Patients**
- **Appointments** (linked to patients)

## ✨ Features
- Create, Read, Delete Patients
- Create & List Appointments
- Relational mapping (1 Patient → Many Appointments)
- Interactive API docs (Swagger / ReDoc)

## 🛠 Tech Stack
- FastAPI
- SQLAlchemy ORM
- PostgreSQL (recommended) or SQLite (default fallback)

##  Setup

```bash
git clone <your-repo-url>
cd hospital-crud

# Create virtual environment
python -m venv venv
source venv/bin/activate   # Linux/Mac/gitbash
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt
 Database
Option 1: SQLite (default)
No setup needed, runs out-of-the-box.

Option 2: PostgreSQL
Create a database:

sql
Copy code
CREATE DATABASE hospital_db;
CREATE USER fastapi WITH PASSWORD 'yourpassword';
GRANT ALL PRIVILEGES ON DATABASE hospital_db TO fastapi;
Add .env file:

env
Copy code
DATABASE_URL=postgresql+psycopg2://fastapi:yourpassword@localhost/hospital_db
▶️ Run the API
bash
Copy code
uvicorn app.main:app --reload
🔗 API Endpoints
Patients
Method	Endpoint	Description
POST	/patients/	Create patient
GET	/patients/	List all patients
GET	/patients/{id}	Get patient by ID
DELETE	/patients/{id}	Delete patient

Appointments
Method	Endpoint	Description
POST	/appointments/patients/{patient_id}	Create appointment for a patient
GET	/appointments/	List all appointments

 API Docs
Swagger UI → http://127.0.0.1:8000/docs

ReDoc → http://127.0.0.1:8000/redoc