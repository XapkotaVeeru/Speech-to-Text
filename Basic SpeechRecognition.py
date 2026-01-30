import speech_recognition as sr

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"User said: {query}")
        return query
    except Exception as e:
        print("Say that again please...")
        return None

text = speech_to_text()
if text:
    print(f"Transcribed: {text}")
