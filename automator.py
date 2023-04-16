import webbrowser
import urllib.parse

# Read the numbers from file
with open("numbers.txt", "r") as f:
    numbers = [line.strip() for line in f]

# Add "91" to the beginning of each number
numbers = ["91" + number for number in numbers]

# Define the message text
f = open("message.txt", "r", encoding="utf8")
message = f.read()
f.close()

# Encode the message text for use in the URL
encoded_message = urllib.parse.quote(message)

# Create a list of URLs with each number and the updated text
urls = [f"https://wa.me/{number}?text={encoded_message}" for number in numbers]

# Open each URL in the default web browser
for url in urls:
    webbrowser.open(url)
