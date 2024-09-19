# Wise Backend
This is the backend for the Wise Assistant project, built with Django and PostgreSQL.

## Setup
1. Ensure you have Python and PostgreSQL installed on your system.
2. Clone the repository:
```
git clone <repository-url>
cd wise_backend
```
3. Create a virtual environment:
```bash
python -m venv venv
source venv/Scripts/activate
```
4. Install dependencies:
```bash
pip install -r requirements.txt
```
5. Set up the database:
```bash
python manage.py migrate
```
6. Start the development server:
```bash
python manage.py runserver
```