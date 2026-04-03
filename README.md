Smart Storage Locker Management System - Backend
This is the REST API backend for the Smart Storage Locker Management System, built using Django and Django REST Framework. It provides secure, role-based access to manage lockers and user reservations.
+2

🚀 Live API
The backend is deployed and live at: https://smart-locker-system-2.onrender.com/

🛠 Tech Stack

Framework: Django 4.2.x 


API: Django REST Framework (DRF) 


Database: PostgreSQL 


Authentication: JWT (SimpleJWT) 
+1

Deployment: Render

🔐 Core Features

JWT Authentication: Secure registration and login flow.


Role-Based Access Control (RBAC): Distinct permissions for Admin and User roles.


Locker Management: Full CRUD operations for lockers (Admin only for creation/updates).
+1


Reservation System: Users can view available lockers and book them with a reserved_until timestamp.
+1

📡 API Endpoints
Authentication

POST /api/auth/register/ - Register a new user.


POST /api/auth/login/ - Obtain JWT Access and Refresh tokens.


POST /api/auth/refresh/ - Refresh an expired access token.

Lockers

GET /api/lockers/ - List all lockers and their current status.


POST /api/lockers/ - Create a new locker (Admin only).


GET /api/lockers/<id>/ - View specific locker details.

Reservations

POST /api/reservations/ - Create a new locker reservation.


GET /api/reservations/ - List all reservations (Admin) or user-specific reservations.


PUT /api/reservations/<id>/release/ - Release/Cancel a reservation.

⚙️ Local Setup
Clone the repository:

Bash
git clone <your-repo-url>
cd backend
Create a virtual environment:

Bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

Bash
pip install -r requirements.txt
Run migrations:

Bash
python manage.py migrate
Start the server:

Bash
python manage.py runserver
