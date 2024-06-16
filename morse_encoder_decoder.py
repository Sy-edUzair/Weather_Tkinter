import os
import csv
import sys
import time
from playsound import playsound
from gtts import gTTS

#reading csv file where morse codes for characters are saved
morse_code_dict ={} #for encoding
with open("MorseDict.csv","r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        char,code=row
        morse_code_dict[char]=code
    
decode_morse_code_dict = {v: k for k, v in morse_code_dict.items()} #for decoding

def morse_code_audio(msg: str):
        for char in msg:
            if char == ".":
                playsound("shortbeep.mp3")
                time.sleep(0.1)
            elif char == "-":
                playsound("longbeep.mp3")
                time.sleep(0.1)
            elif char == "|" or char == " ":
                time.sleep(0.3)
            else:
                raise ValueError
        
def text_to_speech(msg:str):
        tts = gTTS(text=msg, lang='en')
        tts.save("text_audio.mp3")
        playsound("text_audio.mp3")
        os.remove("text_audio.mp3")


def encode(morse_dict: dict,message: str):
        """ Encodes a message into Morse Code """
        msg = " ".join(morse_dict[char] for char in message.upper())
        return msg
    
def decode(decode_morse_dict: dict, message:str):
        """ Decode Morse code to English """
        msg = " ".join(decode_morse_dict[char] for char in message.split(" "))
        return msg.lower().capitalize()

def main():
    txt = "Hi I am Megan Morse aka M'Gann M'orzz. I will be serving as your morse code translator via the powers of my telepathic link. Are you Ready?"
    print(txt)
    text_to_speech(txt)

    print("Yes/No? ", end="")
    ch = input().lower()
    if ch == "yes" or ch == "y":
        txt="Great. Initiating Telepathic link..."
        print(txt)
        text_to_speech(txt)
        playsound("longbeep.mp3")
        txt="Link Established..."
        print(txt)
        print()
        text_to_speech(txt)
         
        while True:
            print("Select one of the options:")
            print("1.Translate English to Morse Code")
            print("2.Translate Morse Code to English")
            print("3.Exit")
            try:
                choice = int(input("Choice: "))

                if choice == 1:
                    msg = input("Enter your message: ")
                    try:
                        encoded = encode(morse_code_dict,msg)
                        print(encoded)
                        morse_code_audio(encoded)
                    except KeyError:
                        print("Invalid Character")
                        sys.exit(1)
                elif choice == 2:
                    msg = input("Enter your morse code: ")
                    try:
                        decoded = decode(decode_morse_code_dict,msg)
                        print(decoded)
                        try:
                            text_to_speech(decoded)
                        except AssertionError:
                            pass
                    except KeyError:
                        print("Invalid Character")
                        sys.exit(1)
                elif choice == 3:
                    print("Exiting")
                    sys.exit(1)
                else:
                    continue
            except ValueError:
                pass
    else:
        txt="It was lovely having you...Have a great day :)"
        print(txt)
        text_to_speech(txt)

if __name__ == "__main__":
    main()
          










