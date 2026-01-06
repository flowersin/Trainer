# IOT Treat Trainer and Discord Bot

## Setup
I have this project set up to have two independent parts: An Aurdino-powered automatic cat food dispenser, (The treat dispenser) and a Discord bot running off a self-hosted VM.  The two halves communicate via a USB/serial connection.

### Treat Dispenser

#### Materials
For this project, I purchased [this](LINK HERE) automatic cat food dispenser.  A lot of other models would likely work as we'll be removing everything but the most fundamental components. You will also need an Arduino, I used an Uno, and a Relay of some kind.

#### Setting up the Hardware
1. Disassemble the treat Dispenser
2. Remove the included PCB/"brain," all we will need is the original power supply, motor and switch to count the rotations.
3. Wire everything up
  - Relay between the motor and the original power supply, connected to Pin 11 on the arduino for control
  - The switch should be connected to ground and Pin 12
4. Flash the Arduino using the Arduino/treatDispenser/treatDispenser.ino file
5. Re-assemble everything, you will need a USB cable to communicate with the Ardunio via it's built in USB port.
6. Connect the USB cable to the system running the discord bot

### Discord Bot
This can be run on any system, but setting up a dedicated server/vm will allow the bot to run 24/7.  Setting up the application as a service on Linux or windows can automate startup.

#### Getting your bot token
Go to [Discord.com](https://discord.com/developers/applications/) and create a new application.  Navigate to your new application -> Bot -> Reset token.  This should give you a string, copy this and save it somewhere private.

#### Add the Bot to a Server
Back in the discord developer portal, you will need to enable some permissions first.  First, enable "Message Content Intent" in bot settings.  Then, Navigate to the OAuth page, and under "OAuth2 URL Generator" Select the "Bot" permission.  Under "Bot Permissions," Select "Send Messages."  Then copy the generated URL and paste it into your web browser.  This page should allow you to select a server to add the bot to, you may need to log-in first.

#### Run the Application
Now, you can either run the bot off of your desktop, or set up a dedicated server to run the bot off of.  The process will be similar for both:

1. Install Python
2. If you are on linux, you will need to set up venv for the project.  This can be safely skipped on other OSes
3. Install discord.py and pyserial via pip
4. Set up service.  
  - The trainer.service file can be used template for linux systems running Systemd.
5. Make sure the bot hows as online on the discord server.  This means it's listening!

#### Use the Application
Send `~treat small` in a channel the bot has access to, it should respond with how many treats it has given.  

#### Troubleshooting the Bot
The bot should respond with errors.  If the bot isn't responding, check .trainer.log in the application directory.