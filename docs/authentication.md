# Authentication Documentation for Library Management System

## Overview
This document outlines the authentication and authorization mechanisms implemented in the Library Management System.

## User Roles
The Library Management System supports the following user roles:
- **Admin**: Has full access to manage users, books, and loans.
- **Librarian**: Can manage books and loans but has limited access to user management.
- **Member**: Can borrow books and manage their own profile.

## Authentication
### User Registration
Users can register by providing the following information:
- Username
- Email
- Password
- first_name
- last_name

### User Login
Users can log in using their username and password. Upon successful authentication, a JSON Web Token (JWT) is issued for subsequent requests.

## API Endpoints
### Registration
- **POST** `/api/users/register/`
  - Request Body: `{ "username": "string", "email": "string", "password": "string", "first_name": "string", "last_name": "string" }`
  - Response: `{ "id": "integer", "username": "string", "email": "string", "first_name": "string","last_name": "string", "is_staff": "boolean", "is_active": "boolean"}`

### Login
- **POST** `/api/users/login/`
  - Request Body: `{ "username": "string", "password": "string" }`
  - Response: `{ "access": "JWT_TOKEN", "refresh": "JWT_TOKEN" }`

## Security Considerations
- Passwords are hashed using Django's built-in password hashing mechanisms.
- JWT tokens are used for stateless authentication and should be stored securely on the client side.
