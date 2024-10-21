
# Flask MongoDB REST API

A Flask-based REST API with MongoDB integration. This project follows a modular structure similar to Express.js, featuring routes, controllers, and database models.

## Features

- **Flask**: Lightweight web framework for building APIs.
- **MongoDB**: NoSQL database integrated using `pymongo`.
- **Environment Variables**: Configuration managed via `.env` files.
- **Modular Structure**: Organized with routes, controllers, and models for maintainability.

## Project Structure

```
flask_project/
├── .env                 # Environment variables
├── app.py               # Main entry point
├── config.py            # Configuration
├── libs/                # Additional libraries
│   └── db.py            # MongoDB connection setup
├── controllers/         # Business logic
│   └── example_controller.py
├── routes/              # Route handling
│   └── example_routes.py
├── models/              # Database models (if required)
├── middleware/          # Custom middleware
│   └── auth_middleware.py
├── utils/               # Utility functions
└── .gitignore           # Git ignore rules
```

## Prerequisites

- Python 3.8 or higher
- MongoDB (local or remote)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/flask-mongo-api.git
   cd flask-mongo-api
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On Mac/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Create a `.env` file in the project root**:
   ```bash
   MONGO_URI=mongodb://localhost:27017/mydatabase
   ```

6. **Run the application**:
   ```bash
   flask run
   ```

   The app will be running on `http://127.0.0.1:5000`.

## API Endpoints

### **GET /api/items**
Retrieve all items from the MongoDB collection.

#### Example:
```bash
GET http://localhost:5000/api/items
```

#### Response:
```json
[
  {
    "_id": "60dbfe9b123abc45ef67",
    "name": "Item 1",
    "description": "First item description"
  },
  {
    "_id": "60dbfe9b123abc45ef68",
    "name": "Item 2",
    "description": "Second item description"
  }
]
```

### **POST /api/items**
Add a new item to the database.

#### Example:
```bash
POST http://localhost:5000/api/items
Content-Type: application/json

{
  "name": "Item 3",
  "description": "New item description"
}
```

#### Response:
```json
{
  "id": "60dbfe9b123abc45ef69"
}
```

## Project Files

- **`app.py`**: The main application file where the Flask app is initialized.
- **`config.py`**: Loads environment variables and other configuration settings.
- **`libs/db.py`**: Handles MongoDB connection logic.
- **`controllers/`**: Contains business logic for interacting with the database.
- **`routes/`**: Defines the API endpoints.
- **`.env`**: Holds environment-specific variables like `MONGO_URI`.
- **`.gitignore`**: Specifies files and directories to ignore in git (e.g., `__pycache__`, virtual environments, `.env`).

## Running Tests (if applicable)

To run tests, use the following command:
```bash
pytest
```

Make sure to have `pytest` installed if you're writing tests for your API.

