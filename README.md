Company API (Django REST Framework)

A simple Company & Employee Management REST API built using Django and Django REST Framework (DRF).
This API allows you to manage companies, employees, and retrieve employees belonging to a specific company.

🚀 Features

CRUD operations for Company

CRUD operations for Employee

Fetch all employees of a specific company

Hyperlinked REST API

Easy to test using Postman

🛠 Tech Stack

Python

Django

Django REST Framework

SQLite / PostgreSQL (any Django-supported DB)

📁 Models Overview
Company

company_id (Primary Key)

name (unique)

location

about

company_type (startup, sme, enterprise, agency, other)

active

created_at

updated_at

Employee

name

email

address

phone

about

employee_position (intern, junior, senior, manager, hr, admin, other)

company (ForeignKey → Company)

active

created_at

updated_at

🔗 Base URL
http://127.0.0.1:8000/api/

📌 API Endpoints
🏢 Company APIs

| Method | Endpoint                     | Description                |
| ------ | ---------------------------- | -------------------------- |
| GET    | `/companies/`                | List all companies         |
| POST   | `/companies/`                | Create a new company       |
| GET    | `/companies/{id}/`           | Retrieve company details   |
| PUT    | `/companies/{id}/`           | Update company             |
| PATCH  | `/companies/{id}/`           | Partial update company     |
| DELETE | `/companies/{id}/`           | Delete company             |
| GET    | `/companies/{id}/employees/` | Get employees of a company |

👨‍💼 Employee APIs

| Method | Endpoint           | Description               |
| ------ | ------------------ | ------------------------- |
| GET    | `/employees/`      | List all employees        |
| POST   | `/employees/`      | Create a new employee     |
| GET    | `/employees/{id}/` | Retrieve employee details |
| PUT    | `/employees/{id}/` | Update employee           |
| PATCH  | `/employees/{id}/` | Partial update employee   |
| DELETE | `/employees/{id}/` | Delete employee           |

📦 Sample Request & Response
1️⃣ Create Company
➤ Request

POST /api/companies/

{
  "name": "TechNova Pvt Ltd",
  "location": "Pune, India",
  "about": "A software development company",
  "company_type": "startup",
  "active": true
}

✔ Response
{
  "url": "http://127.0.0.1:8000/api/companies/1/",
  "company_id": 1,
  "name": "TechNova Pvt Ltd",
  "location": "Pune, India",
  "about": "A software development company",
  "company_type": "startup",
  "active": true,
  "created_at": "2026-01-15T16:45:20Z",
  "updated_at": "2026-01-15T16:45:20Z"
}

2️⃣ List All Companies
➤ Request

GET /api/companies/

✔ Response
[
  {
    "url": "http://127.0.0.1:8000/api/companies/1/",
    "company_id": 1,
    "name": "TechNova Pvt Ltd",
    "location": "Pune, India",
    "about": "A software development company",
    "company_type": "startup",
    "active": true,
    "created_at": "2026-01-15T16:45:20Z",
    "updated_at": "2026-01-15T16:45:20Z"
  }
]

3️⃣ Create Employee
➤ Request

POST /api/employees/
{
  "name": "Rahul Sharma",
  "email": "rahul@technova.com",
  "address": "Mumbai, India",
  "phone": "+919876543210",
  "about": "Backend Developer",
  "employee_position": "senior",
  "active": true,
  "company": "http://127.0.0.1:8000/api/companies/1/"
}

✔ Response
{
  "url": "http://127.0.0.1:8000/api/employees/1/",
  "id": 1,
  "name": "Rahul Sharma",
  "email": "rahul@technova.com",
  "address": "Mumbai, India",
  "phone": "+919876543210",
  "about": "Backend Developer",
  "employee_position": "senior",
  "company": "http://127.0.0.1:8000/api/companies/1/",
  "company_id": 1,
  "active": true,
  "created_at": "2026-01-15T16:50:10Z",
  "updated_at": "2026-01-15T16:50:10Z"
}

4️⃣ List All Employees
➤ Request

GET /api/employees/

✔ Response
[
  {
    "url": "http://127.0.0.1:8000/api/employees/1/",
    "id": 1,
    "name": "Rahul Sharma",
    "email": "rahul@technova.com",
    "employee_position": "senior",
    "company_id": 1,
    "active": true
  }
]

5️⃣ Get Employees of a Company
➤ Request

GET /api/companies/1/employees/

✔ Response (Employees Found)
[
  {
    "name": "Rahul Sharma",
    "email": "rahul@technova.com",
    "employee_position": "senior",
    "company_id": 1
  }
]

❌ Response (No Employees)
{
  "message": "OOPS, Employee Not Found!"
}

❌ Response (Company Not Found)
{
  "message": "OOPS, Company Not Found!"
}

🧪 Testing with Postman

Import endpoints manually

Set Content-Type: application/json

Use GET / POST / PUT / PATCH / DELETE methods

For Employee creation, use company URL (Hyperlinked field)

📌 Notes

Uses HyperlinkedModelSerializer

Company deletion will delete related employees (CASCADE)

Phone number validation supported

Ordered by created_at (latest first)

👨‍💻 Author

Dattatraya Walunj

Backend Developer | Django | DRF
