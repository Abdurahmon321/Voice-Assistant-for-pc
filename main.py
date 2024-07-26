from speech_to_text import recognize_speech
from commands import execute_command
import asyncio


async def main():
    while True:
        text = await recognize_speech()
        if text:
            await execute_command(text.lower())

if __name__ == "__main__":
    asyncio.run(main())
