# 📰 Auto News Fetcher & Dashboard

A Django-based web application that automatically fetches the latest **India news headlines** from NewsAPI and displays them in a simple dashboard.

---

## 📦 Features
- Fetches **top headlines** from NewsAPI for India (`country=in`)
- Stores news in a Django model (`NewsArticle`)
- Displays headlines in a simple web dashboard
- Supports manual news fetching using a custom Django management command
- Can be extended for scheduled background fetching (CRON/APScheduler)

---

## 🛠️ Setup Instructions
1️⃣ Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/auto-news-fetcher.git
cd auto-news-fetcher

2️⃣ Create Virtual Environment

python -m venv venv

Activate the environment:

venv\Scripts\activate

3️⃣ Install Requirements

pip install -r requirements.txt

4️⃣ Create .env File
Inside the project root, create a .env file:

NEWS_API_KEY=189bfa84fda245e5a2af6b468a6b04ba

5️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate

6️⃣ Start the Development Server

python manage.py runserver

📰 Fetching News
To manually fetch latest news:

python manage.py fetch_news

🛠 How It Works
services.py handles fetching articles from NewsAPI.

models.py defines the NewsArticle model for storage.

fetch_news is a Django management command that calls the fetcher.

Templates render the dashboard for viewing articles.




