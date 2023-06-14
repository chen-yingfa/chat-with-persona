from pathlib import Path
from chatbot import Chatbot


OPENAI_API = '...'

INTRO_MSG = '''
=====================================================
=== Welcome to the chatbot with persona inference ===
=====================================================
Instructions:
- Press enter to send.
- Type "exit" to exit.
==== Chat Start ===='''

OUTRO_MSG = '''==== Chat End ===='''


def main():
    cache_dir = Path("cache/temp")
    chatbot = Chatbot(OPENAI_API, cache_dir=cache_dir, do_infer_persona=True)
    print(INTRO_MSG)
    # Chat loop
    while True:
        user_message = input("You: ")
        if user_message == "exit":
            break
        response = chatbot.add_user_message(user_message)
        print("Bot:", response)
    print(OUTRO_MSG)


if __name__ == "__main__":
    main()
