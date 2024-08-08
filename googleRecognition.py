import speech_recognition as sr

def holeText()->str:
    '''
    Diese Funktion wird verwendet, um den Text vom Mikrofon abzurufen
    :return:
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        audio_data = r.record(source, duration=2)

        try:
            text = r.recognize_google(audio_data, language="de-DE")

            return text
        except sr.UnknownValueError:

            return "Google could not understand"