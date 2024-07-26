import pyautogui
import subprocess
import webbrowser
import os
from text_to_speech import speak
import keyboard
import asyncio


async def open_program(program_name):
    if program_name == "notepad":
        subprocess.Popen(["notepad.exe"])
        await speak("Notepad is opened.")
    elif program_name == "chrome":
        webbrowser.open("http://www.google.com")
        await speak("Chrome is opened.")
    else:
        await speak(f"Sorry, I can't open {program_name}.")


async def control_program(action):
    if action == "maximize":
        pyautogui.hotkey('win', 'up')
    elif action == "minimize":
        pyautogui.hotkey('win', 'down')
    elif action == "close":
        pyautogui.hotkey('alt', 'f4')
    elif action == "type":
        pyautogui.typewrite('Hello, this is a test!', interval=0.1)
    elif action == "sound up":
        keyboard.press_and_release('volume up')
        await speak("Sound up.")
    elif action == "sound down":
        keyboard.press_and_release('volume down')
        await speak("Sound down.")
    elif action == "sound pause":
        keyboard.press_and_release('play/pause media')
        await speak("Paused.")
    elif action == "sound play":
        keyboard.press_and_release('play/pause media')
        await speak("Playing.")
    else:
        await speak(f"Sorry, I can't perform {action} action.")


async def execute_command(command):
    if "open" in command:
        program_name = command.replace("open", "").strip()
        await open_program(program_name)
    elif any(action in command for action in ["maximize", "minimize", "close", "type", "sound up", "sound down", "sound pause", "sound play"]):
        action = command.strip()
        await control_program(action)
    elif "shutdown" in command:
        os.system("shutdown /s /t 1")
        await speak("Shutting down the system.")
    else:
        await speak(f"Sorry, I don't understand the command: {command}")
