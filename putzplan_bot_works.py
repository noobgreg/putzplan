import datetime
import time
import telegram

BOT_TOKEN = None ## insted of 'None' add your bots token 
CHAT_ID = None ## insted of 'None' add your chat id

# Replace TOKEN with your bot's token
bot = telegram.Bot(token=BOT_TOKEN)

# Replace CHAT_ID with the chat ID of the group chat
chat_id = CHAT_ID

# Create a list of names
names = ['Name1', 'Name2', 'Name3', 'Name4', 'Name5']

while True:
    # Get the current day and time
    now = datetime.datetime.now()

    # Check if it's Friday at 12:00
    # now.weekday() == 5 and now.hour == 9 and now.minute == 00:
    if now.minute == 19:
        

        # Initialize 3 empty lists
        wohnzimmer = []
        bad = []
        flur = []

        # Assign the first 2 names to list1
        wohnzimmer.append(names[0])
        wohnzimmer.append(names[1])

        # Assign the next 2 names to list2
        bad.append(names[2])
        bad.append(names[3])

        # Assign the last name to list3
        flur.append(names[4])

        # Rotate the names by one index
        names = [names[-1]] + names[:-1]

        # Send the lists to the group chat
        bot.send_message(chat_id=chat_id, text = f'Wohnzimmer: {wohnzimmer[0]} und {wohnzimmer[1]}\n'f'Bad: {bad[0]} und {bad[1]}\n'f'Flur: {flur[0]}')

    # Sleep for 1 minute
    time.sleep(60)
