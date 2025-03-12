## Library Management System


Description:


Create an application for library management where users can search for books, and borrow them. Create a simple admin panel for it


User Roles:


Anonymous users can browse books but cannot borrow them.
Registered users can search for and borrow books.
Administrators can add/remove books and manage users.
Authentication and Authorization:


Allow user registration and login.
Implement JWT authentication to secure the API.


Database Models:


User model (extended Django User model).
Book model containing fields such as title, author, ISBN, page count, availability, etc.
Loan model to track which user borrowed which book and when.


API:
Endpoint for borrowing and returning books.


Testing:


Write unit tests for models, views, and serializers.
Write integration tests to verify the main functionalities of the API.


Documentation:


Use Swagger or DRF-YASG for automatic API documentation generation.
Add a README file with instructions for deploying and running the project.


Deployment:


Prepare the project for deployment on Heroku or another hosting platform (including configuration for PostgreSQL).
Create a simple Dockerfile for running the application in a Docker container.


Bonus Points:


Implement filtering and pagination for books.
Securing the application against common attacks (CSRF, XSS, SQL Injection).


Prerequisites:
Technology: Django, Django REST Framework, PostgreSQL
Tools: Docker, Git, Heroku
Testing: Pytest or unit test, Coverage
