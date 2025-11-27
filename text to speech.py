import pyttsx3

speaker = pyttsx3.init()
text = input("Enter your text : ")
speaker.say(text)
speaker.runAndWait()