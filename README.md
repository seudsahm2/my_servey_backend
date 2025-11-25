# Islamic Learning Survey Platform - Backend

Django REST Framework backend for collecting and analyzing survey responses from students and teachers.

## Features

- ✅ Student Survey API (11 questions)
- ✅ Teacher Survey API (12 questions)
- ✅ Analytics Endpoints with aggregated data
- ✅ Django Admin for data management
- ✅ PostgreSQL/Supabase integration
- ✅ CORS configured for Next.js frontend

## Quick Start

### 1. Install Dependencies

```bash
# Create and activate virtual environment (recommended)
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On MacOS/Linux

# Install packages
pip install -r requirements.txt
```

### 2. Configure Environment

Create `.env` file in the root directory:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Supabase PostgreSQL
DB_NAME=your_db_name
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=your-project.supabase.co
DB_PORT=5432

CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
```

### 3. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Superuser

```bash
python manage.py createsuperuser
```

### 5. Run Server

```bash
python manage.py runserver
```

Server runs at `http://127.0.0.1:8000/`

## API Endpoints

### Surveys
- `POST /api/surveys/student/` - Submit student survey
- `POST /api/surveys/teacher/` - Submit teacher survey
- `GET /api/surveys/student/` - List student surveys
- `GET /api/surveys/teacher/` - List teacher surveys

### Analytics
- `GET /api/analytics/students/` - Student analytics
- `GET /api/analytics/teachers/` - Teacher analytics  
- `GET /api/analytics/summary/` - Overall summary

### Admin
- Access at `/admin/` with superuser credentials

## Database Models

**StudentSurvey**: 11 questions covering experience, preferences, pricing, subjects, trust factors

**TeacherSurvey**: 12 questions covering background, capacity, rates, topics, platform interest

## Tech Stack

- Django 4.2.7
- Django REST Framework 3.14.0
- PostgreSQL (via Supabase)
- django-cors-headers
- python-decouple
