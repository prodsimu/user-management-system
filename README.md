# User Management System (CLI)

## Overview

This project is a command-line User Management System built with Python.

It simulates a simple backend structure within a terminal application and includes authentication, session management, role-based access control, and full CRUD operations for users.

The main goal of this project was to practice organizing a medium-sized application using clear separation of responsibilities and clean code principles.

---

## Features

- User authentication
- Session management
- Role-based access (admin and regular user)
- Create, read, update and delete users
- Password validation rules
- Login attempt tracking and reset
- Centralized feedback handling inside the controller

---

## Architecture

The project follows a layered structure:

### Controller
Handles application flow and state management.  
Coordinates between the UI and the service layer.

### Service
Contains business logic and validation rules.  
Responsible for enforcing authentication and authorization rules.

### Repository
Abstracts data storage and provides CRUD operations.

### UI
Handles input/output and menu rendering.  
Returns formatted messages instead of printing directly.

### Domain Models
Defines the main entities:
- User
- Session

Each layer has a clear responsibility, which keeps the code organized and easier to maintain.

---

## Error Handling

The application uses custom exceptions to represent domain errors, such as:

- InvalidPasswordError
- UserNotFoundError
- InactiveUserError
- SamePasswordError
- AppError (base exception)

This approach keeps validation logic clean and avoids mixing error handling with presentation logic.

---

## Technologies

- Python 3
- Object-Oriented Programming
- Command-line interface
- Standard library only

---

## Possible Improvements

- Password hashing
- Persistent storage (SQLite or JSON)
- Unit tests
- Logging
- Dependency injection improvements

---

## Purpose

This project demonstrates the ability to structure a non-trivial Python application using backend design concepts in a CLI environment, with focus on organization, separation of concerns, and maintainability.