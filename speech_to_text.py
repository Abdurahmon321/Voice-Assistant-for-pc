import speech_recognition as sr
import asyncio


async def recognize_speech():
    loop = asyncio.get_event_loop()
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")

        audio = await loop.run_in_executor(None, recognizer.listen, source)

        try:
            text = await loop.run_in_executor(None, recognizer.recognize_google, audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not get that")
            return ""
        except sr.RequestError:
            print("Request error from Google Speech Recognition service")
            return ""
