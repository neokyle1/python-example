from gtts import gTTS
from playsound import playsound
import os
import requests
import json


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

# token = os.environ['APITOKEN']
# response = requests.get('https://graph.facebook.com/v7.0/me/feed?access_token=' + token)
# jsondata = json.loads(response.text)
# firtdictionary = jsondata['data']
# first_array_value = firstdictionary[0]
# message = first_array_value[]
# tts = gTTS('Hello, my name is trey. Wubbalubbadubdub')
# tts.save('hello.mp3')
# playsound('hello.mp3')
