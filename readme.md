# Career Portal - LoRa IT Innovations Pvt Ltd

A fully functional Career Portal offering a clean, responsive interface for job seekers to browse and apply for jobs. It includes a powerful admin panel for HR teams to manage job listings, review applications, and update site content—all from a centralized dashboard.

## Features

- View job listings with detailed descriptions
- Submit job applications with resume upload
- Admin dashboard to manage:
  - Job postings
  - View submitted applications
  - Edit home and about page content
  - View contact messages
- Responsive and modern UI (HTML, CSS, Font Awesome)
- Admin login and access control


## Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML5, CSS3
- **Database:** SQLite (default Django DB)
- **Other Tools:** Bootstrap, Font Awesome


## Installation and Setup Instructions

1. **Create Project Directory**
   ```bash
   mkdir careerportal
   cd careerportal

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv env
   env\Scripts\activate  # On Windows

3. **Install all project dependencies**

   ```bash
   pip install \
   django \
   djangorestframework \
   djangorestframework-simplejwt \
   psycopg2-binary \
   python-decouple \
   python-dotenv \
   dj-database-url \`

4. **Create Django Project and App**
   ```bash
   django-admin startproject project
   cd project
   python manage.py startapp app

5. **Make changes in settings.py**
   - Add 'app', to the INSTALLED_APPS list.
   - Configure Database in settings.py ( Used default Database)
   - Add static and media settings for serving CSS and file uploads.
   - Set timezone and language

6. **Apply Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate

7. **Final Setup and Run**
   ```bash
   python manage.py createsuperuser  # Create Superuser for admin panel
   python manage.py runserver   # Run the Development Server
   pip freeze > requirements.txt  # Create Requirements File

8. **Folder Structure**
   ```bash
    careerportal/                  # Root project directory
    │
    ├── app/                      # Main Django app
    │   ├── migrations/           # Database migration files
    │   ├── static/               # Static files (CSS, JS, images)
    │   │   └── css/
    │   │       └── styles.css
    │   ├── templates/            # HTML templates
    │   │   ├── base.html
    │   │   ├── home.html
    │   │   ├── jobs.html
    │   │   ├── job-details.html
    │   │   ├── job_application_success.html
    │   │   ├── about.html
    │   │   ├── contact.html
    │   │   ├── admin_login.html
    │   │   └── admin_dashboard.html
    │   ├── __init__.py
    │   ├── admin.py              # Admin customizations
    │   ├── apps.py
    │   ├── forms.py              # Django Forms
    │   ├── models.py             # Database Models
    │   ├── tests.py
    │   ├── urls.py               # App-specific URLs
    │   └── views.py              # App views
    │
    ├── media/                    # Uploaded files (resumes)
    │
    ├── project/                  # Django project folder
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py               # Project-wide URL routing
    │   ├── wsgi.py
    │   └── asgi.py
    │
    ├── manage.py                 # Django management script
    ├── db.sqlite3                # SQLite database (default)
    └── README.md                 # Project overview and setup instructions


## Development Workflow

 **Create templates** 

This Django project includes the following templates located in the templates

1. **User Pages**

home.html – Landing page with company overview

jobs.html – Browse available job listings

job-details.html – View full job details and apply

job_application_success.html – Confirmation page after form submission

about.html – About the company

contact.html – Contact form for user queries

2. **Admin Pages**

admin_login.html – Admin authentication page

admin_dashboard.html – Overview of job postings, applications, and site management

manage_jobs.html – Add/edit/delete job listings

view_applications.html – View submitted job applications

manage_home.html – Update homepage content

manage_about.html – Edit about page content

view_messages.html – Read contact form submissions

## Implementation 

1. Define Models
Create model classes to represent each feature (e.g., JobDetails, JobApplication).
Whenever we change models, run makemigrations and migrate to apply changes to the database.

2. Create Forms
Use ModelForm to handle form creation and validation based on models.

3. Implement Views
Write views to handle logic, fetch data, and render templates (both function-based and class-based).

4. Set Up URLs
Map views to URLs in both app/urls.py and project/urls.py.

5. Design Templates
Build user and admin HTML templates using Django's template language.

6. Add CSS in Static Folder
Style all pages using external CSS files placed in the static/css/ directory.

7. Configure Admin
Register models in admin.py to manage data from Django Admin Panel.

8. Connect Everything
Link models, forms, views, URLs, templates, and static files to build a functional portal.




