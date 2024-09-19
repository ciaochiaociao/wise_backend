# Wise Backend
This is the backend for the Wise Assistant project, built with Django and PostgreSQL.

## Setup
1. Ensure you have Python and PostgreSQL installed on your system.
2. Clone the repository:
```
git clone <repository-url>
cd wise_backend
```
3. Create a virtual environment by conda:
```bash
(base) $ conda create -f environment.yml
```
4. Set up the database:
```bash
(base) $ conda activate wise-backend
(wise-backend) $ python manage.py migrate
```
5. Start the development server:
```bash
python manage.py runserver
```

## Database Setup
1. Ensure you have PostgreSQL installed on your system.
2. Create a new PostgreSQL database named 'wise':
```bash
createdb wise
```
3. Set up your database credentials in a .env file in the project root:
```bash
POSTGRESQL_PASSWORD=your_password_here
```

4. Run the database setup script:
```bash
cd db
.\run.bat
```

5. Apply Django migrations:
```bash
python manage.py migrate
```

6. (Optional) Seed the database with initial data:
```bash
python manage.py seed_emotion_records
```

## API Documentation
The API documentation is available at:
```bash
http://127.0.0.1:8000/api/schema/swagger-ui/
```
