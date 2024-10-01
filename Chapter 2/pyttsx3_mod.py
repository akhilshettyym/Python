# Install an external module and use it to perform an operation of your interest.

# pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3.

# A TTS engine (Text-to-Speech engine) is software that converts written text into spoken words using synthesized speech. Essentially, it allows computers or other devices to "speak" written content.

# If you get installation errors , make sure you first upgrade your wheel version using : pip install –upgrade wheel

import pyttsx3
a = pyttsx3.init()     #This line initializes the TTS engine. The pyttsx3.init() function returns an instance of the TTS engine, which you will use to control the speech synthesis.

a.say("Ena Bolimaga shoot madbeka")    #The engine.say() function is used to pass the text that you want the engine to speak. In this case, it will speak the sentence "I will speak this text".


a.runAndWait()     #This line tells the engine to start processing the speech (i.e., actually speak the text) and waits for the speech to complete before allowing the program to proceed.




# import pyttsx3
# engine = pyttsx3.init()
# engine.say("I will speak this text")
# engine.runAndWait() 
