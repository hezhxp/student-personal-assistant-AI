import speech_recognition as sr
# imports speechrecog library as sr
# it converts audio from microphone into text

r = sr.Recognizer()
# recogniser object - processes audio and converts it to text
    
with sr.Microphone(device_index=None, sample_rate=44100) as source:
    # use default microphone as source + samplerate standard
    print("Listening... Say something!")
    audio = r.listen(source)
    # captures the audio and stores it in audio

try:
    text = r.recognize_google(audio)
    # uses googles free speech to test api to convert audio to text
    # stored in text
    print("You said:    ", text)
except sr.UnknownValueError:
    print("Could not understand audio")
    # occurs if the speech no understand
except sr.RequestError:
    # occurs if api is unreachable or no internet
    print("Could not reach Google API")
