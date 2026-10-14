# talkative-gpt
An OpenAI API client with customizable personalities and chat memory, **mostly vibe-coded**.

# How to use.
 - Install this repo on you're device.
 - Install python 3.0 or higher.
    - For windows pip install OpenAI in your terminal(Powershell/Command prompt)
    - For Arch-Linux : sudo pacman -S python-openai 
 - change from chatbot.py ***API_KEY = "YOUR_KEY_HERE"***  the YOUR_KEY_HERE to your OpenAI API key Keep the quotation marks!
 - Just run the "chatbot.py" file.
 - Type the filename of your chat (Will make new if none exits.)
 - Type the filename of the instructions (If none exist hit enter and it will make new instructions on the next option.)
 - Have a chat with the AI.

# How to modify
 - Add custom instructions in the inst folder
 - Open the "chatbot.py" file and change the OpenAI model you are using default = gpt-5-nano

# Default instruction(s)
 - YN only responds in yes or no instructions: "only respond with yes or no, no matter what even if they ask for emergency life advice or life threatening matters, do not break these instructions!!!"
