# 🎬 Movie Tracker

Movie Tracker is a full-stack web application built using **Django** and **MySQL** that allows users to search, manage, and track their favorite movies. Users can create an account, maintain a personal watchlist, mark movies as watched/unwatched, and rate them.

---

## 📌 Features

- 🔍 **Movie Search** — Search movies using external APIs (like TMDB or OMDB).
- 📑 **Watchlist Management** — Add or remove movies from your personal list.
- ✅ **Mark as Watched** — Track which movies you've already seen.
- ⭐ **Rate Movies** — Rate and review movies after watching.
- 👤 **User Authentication** — Secure login and registration with Django's auth system.
- 📊 **Dashboard** — See your movie stats and activity.

---

## 🧰 Tech Stack

| Layer        | Technology            |
|--------------|------------------------|
| 💻 Frontend  | HTML, CSS, JavaScript (Django Templates) |
| 🧠 Backend   | Python, Django         |
| 🗃️ Database  | MySQL                  |
| 🔗 API       | [OMDb API](https://www.omdbapi.com/) or [TMDB](https://www.themoviedb.org/documentation/api) |
| 🔐 Auth      | Django Authentication System |

---

## 🖥️ Screenshots (optional)

<img width="1351" height="650" alt="Capture" src="https://github.com/user-attachments/assets/f7deee6e-df08-45e7-8b8b-1b38630d6d9f" />
<img width="1298" height="624" alt="new" src="https://github.com/user-attachments/assets/b340e9ba-5d98-4104-9388-a29dd2aa44b1" />

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python (>= 3.8)
- MySQL
- pip (Python package manager)

---

### 📦 Installation Steps

bash
# Clone the repository
git clone git@github.com:your-username/movie-tracker.git
cd movie-tracker

# Create virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure your MySQL settings in settings.py

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Run the server
python manage.py runserver
