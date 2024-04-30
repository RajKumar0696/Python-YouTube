# Details="""NAME:RAJKUMAR "\n"
# Address:A/25 Bajanai kovil street melanur "\n"
# Pincode:602021
# """
# print(Details,file=open("/home/raj/Documents/Python/print_func",'w'))
# print("completed")
#


#Python 2.x program to transcribe an Audio file
import speech_recognition as sr

AUDIO_FILE = ("welcome_bt.wav")

# use the audio file as the audio source

r = sr.Recognizer()

with sr.AudioFile(AUDIO_FILE) as source:
	#reads the audio file. Here we use record instead of
	#listen
	audio = r.record(source)

try:
	print("The audio file contains: " + r.recognize_google(audio))

except sr.UnknownValueError:
	print("Google Speech Recognition could not understand audio")

except sr.RequestError as e:
	print("Could not request results from Google SpeechRecognition service; {0}".format(e))

