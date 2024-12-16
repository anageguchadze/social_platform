# social_platform

🚀 Overview
Welcome to the Social Platform Project!
This is a Django-based web application utilizing REST APIs, PostgreSQL as the database, JWT authentication, and other modern technologies for seamless user interaction.

🛠️ Technologies Used
Django 5.x
PostgreSQL for database
Django REST Framework for building APIs
JWT Authentication with djangorestframework-simplejwt
Drf-YASG for API documentation (Swagger & ReDoc)
Push Notifications integration support
Python 3.x

📂 Table of Contents
Features
Installation
Setup with PostgreSQL
Configuration
Running the Application
API Documentation
Contributing
License

🎉 Features
✅ Core features:
User registration & authentication
JWT Token-based authentication
REST API endpoints
Database migrations with PostgreSQL
API documentation with Swagger and ReDoc
Push Notifications support

🛠️ Installation
Clone the repository:
git clone https://github.com/anageguchadze/social_platform.git

Set up a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install dependencies:
pip install -r requirements.txt

⚙️ Setup with PostgreSQL
Make sure you have PostgreSQL installed.
Update the following PostgreSQL settings in settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'social_platform',
        'USER': 'postgres',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

Run migrations:
python manage.py makemigrations
python manage.py migrate

🛡️ Configuration
If you want to use environment variables (.env) for sensitive keys and database configurations:
Create a .env file in the root directory of the project with the following structure:
makefile
Copy code
DATABASE_NAME=social_platform
DATABASE_USER=your_db_user
DATABASE_PASSWORD=your_db_password
DATABASE_HOST=localhost
DATABASE_PORT=5432
SECRET_KEY=your_secret_key
DEBUG=True

Install python-dotenv if needed:
pip install python-dotenv

🚀 Running the Application
Start the development server:
python manage.py runserver
Visit http://localhost:8000/ in your browser to interact with the application.

📜 API Documentation
This project uses Swagger & ReDoc for visualizing the RESTful APIs.

Access Swagger here:
http://localhost:8000/swagger/

Access ReDoc here:
http://localhost:8000/redoc/

🤝 Contributing
We welcome contributions! If you find any issues, or want to add features, feel free to fork this repository and submit a pull request.

Steps:
Fork the repository.
Clone your forked repository.
Create a new branch (git checkout -b feature/your-feature-name).
Commit changes and push to your branch.
Submit a pull request.

📄 License
This project is licensed under the MIT License.

