# EducationalTaskManager

## Description
The Educational Task Manager is a tool designed to help students manage their educational tasks. It provides a platform for tracking deadlines and maintaining motivation, ensuring that students can effectively organize their academic workload. The application can be utilized in two ways: through a Streamlit web interface or via a Telegram bot.

## Installation
```bash
git clone https://github.com/username/EducationalTaskManager.git
cd EducationalTaskManager
pip install -r requirements.txt
```

## Usage

   - Streamlit:
   ```bash
   cd src
   python streamlit_app.py
   ```
   Then open your web browser and go to `http://localhost:8501`.

   - Telegram Bot:
   ```bash
   cd src
   python tg_bot.py
   ```
   Then open your Telegram app and search for the bot using its username.

   - Docker:
   
   First, you need to build the Docker images for the Streamlit app and the Telegram bot:

   ```bash
   docker-compose build streamlit
   docker-compose build tg_bot
   ```
   
   Then, you can run the services separately with these commands:

   ```bash
   docker-compose up streamlit
   docker-compose up tg_bot
   ```
   
   For the Streamlit app, open your web browser and go to `http://localhost:8501`.

