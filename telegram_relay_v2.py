import json
import logging
import sys
import os
from telethon import TelegramClient, events

# Load configuration from config.json
with open("config.json", "r") as config_file:
    config = json.load(config_file)

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("telegram_relay.log"),  # Log to a file
        logging.StreamHandler(sys.stdout),  # Log to console
    ],
)
logger = logging.getLogger(__name__)

# Telegram API credentials
api_id = config["api_id"]
api_hash = config["api_hash"]

# Account B's phone number and session name
phone_number = config["phone_number"]
session_name = config["session_name"]

# Account A and C IDs (ensure they are integers)
account_a = int(config["account_a"])
account_c = int(config["account_c"])

# Initialize the Telegram client
client = TelegramClient(session_name, api_id, api_hash)

# Event handler for incoming messages to Account B
@client.on(events.NewMessage)
async def forward_messages(event):
    try:
        # Log the incoming message
        logger.info(f"New message received from {event.sender_id}: {event.text}")

        # Get the sender's ID
        sender_id = event.sender_id

        # Forward messages from Account A to Account C
        if sender_id == account_a:
            await client.send_message(account_c, event.message)
            logger.info(f"Forwarded message from Account A ({account_a}) to Account C ({account_c})")

        # Forward messages from Account C to Account A
        elif sender_id == account_c:
            await client.send_message(account_a, event.message)
            logger.info(f"Forwarded message from Account C ({account_c}) to Account A ({account_a})")

    except Exception as e:
        logger.error(f"Error forwarding message: {e}")

# Placeholder for handling calls (Currently Not Supported by Telethon)
async def handle_incoming_call(event):
    logger.warning("Telethon does not support call events. Consider using another approach.")

# Function to restart the script on failure
def restart_script():
    logger.info("Restarting script...")
    python = sys.executable
    os.execl(python, python, *sys.argv)

# Start the client and listen for messages
if __name__ == "__main__":
    logger.info("Starting Telegram relay script...")
    try:
        with client:
            client.run_until_disconnected()
    except Exception as e:
        logger.error(f"Script crashed: {e}")
        restart_script()
