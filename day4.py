import pyttsx3
import os
# engine = pyttsx3.init()
# engine.say("hello sagar")
# engine.runAndWait()


directory_path= '/mems'

contents = os.listdir(directory_path)

for item in contents:
    print(item)
