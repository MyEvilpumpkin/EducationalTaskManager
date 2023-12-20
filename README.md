# EducationalTaskManager

## Description
The Educational Task Manager is a tool designed to help students manage their educational tasks. It provides a platform for tracking deadlines and maintaining motivation, ensuring that students can effectively organize their academic workload. The application can be utilized in two ways: through a Streamlit web interface or via a Telegram bot.

## Prerequisites: 


Before you can run the application, you need to obtain an iCal URL for Google Calendar, a Telegram bot token, a Yandex GPT API key, and a Yandex Cloud folder ID (GPT_CATALOG). Here's how you can get these:

- Google Calendar iCal URL: Follow the instructions on [this page](https://support.google.com/calendar/answer/37648?hl=en) to get the iCal URL of your Google Calendar.

- Telegram: Follow the instructions on [this page](https://core.telegram.org/bots#botfather) to create a new bot with BotFather and get your bot token.

- Yandex GPT: Follow the instructions on [this page](https://cloud.yandex.com/en/docs/yandexgpt/quickstart) to create a new Yandex Cloud account, enable the Yandex GPT API, and get your API key.

- Yandex Cloud Folder ID (GPT_CATALOG): Follow the instructions on [this page](https://cloud.yandex.com/en/docs/resource-manager/operations/folder/get-id) to get your Yandex Cloud folder ID.

Once you have obtained your iCal URL, bot token, API key, and folder ID, create a `secrets.json` file in the root directory of the project. Use the `secrets_file_template.json` file as a template. Replace the placeholders with your actual iCal URL, bot token, API key, and folder ID.

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
   python telegram_bot.py
   ```
   Then open your Telegram app and search for the bot using its username.

   - Docker:
   
   First, you need to build the Docker images for the Streamlit app and the Telegram bot:

   ```bash
  docker compose build educational_task_manager
   ```
   
   Then, you can run the services separately with these commands:

   ```bash
docker compose up -d streamlit_app
docker compose up -d telegram_bot
   ```
   
   For the Streamlit app, open your web browser and go to `http://localhost:8501`.

