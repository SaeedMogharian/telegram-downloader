from telethon import TelegramClient, events
import os
import asyncio
from dotenv import load_dotenv


load_dotenv()  # This loads variables from .env file
# --- Configuration from Environment Variables ---
api_id = int(os.getenv('TELEGRAM_API_ID'))  # Get from environment variable
api_hash = os.getenv('TELEGRAM_API_HASH')  # Get from environment variable
channel_username = os.getenv('TELEGRAM_CHANNEL_USERNAME', '@channelid')  # Optional: provide default
download_folder = os.getenv('TELEGRAM_DOWNLOAD_FOLDER', 'telegram_downloads')  # Optional: provide default

# Validate required environment variables
if not api_id or not api_hash:
    raise ValueError("TELEGRAM_API_ID and TELEGRAM_API_HASH environment variables must be set")

allowed_extensions = ('.mp3', '.m4a', '.flac', '.wav')  # Add other formats you need

# Create download folder if it doesn't exist
os.makedirs(download_folder, exist_ok=True)

# --- Create and start the client ---
client = TelegramClient('session_name', api_id, api_hash)

async def download(message):
    """Download files from a message."""
    if message.media:
        # Check if the media is a document (which files like MP3 often are)
        if hasattr(message.media, 'document'):
            file_attributes = message.media.document.attributes
            file_name = None
            
            # Try to get the file name from its attributes
            for attr in file_attributes:
                if hasattr(attr, 'file_name'):
                    file_name = attr.file_name
                    break
            
            # If a file name exists and is an file, download it
            if file_name and file_name.lower().endswith(allowed_extensions):
                file_path = os.path.join(download_folder, file_name)
                
                # Check if file already exists to avoid re-downloading
                if not os.path.exists(file_path):
                    print(f"Downloading file: {file_name}")
                    await message.download_media(file=file_path)
                    print(f"Successfully downloaded: {file_name}")
                else:
                    print(f"File already exists: {file_name}")
        
        # Also check for audio media type
        elif hasattr(message.media, 'audio'):
            # For audio media types, we need to create a filename
            file_name = f"audio_{message.id}.mp3"
            file_path = os.path.join(download_folder, file_name)
            
            if not os.path.exists(file_path):
                print(f"Downloading audio message: {file_name}")
                await message.download_media(file=file_path)
                print(f"Successfully downloaded: {file_name}")
            else:
                print(f"File already exists: {file_name}")

async def main():
    """Main function to download songs from a Telegram channel."""
    client = TelegramClient('session_name', api_id, api_hash)
    
    await client.start()
    print("Client created. Starting download...")
    
    # Download past messages from the channel
    total_downloaded = 0
    async for message in client.iter_messages(channel_username):
        await download(message)
    
    print("Download process completed!")
    await client.disconnect()

if __name__ == '__main__':
    asyncio.run(main())