# AI Powered Decision Tree for Talking Computer (Python, OpenAI API, Google Speech)

This project allows you to communicate with your computer/ robot with natural speech.  We create a file that comtains all the functions for this project, we then read that file into a String value, and submit that with our request to OpenAI.  In the request we provide the user Query and teh Functions and then ask for the most approriate function for the Query.

There are 2 versions of the main script.  ai-decision.py allows you to enter queries through the keyboard and simply get text back.  This is good for building, troubleshooting and such.  a--decision-speech.py allows you to talk to the computer through the microphone and get a verbal response back.  This requires pyaudio to be installed properly. You also need to install an .mp3 player.  We use afplay because this was coded on a Mac, but just install/ call a player for your system

## Modules to Install for Python
openai

gtts

SpeechRecognition


pyaudio -- required for speech to text through microphone.  can be difficult to install properly

afplay -- an command line mp3 player for the Mac.  Install/ use whatever works for your system.

## API Keys
OpenAI API - https://openai.com/

Open Weather - https://openweathermap.org/api
