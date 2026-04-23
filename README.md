#  FastAPI Hospital Management System

A scalable and modular backend application built using **FastAPI** for managing doctors, patients, and appointments with secure authentication and clean architecture.


##  Features

###  Doctor Module
- Create, update, delete doctors
- Filter doctors by specialization
- Activate / Deactivate doctor

###  Patient Module
- Create, update, delete patients
- Search patients by name or phone number

###  Appointment Module
- Book appointments (Doctor ↔ Patient)
- View all appointments
- Filter by doctor or patient
- Cancel appointments
- Appointment status management:
  - Scheduled
  - Completed
  - Cancelled

###  Authentication
- JWT-based authentication
- Login system
- Protected routes (secured APIs)

---

## 🛠 Tech Stack

- FastAPI
- SQLAlchemy (ORM)
- SQLite / MySQL
- Pydantic
- Uvicorn
- Python-dotenv
- JWT Authentication


