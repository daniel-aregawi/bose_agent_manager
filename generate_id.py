from telethon.sync import TelegramClient

# Replace with your own Telegram API credentials
api_id = "28565475"  # Replace with your API ID
api_hash = "98bb1e0a4d435181ff108b964a252eda"  # Replace with your API Hash
phone_number = "+251714147014"  # Replace with your phone number

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
