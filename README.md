Telegram Message Forwarding Bot

This Python script automates message forwarding between three Telegram accounts using the Telethon library. Account B acts as a relay, automatically forwarding messages between Account A and Account C.

Features

Automatically forwards messages from Account A to Account C.

Automatically forwards messages from Account C to Account A.

Runs in the background, continuously listening for new messages.

Requirements

Python 3.7+

Telethon library

A Telegram API ID and API Hash (obtained from my.telegram.org).

A Telegram account to act as Account B.

Installation

Clone this repository or download the script:

git clone https://github.com/yourusername/telegram-forward-bot.git
cd telegram-forward-bot

Install dependencies:

pip install telethon

Edit telegram_relay.py and replace:

api_id and api_hash with your Telegram API credentials.

phone_number with Account B's phone number.

account_a and account_c with their numeric Telegram user IDs.

How to Get Numeric User IDs

Run the following script to get user IDs:

from telethon.sync import TelegramClient
from telethon.tl.functions.users import GetFullUserRequest

api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
phone = 'YOUR_PHONE_NUMBER'

with TelegramClient('session', api_id, api_hash) as client:
    user = client(GetFullUserRequest('username_here'))
    print(f'User ID: {user.user.id}')

Replace 'username_here' with @username of Account A or C, then run the script and note the printed User ID.

Running the Bot

Start the script by running:

python telegram_relay.py

How It Works

The script logs into Account B.

It listens for incoming messages.

If a message is received from Account A, it forwards it to Account C.

If a message is received from Account C, it forwards it to Account A.

Troubleshooting

If the script is not forwarding messages:

Ensure that Account A and C’s user IDs are correct numeric IDs.

Ensure that Account B has proper permissions and is not restricted by Telegram.

Check if the session file (account_b_session.session) exists and is valid.

Make sure Telethon is installed (pip install telethon).
