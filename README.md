# Task Management API (my_API_app)

A modular API built with Python and Flask for managing a task list. This application uses a Blueprint-based architecture to separate routing logic from centralized error handling.

## Project Structure

* **app.py**: The entry point that initializes the Flask app and registers the `tasks_bp` and `errors_bp` blueprints.
* **routes.py**: Defines endpoints for CRUD operations on tasks.
* **models.py**: Contains the mock database (list of dictionaries) and functions for data manipulation.
* **errors.py**: Implements global error handlers using `@app_errorhandler` to return JSON responses instead of HTML.

## Features

* **Modular Architecture**: Separates concerns using Flask Blueprints.
* **Unique Identification**: Uses `uuid` to generate unique IDs for every new task.
* **Custom JSON Errors**: Overrides default Flask/Werkzeug HTML errors with a structured JSON format.
* **Input Validation**: Includes checks for JSON body presence, string type for titles, and boolean type for task completion status.

## API Endpoints

### Tasks Collection
* **GET `/tasks`**: Retrieve the full list of tasks.
* **POST `/tasks`**: Create a new task.
    * **Body**: `{"title": "string"}`

### Individual Task Operations
* **GET `/tasks/<id>`**: Retrieve a specific task by ID.
* **PUT `/tasks/<id>`**: Update an existing task's title and status.
    * **Body**: `{"title": "string", "completed": boolean}`
* **DELETE `/tasks/<id>`**: Remove a task from the list.

## Error Handling

The API returns consistent JSON objects for errors:

| Code | Custom Message | Scenario |
| :--- | :--- | :--- |
| **400** | "bad request use correct json format and str in title" | Missing or malformed JSON body. |
| **404** | "Not Found" | Requested Task ID does not exist. |
| **405** | "Method not allowed for this endpoint..." | Using the wrong HTTP method (e.g., POST to a GET-only route). |
| **422** | "invalid input of data" | Title is empty or contains only spaces. |

## Getting Started

1. **Install Dependencies**:
   ```bash
   pip install flask