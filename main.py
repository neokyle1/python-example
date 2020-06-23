from gtts import gTTS
from playsound import playsound
import os
import sys
import requests
import json
import time


my_dictionary = {
    'name': 'Trey',
    'age': 27,
    'friends': ['kyle', 'someone else?']
}
variable = my_dictionary['friends'][0]
people = [my_dictionary, {
    'stds': 'herps',
}]
print(people[1]['stds'])

# https://developers.facebook.com/tools/explorer/
token = os.environ['APITOKEN']

# curl -X GET "https://graph.facebook.com/oauth/access_token?client_id={your-app-id}&client_secret={your-app-secret}&grant_type=client_credentials"

# while True:
print('starting loop')
response = requests.get(f'https://graph.facebook.com/v7.0/me/feed?fields=from,message&access_token={token}')
if response.status_code != 200:
    print('Boo!')
    sys.exit(1)
jsondata = json.loads(response.text)
from_name = jsondata['data'][0]['from']['name']
message = jsondata['data'][0]['message']
speech_message = f"Message from {from_name}, {message}"
tts = gTTS(speech_message)
tts.save('hello.mp3')
playsound('hello.mp3')
print('finishing loop')
time.sleep(2)

