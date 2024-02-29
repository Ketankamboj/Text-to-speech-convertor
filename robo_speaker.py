import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

print("Welcome To The RoboSpeaker Created By Ketan Kamboj")
speaker.speak("Welcome To The RoboSpeaker Created By Ketan Kamboj")
print("Enter 'bye' To Exit")
speaker.speak("Type anything which you want me to speak")

while 1:
    print("Enter The Text You Want To Speak: ")
    s = input()
    speaker.speak(s)
    if s == 'bye':
        break