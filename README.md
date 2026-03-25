# TikTok Clone (Django)

## Project Overview
This is a lightweight TikTok replica built using **Django** for the backend and **HTML/CSS/JavaScript** for the frontend. The application allows users to:

- Browse a scrollable video feed
- Like videos
- View user profiles and uploaded videos
- Sign up, log in, and log out

> ⚠️ LangChain integration for AI-based recommendations was initially explored but not implemented due to technical constraints. The prototype currently uses a basic feed sorted by upload time.

---

## Features Implemented

| Feature | Status |
|---------|--------|
| Video Feed | ✅ |
| Like System | ✅ |
| User Signup/Login/Logout | ✅ |
| User Profile (Bio + Profile Picture) | ✅ |
| AI Recommendations (LangChain) | ❌ |
| Comments & Share | ❌ |

---

## Project Structure
tiktok_clone/
├── tiktok/
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ └── asgi.py
├── core/
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── templates/core/
│ │ ├── index.html
│ │ ├── signup.html
│ │ ├── login.html
│ │ └── profile.html
│ └── static/core/
│ ├── css/style.css
│ └── js/script.js
├── manage.py
└── db.sqlite3


---

## Installation & Setup

1. **Clone the repository**  
```bash
git clone <your-repo-url>
cd tiktok_clone

# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

python manage.py runserver

Adding Videos

Videos can be added through the Django admin panel:

Navigate to http://127.0.0.1:8000/admin/
Login using superuser credentials
Add videos with:
Title
Video URL
Uploaded By (user)
