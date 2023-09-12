# Flask CRUD API with SQLAlchemy and Marshmallow

This is a simple Flask application that implements a CRUD (Create, Read, Update, Delete) API for managing a list of persons. It uses SQLAlchemy for database management and Marshmallow for data serialization. This API allows you to create, read, update, and delete person records.

## Getting Started

### Prerequisites
- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-Marshmallow
- SQLite or another compatible database

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/DejiFN/Stage2HNX.git
   ```

2. Change to the project directory:

   ```bash
   cd flask-crud-api
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. Set the `DATABASE_URI` environment variable to point to your database (e.g., SQLite database URI). You can set it in your system environment or create a `.env` file in the project directory and add the following line:

   ```
   DATABASE_URI=sqlite:///your_database.db
   ```

2. Start the Flask application:

   ```bash
   python app.py
   ```

The API should now be running on [http://localhost:10000/api](http://localhost:10000/api).

Can check the hosted functionality at [https://stage2-ctuf.onrender.com/api]

## API Endpoints
Before testing with postman make sure you set
![image](https://github.com/DejiFN/Stage2HNX/assets/82783426/7582c268-4293-4086-858f-eb2b83f671d4)

### Create a New Person

- **Endpoint**: `POST /api`
- **Request Body**: JSON
  ```json
  {
    "name": "John Doe",
    "details": "A sample person"
  }
  ```
- **Response**: JSON
  ```json
  {
    "id": 1,
    "name": "John Doe",
    "details": "A sample person"
  }
  ```

### Retrieve All Persons

- **Endpoint**: `GET /api`
- **Response**: JSON
  ```json
  [
    {
      "id": 1,
      "name": "John Doe",
      "details": "A sample person"
    },
    {
      "id": 2,
      "name": "Jane Smith",
      "details": "Another person"
    }
  ]
  ```

### Retrieve a Single Person

- **Endpoint**: `GET /api/<int:id>`
- **Response**: JSON
  ```json
  {
    "id": 1,
    "name": "John Doe",
    "details": "A sample person"
  }
  ```

### Update a Person

- **Endpoint**: `PUT /api/<int:id>`
- **Request Body**: JSON
  ```json
  {
    "name": "Updated Name",
    "details": "Updated details"
  }
  ```
- **Response**: JSON
  ```json
  {
    "id": 1,
    "name": "Updated Name",
    "details": "Updated details"
  }
  ```

### Delete a Person

- **Endpoint**: `DELETE /api/<int:id>`
- **Response**: JSON
  ```json
  {
    "success": "Person has been removed"
  }
  ```

## Error Handling

The API handles the following HTTP error codes and returns JSON responses:

- 400 Bad Request
  ```json
  {"error": "Misunderstood"}
  ```

- 401 Unauthorized
  ```json
  {"error": "Unauthorized"}
  ```

- 404 Not Found
  ```json
  {"error": "Not found"}
  ```

- 500 Internal Server Error
  ```json
  {"error": "Server error"}
  ```


# UML IMAGE
![image](https://github.com/DejiFN/Stage2HNX/assets/82783426/46ca309e-a5a8-4767-a55a-1757fbb876b2)


# ER IMAGE
![image](https://github.com/DejiFN/Stage2HNX/assets/82783426/6b6ab8db-5aba-4e0e-88c8-9fc329d9ba8d)


## assumption
all queries are done with id as name cannot be unique


## Usage

You can use this Flask CRUD API as a template for building your own API for managing data entities. Customize the data model, routes, and error handling as needed for your application.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
