# 🚀 Weblog REST API

A production-ready **Weblog REST API** built with **Django REST Framework**, following RESTful architecture and modern backend development practices.

This project provides a secure, scalable backend for a blogging platform with JWT authentication, Dockerized deployment, PostgreSQL, Redis caching, and Nginx integration.

---

## ✨ Features

* 🔐 JWT Authentication with Djoser
* 👤 User Registration & Login
* 📝 Full CRUD Operations for Blog Posts
* 📂 Category Management
* 🔍 Search & Filtering
* 📄 Pagination
* 🛡️ Permission-Based Access Control
* ⚡ Redis Caching
* 🐘 PostgreSQL Database
* 🐳 Docker & Docker Compose
* 🌐 Nginx Reverse Proxy
* 📦 Production-Ready Architecture

---

## 🛠 Tech Stack

| Category         | Technologies                  |
| ---------------- | ----------------------------- |
| Backend          | Django, Django REST Framework |
| Authentication   | Djoser, Simple JWT            |
| Database         | PostgreSQL                    |
| Cache            | Redis                         |
| Reverse Proxy    | Nginx                         |
| Containerization | Docker, Docker Compose        |
| Language         | Python 3                      |

---

## 📁 Project Structure

```text
.
├── blog/
├── accounts/
├── core/
├── config/
├── docker/
│   ├── nginx/
│   └── ...
├── media/
├── static/
├── requirements/
├── docker-compose.yml
├── Dockerfile
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone git@github.com:A-Aghaverdizadeh/Django_Weblog_API.git
cd Django_Weblog_API
```

---

### 2. Build and start containers

```bash
docker compose up --build
```

---

### 3. Create a superuser

```bash
docker compose exec backend python manage.py createsuperuser
```

---

## 📚 API Features

The API includes endpoints for:

* Authentication
* User Management
* Blog Posts
* Categories
* Search
* Pagination

Authentication is handled using **JWT Bearer Tokens**.

---

## 🔒 Authentication

After login you'll receive:

```json
{
    "access": "jwt-access-token",
    "refresh": "jwt-refresh-token"
}
```

Use the access token in requests:

```http
Authorization: Bearer YOUR_ACCESS_TOKEN
```

---

## 📸 Screenshots

You can add screenshots here.

```
docs/
├── swagger.png
```

Example:

```markdown
![swagger](docs/swagger.png)
```

---

## 💡 Why This Project?

This project demonstrates practical backend development skills including:

* REST API Design
* Authentication & Authorization
* Dockerized Development
* Production Deployment
* Database Design
* API Security
* Clean Project Architecture
* Redis Performance Optimization

---

## 📈 Future Improvements

* Email Verification
* Password Reset
* API Rate Limiting
* Swagger/OpenAPI Documentation
* Unit & Integration Tests
* CI/CD Pipeline
* Celery Background Tasks
* Image Upload Support

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

Feel free to fork the project and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Amir Aghaverdi**

Backend Developer | Python & Django

GitHub: https://github.com/A-Aghaverdizadeh
