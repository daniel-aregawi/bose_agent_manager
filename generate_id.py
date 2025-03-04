from telethon.sync import TelegramClient

# Replace with your own Telegram API credentials
api_id = "Replace with your API ID"  # Replace with your API ID
api_hash = "Replace with your API Hash"  # Replace with your API Hash
phone_number = "+251......"  # Replace with your phone number

# Start Telegram Client
client = TelegramClient("get_user_id", api_id, api_hash)
client.start(phone_number)

# Fetch your own user ID
me = client.get_me()
print(f"Your Telegram ID: {me.id}")

# Fetch other user's ID (replace username)
username = input("Enter the username or phone number of the user: ")
user = client.get_entity(username)
print(f"User ID for {username}: {user.id}")

client.disconnect()
