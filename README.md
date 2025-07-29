# FastAPI ToDo App Project

## Table of Contents

- [Overview](#overview)
- [Why FastAPI?](#why-fastapi)
- [The 7 Advantages of FastAPI](#the-7-advantages-of-fastapi-demonstrated-in-this-project)
- [Project Features](#project-features)
- [Technologies Used](#technologies-used)
- [Folder Structure](#folder-structure)
- [How to Run the Project](#how-to-run-the-project)
- [API Documentation](#api-documentation)
- [Conclusion](#conclusion)

---

## Overview

This is a hands-on project built using **FastAPI**, a modern, high-performance Python framework for building APIs. The app is a minimal **ToDo API** designed to demonstrate the key advantages of using FastAPI over traditional frameworks like Flask or Django.

This README follows the tutorial by Travis Media titled [_"Why You NEED To Learn FastAPI | Hands-On Project"_](https://youtu.be/cbASjoZZGIw?si=8yrFNMHbEWD-_wgd), where we build a ToDo application while showcasing 7 core reasons to learn and use FastAPI.

---

## Why FastAPI?

Modern software often requires APIs that are flexible, scalable, and easy to integrate with multiple platforms (web, mobile, desktop). FastAPI provides a clean solution:

- Maintain a **single backend** that supports multiple frontends
- Promote clean code separation (routes, models, logic)
- Boost productivity with built-in developer tools

> "FastAPI is like the USB port for your backend — once it's in place, anything can plug in and work."

---

## The 7 Advantages of FastAPI (Demonstrated in this Project)

1. **Plain Python Syntax**

   - FastAPI is intuitive and readable.
   - Route definitions are clean and require no boilerplate.

2. **Async Support Built-in**

   - FastAPI uses ASGI for asynchronous request handling out of the box.
   - Great for performance when handling concurrent I/O.

3. **Data Validation with Pydantic**

   - Define data models using `pydantic.BaseModel`
   - Automatically validate and parse input data

4. **Typed Python**

   - Use standard Python type hints for inputs and outputs
   - Improves readability, autocomplete, and documentation

5. **JSON Error Responses**

   - All errors return structured, developer-friendly JSON

6. **Built-in Authentication Support**

   - HTTP Basic Auth, OAuth2, JWT and API Keys

7. **Auto-generated Documentation**

   - Swagger UI: `/docs`
   - ReDoc: `/redoc`

---

##  Project Features

- Create, Read, Update, and Delete ToDo items
- All data is handled in-memory (for simplicity)
- Typed request/response models with `pydantic`
- Uses `uvicorn` as ASGI server

## Technologies Used

| Component       | Tech                                             |
| --------------- | ------------------------------------------------ |
| API Framework   | [FastAPI](https://fastapi.tiangolo.com/)         |
| Server          | [Uvicorn](https://www.uvicorn.org/)              |
| Data Validation | [Pydantic](https://pydantic-docs.helpmanual.io/) |
| Language        | Python 3.10+                                     |

---

## Folder Structure

```
fastapi-project/
├── app/
│   ├── main.py
│   └── models.py
├── requirements.txt
└── README.md
```

---

## How to Run the Project

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
uvicorn app.main:app --reload
```

Visit [http://localhost:8000/docs](http://localhost:8000/docs) to access the Swagger UI.

---

## API Documentation

### Endpoints

| Method | Endpoint           | Description         |
| ------ | ------------------ | ------------------- |
| GET    | `/`                | Root endpoint       |
| GET    | `/todos`           | Get all todos       |
| GET    | `/todos/{todo_id}` | Get a specific todo |
| POST   | `/todos`           | Create a new todo   |
| PUT    | `/todos/{todo_id}` | Update a todo       |
| DELETE | `/todos/{todo_id}` | Delete a todo       |

### Request/Response Examples

**Create Todo (POST /todos)**

```json
// Request
{
  "id": 1,
  "item": "Learn FastAPI"
}

// Response
{
  "message": "Todo has been added"
}
```

**Get All Todos (GET /todos)**

```json
// Response
{
  "todos": [
    {
      "id": 1,
      "item": "Learn FastAPI"
    }
  ]
}
```

**Get Single Todo (GET /todos/1)**

```json
// Response
{
  "todo": {
    "id": 1,
    "item": "Learn FastAPI"
  }
}
```

---

## Conclusion

This FastAPI ToDo project demonstrates my proficiency in modern Python web development, showcasing technical skills in RESTful API design, type-safe programming with Python type hints, asynchronous programming concepts, and modern frameworks like FastAPI, Pydantic, and Uvicorn. Beyond the technical implementation, this project reflects my professional competencies in writing clean, maintainable code architecture, following industry best practices for API development, and my ability to quickly learn and implement new technologies while maintaining excellent documentation standards. This project represents my commitment to staying current with modern development tools and delivering production-ready code that follows industry standards.

---

**Related Project:** For a production-ready implementation featuring Docker containerization, security best practices, and CI/CD integration with GitHub Actions, see the [docker-security-falcon](https://github.com/JThomas404/docker-security-falcon) repository.

---
