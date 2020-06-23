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
print (people[1]['stds'])

# https://developers.facebook.com/tools/explorer/
token = os.environ['APITOKEN']
while True:
    print('starting loop')
    response = requests.get('https://graph.facebook.com/v7.0/me/feed?access_token=' + token)
    if response.status_code != 200:
        print('Boo!')
        sys.exit(1)
    jsondata = json.loads(response.text)
    message = jsondata['data'][0]['message']
    tts = gTTS(message)
    tts.save('hello.mp3')
    playsound('hello.mp3')
    print('finishing loop')
    time.sleep(2)

