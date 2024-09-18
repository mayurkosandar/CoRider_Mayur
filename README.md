# Flask MongoDB Application

## Overview

This project is a Flask-based REST API that performs CRUD operations on user data stored in a MongoDB database.

## Requirements

- Python 3.x
- Flask
- Flask-PyMongo
- MongoDB

## Installation

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone <your-repository-url>
cd <your-project-directory>
==========================================================
Create and Activate a Virtual Environment
python -m venv venv
venv\Scripts\activate
==========================================================
 Install Dependencies
 pip install -r requirements.txt
==========================================================
Set Up MongoDB & mongosh
==========================================================
Run the Flask Application
flask run
The application will be accessible at http://127.0.0.1:5000/.
==========================================================
API Endpoints
GET /users: Retrieve all users from the database.
POST /users: Create a new user in the database.
GET /users/<id>: Retrieve a specific user by their ID.
PUT /users/<id>: Update a specific user by their ID.
DELETE /users/<id>: Delete a specific user by their ID.
==========================================================
1. Create a New User
Endpoint: POST /users

2. Retrieve All Users
Endpoint: GET /users

3. Retrieve a Specific User
Endpoint: GET /users/<id>

4. Update a User
Endpoint: PUT /users/<id>

5. Delete a User
Endpoint: DELETE /users/<id>
=========================================================
Troubleshooting
MongoDB Issues: Ensure MongoDB is running on the default port (27017) and check for any connection errors in the Flask logs.
Flask Errors: Check the Flask server logs for any error messages and verify your routes and configurations.
=========================================================
Contact
If you have any questions, please contact Mayur Kosandar at mayurkosandar018@gmail.com .