# User Authentication System - Flask API with Frontend

![GitHub stars](https://img.shields.io/github/stars/yourusername/user-auth-flask?style=social)
![GitHub forks](https://img.shields.io/github/forks/yourusername/user-auth-flask?style=social)
![GitHub license](https://img.shields.io/github/license/yourusername/user-auth-flask)
![GitHub last commit](https://img.shields.io/github/last-commit/yourusername/user-auth-flask)

A complete user authentication system built with Flask for the backend API and HTML/CSS for the frontend interface. This project provides a professional solution for user registration, login, and session management.

## Features

- User registration with username, email, and password
- User login with email and password authentication
- Responsive frontend interface
- RESTful API endpoints
- SQLite database integration
- Input validation and error handling
- Session management
- Password security (hashed storage)

## Tech Stack

### Backend
- Flask (Python web framework)
- Flask-SQLAlchemy (ORM for database operations)
- Flask-CORS (Cross-Origin Resource Sharing)

### Frontend
- HTML5
- CSS3
- JavaScript (for form submissions)

## Project Structure

```
user-auth-system/
│
├── app.py                # Main Flask application
├── models.py             # Database models
├── routes.py             # API routes and business logic
│
├── views/            # HTML templates
│   ├── index.html        # Welcome page
│   ├── login.html        # Login form
│   └── signup.html       # Signup form
│
└── user_sqlite.db       # SQLite database (auto-generated)
```

## Installation Guide

### Prerequisites
- Python 3.9+
- pip (Python package installer)

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/1wahab/user-auth-flask.git
   cd user-auth-flask
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install flask flask-sqlalchemy flask-cors
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Access the application at `http://127.0.0.1:5000`

## API Documentation

### Base URL
`http://127.0.0.1:5000`

### Endpoints

#### 1. User Registration
- **POST** `/signup`
- **Request Body**:
  ```json
  {
    "username": "string",
    "email": "string",
    "password": "string"
  }
  ```
- **Success Response**:
  ```json
  {
    "message": "User registered successfully"
  }
  ```
- **Error Responses**:
  - 400 Bad Request: Missing fields
  - 400 Bad Request: Username or email already exists

#### 2. User Login
- **POST** `/login`
- **Request Body**:
  ```json
  {
    "email": "string",
    "password": "string"
  }
  ```
- **Success Response**:
  ```json
  {
    "message": "Login successful",
    "username": "string"
  }
  ```
- **Error Responses**:
  - 400 Bad Request: Missing fields
  - 400 Bad Request: Invalid email or password

## Frontend Implementation

The frontend consists of three main pages:

1. **Welcome Page** (`index.html`)
   - Displays the application name
   - Provides options to sign up or log in

2. **Signup Page** (`signup.html`)
   - Form for user registration
   - Input fields for username, email, and password
   - Responsive design for different screen sizes

3. **Login Page** (`login.html`)
   - Form for user authentication
   - Input fields for email and password
   - Link to signup page for new users

## Security Considerations

- Passwords are stored securely in the database
- Input validation to prevent SQL injection
- CORS configured for secure cross-origin requests
- Error handling to prevent information leakage

## Contribution Guidelines

We welcome contributions to improve this project! Please follow these guidelines:

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Commit your changes with descriptive messages
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
