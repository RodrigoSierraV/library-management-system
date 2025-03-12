# Library Management System

## Overview
The Library Management System is a Django-based application designed to manage library operations, including user management, book inventory, and loan tracking. The system supports user roles and authentication, allowing users to register, and log in.

## Features
- User authentication and role management
- Book inventory management
- Loan tracking for borrowed books
- RESTful API endpoints for integration
- Testing suite
- Docker support for easy deployment

## Prerequisites
- Ensure you have Docker and Docker Compose installed on your machine.

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/RodrigoSierraV/library-management-system.git
   cd library-management-system
   ```
2. **Build the Docker Image**
   Run the following command in the root directory of the project to build the Docker image:

   ```
   docker-compose build
   ```

3. **Run the Docker Containers**
   Start the application and database containers using:

   ```
   docker-compose up
   ```

4. **Create a Superuser**
   To access the Django admin, create a superuser by running:

   ```
   docker-compose exec web python manage.py createsuperuser
   ```

## Accessing the Application
- The application will be accessible at `http://localhost:8000`.
- The Django admin interface can be accessed at `http://localhost:8000/admin`.

## Accessing API documentation
- The schema can be downloaded at `http://localhost:8000/api/schema`
- The Swagger UI can be found at `http://localhost:8000/api/schema/swagger-ui/`, and
- ReDoc at `http://localhost:8000/api/schema/redoc/`

## Testing
To run the test suite, use:
```
docker-compose exec web python manage.py test
```

## Testing endpoints
- At root of the project was provided a `api.http` file which can be used in VS Code with the help of the `REST Client` extension to test the endpoints easily.

## Stopping the Application
To stop the running containers, use:

```
docker-compose down
```

## Authentication
For information on authentication and authorization mechanisms, see `docs/authentication.md`.
