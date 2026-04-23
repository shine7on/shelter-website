![Python](https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

# 🐾 Dog Shelter Website

A dog adoption web application built with **Django** and **Tailwind CSS**. Users can browse dogs available for adoption, filter by breed or status, and submit an adoption application. Shelter staff can manage dogs and applications through the Django admin panel.

---
## 📸 Screenshots

| Dog List | Dog Detail | Admin Page |
|----------|------------|------------|
| <img src="screenshots/dog_list.png" width="350"/> | <img src="screenshots/dog_detail.png" width="350"/> |  <img src="screenshots/admin.png" width="350"/> |

<img src="screenshots/adopt_form.png" width="500"/>

---

## ✨ Features

- Browse available dogs with filters by breed, sex, and status
- Dog detail page with photo, age, weight, and description
- Adoption application form with validation
- Admin panel for managing dogs, breeds, and adoption applications

---

## 🛠 Tech Stack

- Python / Django
- Tailwind CSS (CDN)
- JavaScript
- SQLite
- Django Admin

---

## 🚀 How to Run Locally

```bash
# Clone the repo
git clone https://github.com/your-username/shelter-website.git
cd shelter-website

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create a superuser for admin access
python manage.py createsuperuser

# Start the server
python manage.py runserver
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.
Admin panel is available at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin).

---

## 📁 Project Structure

```
shelter-website/
├── config/              # Django project settings and URLs
├── shelter_web/         # Main app
│   ├── models.py        # Dog, Breed, Adoptation models
│   ├── views.py         # View functions
│   ├── forms.py         # DogForm, AdoptionForm
│   ├── admin.py         # Admin configuration
│   └── templates/       # HTML templates
├── static/              # Static files (CSS, images)
├── media/               # Uploaded dog photos
└── requirements.txt
```

---
