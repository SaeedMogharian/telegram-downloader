# Telegram File Downloader
(Totally AI Generated!)
A Python script to automatically download files from a Telegram channel.

## Features

- Downloads files (the current desired formats: MP3, M4A, FLAC, WAV) from Telegram channels
- Skips already downloaded files to avoid duplicates

## Setup

1. **Get Telegram API Credentials**
   - Visit https://my.telegram.org/apps
   - Create an application and note your `api_id` and `api_hash`

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**
   ```bash
   # Copy the example file
   .env.example -> .env
   
   # Edit .env with your credentials
   .env
   ```

4. **Fill in your `.env` file:**
   ```env
   TELEGRAM_API_ID=your_actual_api_id
   TELEGRAM_API_HASH='your_actual_api_hash'
   TELEGRAM_CHANNEL_USERNAME='@your_channel_username'
   TELEGRAM_DOWNLOAD_FOLDER=telegram_downloads
   ```

## Usage

```bash
python telegram_downloader.py
```

The first time you run the script, it will prompt you to:
1. Enter your phone number (with country code)
2. Enter the verification code sent to Telegram
3. Enter your password (if 2FA is enabled)

After authentication, it will start downloading files to the specified folder.

## File Structure

```
telegram-downloader/
├── telegram_downloader.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

You can modify `allowed_extensions` in the script to add more formats or change the 