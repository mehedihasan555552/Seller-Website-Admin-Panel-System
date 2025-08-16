# Seller Website Admin Panel System

A clean and intuitive admin dashboard designed to empower sellers and administrators with seamless control over their web platform.

##  Project Overview

This project provides an **Admin Panel System** built for managing seller-side website functionalities. Crafted using modern web technologies, it allows admins to register and oversee products, categories, and seller activity—all from a user-friendly interface.

##  Key Features

- **Product Management**  
  Add, edit, delete, and categorize products effortlessly.

- **Category Management**  
  Organize your inventory with custom categories.

- **User Administration**  
  Basic user authentication for admin access and seller oversight.

- **Responsive & Intuitive UI**  
  A clean front-end experience—built with HTML, CSS, and JavaScript—for seamless interaction on desktop and mobile.

*(You can expand this section with features like Dashboard analytics, search/sort, user roles, etc., as applicable.)*

##  Technologies Used

| Layer       | Technologies                        |
|-------------|--------------------------------------|
| Backend     | Python, Django framework             |
| Frontend    | HTML5, CSS3, JavaScript              |
| Database    | SQLite (default in Django projects)  |
| Deployment  | Procfile, `runtime.txt`, `requirements.txt` |

Your project also appears to have a `manage.py`, `db.sqlite3`, and dependency/config files (`requirements.txt`, `runtime.txt`, `Procfile`), indicating readiness for deployment (likely to platforms like Heroku).

##  Getting Started

### **Prerequisites**

- Python 3.x  
- Virtual environment manager (optional, but recommended)

### **Setup & Launch**

```bash
# Clone the repo
git clone https://github.com/mehedihasan555552/Seller-Website-Admin-Panel-System.git
cd Seller-Website-Admin-Panel-System

# (Optional) Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply Django migrations
python manage.py migrate

# Create an admin user (follow prompts)
python manage.py createsuperuser

# Start the development server
python manage.py runserver
