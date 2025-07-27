# Complaint Management System

A simple **Django-based web application** to manage complaints between customers, products, employees, and administrators.  
The system supports two roles: **Admin** and **Employee**, and provides a responsive interface for handling complaints, assigning employees, and updating complaint statuses.

---

## 📝 Tech Stack

- **Backend:** Django (Python)
- **Database:** PostgreSQL
- **Frontend:** HTML, CSS, JavaScript (Bootstrap for styling)
- **Maps Integration:** Leaflet (for location selection)

---

## 🚀 Features

### 👩‍💻 Admin Panel
- Employee Management: Create, view, edit employee details.
- Customer Management: Create, view, edit customer details.
- Product Management: Create, view, edit products.
- Complaint Management: Register new complaints, assign employees, update complaints.

### 👷 Employee Panel
- Dashboard showing **assigned** and **unassigned** complaints count.
- View and manage assigned complaints:
  - Update complaint status (**Pending**, **Closed**, **Not Closed**).
  - Add remarks and reports.
- Claim unassigned complaints using the **"Assign to Me"** feature.

### 🌐 Other Features
- **Role-based login** (Admin/Employee).
- Location integration using maps (select latitude and longitude).
- Fully responsive user interface with form validation and error handling.
- Logout and session management.

---

## 📋 Prerequisites

Make sure you have the following installed on your system:
- **Python 3.8+**
- **PostgreSQL**
- **pip** (Python package manager)
- **virtualenv** (optional but recommended)
- **Git**

---

## ⚡ Setup Instructions (Local Development)

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd complaint-management-system
   
2. **Create and activate a virtual environment**
    ```bash
   python -m venv venv
    source venv/bin/activate     # For Linux/Mac
    venv\Scripts\activate        # For Windows
   
3. **Install dependencies**
     ```bash
    poetry install

4. **Setup PostgreSQL database**
    - Create a database (e.g. complaint_db).
    - Update settings.py with your database credentials:
    ```bash
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'complaint_db',
        'USER': '<your-username>',
        'PASSWORD': '<your-password>',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

5.  **Apply migrations** 
    ```bash
        python manage.py makemigrations
        python manage.py migrate
    
6. **Create a superuser (Admin login) **
    ```bash
    python manage.py createsuperuser

7.  **Run the server**
    ```bash
        python manage.py runserver
    
8.  **Go to localhost/login in browser**