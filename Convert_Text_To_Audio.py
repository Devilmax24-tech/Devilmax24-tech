print('\t\t\t\t\t__ _ __WELCOME to oUr GTTS ConVErTOR😍😍__ _ __\n\n')
from gtts import gTTS
import os

def text_to_speech(user_text, language='en', slow=False, filename='Audio.mp3'):
    tts = gTTS(text=user_text, lang=language, slow=slow)
    tts.save(filename)
    print(f"Audio saved as {filename}")
    try:
        os.system(f'start {filename}')  # For Windows
    except Exception:
        pass


#  text input
user_text = input('Write your comment:\n')

# Language selection
print("Select the English accent:")
print('''1: Hindi (hi)
2: India (en-in)
3: Australia (en-au)
4: Canada (en-ca)
5: US (en)
6: Ireland (en-ie)
7: South Africa (en-za)''')
accent_choice = input("Enter the number (1-7): ")

accent_map = {
    '1': 'hi',
    '2': 'en-in',
    '3': 'en-au',
    '4': 'en-ca',
    '5': 'en',
    '6': 'en-ie',
    '7': 'en-za'
}

# If invalid choice then, ByDefault to US English
language = accent_map.get(accent_choice, 'en')  


# Speed selection
speed_choice = input('''Select the speed:
1: Normal
2: Slow
Enter 1 or 2: ''')
if speed_choice == '2':
    slow = True
elif speed_choice == '1':
    slow = False
else:
    print('Invalid choice..\nByDefault speed_choice "Normal"')
    slow = False

# Convert text to speech
text_to_speech(user_text, language=language, slow=speed_choice)
