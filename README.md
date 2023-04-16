# Whatsapp-Bulk-Messenger

Whatsapp Bulk Messenger automates sending of messages via Whatsapp Web. The tool can you used to send whatsapp message in bulk. Program uses runs through a list of numbers provided in numbers.txt and then tries to send a prediefined (but templated) message to each number in the list. It can also read other columns from the number csv to populate template specific words and then send out a personalized message to the number

Note: The current program is limited to sending only TEXT message


# Requirements

*  Python >= 3.6
*  Chrome headless is installed by the program automatically

# Setup

1. Install python - >=v3.6
2. Run `pip install -r requirements.txt`

# Steps

1. Enter the message you want to send inside `message.txt` file.
2. Enter the list of numbers line-separated in `numbers.txt` file.
3. Enter 10 digit Indian numbers, since the code applies a prefix of 91 at the beginning.
4. Run `python automator.py`.
6. After a while, Chrome should pop-up and open tabs for different numbers.
7. Initially clicking open Whatsapp would only open the chat window, click again for the message to appear automatically.
8. Press `Enter` to start sending out messages.
9. Sit back and relax!

