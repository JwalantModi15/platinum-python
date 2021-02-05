from win32com.client import Dispatch
import sys
sys.path.append('/mymodules/')
import mymodules
from mymodules.mathy import *
def speak(string):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(string)
speak(responses[0])
speak(responses[1])
print(responses[0])
print(responses[1])
while True:
    print()
    speak("Please Enter Some Text")
    text = input("Please Enter Some Text: ")
    for word in text.split(" "):
        if word.upper() in operations.keys():
            try:
                l=extract_numbers_from_text(text)
                r = operations[word.upper()](l)
                print(r)
            except:
                print("Something is went Wrong Please Retry")
            finally:
                break

        elif word.upper() in commands.keys():
            commands[word.upper()]()
            break
        
    else:
        sorry()
        
