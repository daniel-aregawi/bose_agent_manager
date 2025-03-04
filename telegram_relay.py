from telethon import TelegramClient, events

# Replace these with your own values
api_id = 'Your Telegram API ID'  # Your Telegram API ID
api_hash = 'api hash'  # Your Telegram API Hash

# Account B's phone number and session name
phone_number = '+251.....'  # Phone number of Account B
session_name = 'account_b_session'  # Session name for Account B

# Account A and C IDs (replace with actual numeric IDs)
account_a = `replace Numeric ID of Account A`  # Numeric ID of Account A
account_c = `replace Numeric ID of Account C`  # Numeric ID of Account C

# Initialize the Telegram client
client = TelegramClient(session_name, api_id, api_hash)

# Event handler for incoming messages to Account B
@client.on(events.NewMessage)
async def forward_messages(event):
    # Debug: Print the incoming message details
    print(f"New message received from {event.sender_id}: {event.text}")

    # Get the sender's ID
    sender_id = event.sender_id

    # Debug: Print the sender's ID and account IDs
    print(f"Sender ID: {sender_id}")
    print(f"Account A ID: {account_a}")
    print(f"Account C ID: {account_c}")

    # Forward messages from Account A to Account C
    if sender_id == account_a:
        await client.send_message(account_c, event.message)
        print(f"Forwarded message from Account A ({account_a}) to Account C ({account_c})")

    # Forward messages from Account C to Account A
    elif sender_id == account_c:
        await client.send_message(account_a, event.message)
        print(f"Forwarded message from Account C ({account_c}) to Account A ({account_a})")

# Start the client and listen for messages
print("Listening for messages...")
with client:
    client.run_until_disconnected()
