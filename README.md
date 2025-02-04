# VSMS Project

This project is a Virtual Stock Management System (VSMS) built with Django and Django REST Framework.

## Features

- Supplier management
- Item and stock management
- API documentation with Swagger and ReDoc

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd <project-directory>
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

5. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

6. Run the migrations:
   ```bash
   python manage.py migrate
   ```

7. Start the development server:
   ```bash
   python manage.py runserver
   ```

## API Documentation

- Swagger UI: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
- ReDoc: [http://localhost:8000/redoc/](http://localhost:8000/redoc/)

## License

This project is licensed under the BSD License.