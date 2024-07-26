import pyttsx3
import asyncio

async def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
