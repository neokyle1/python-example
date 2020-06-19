from gtts import gTTS
from playsound import playsound

tts = gTTS('Hello, my name is trey. Wubbalubbadubdub')
tts.save('hello.mp3')
playsound('hello.mp3')

