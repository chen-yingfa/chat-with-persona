"""
ChatGPT augmented with persona estimation.
"""
import openai
from pathlib import Path


class Chatbot:
    """
    A wrapper around ChatGPT that infers the persona of the user on every
    message.
    """

    def __init__(
        self,
        api: str,
        cache_path: Path = Path("cache/temp"),
        do_infer_persona: bool = True,
    ):
        '''
        Args:
            api: The OpenAI API key.
            cache_path: The path to the cache directory, which stores states
                such as chat history, persona etc.
            do_infer_persona: Whether to infer the persona of the user during chat.
        '''
        # Sanity checks
        assert isinstance(api, str), "API key must be a string."
        assert len(api) > 0, "API key must not be empty."

        self.api = api
        self.output_path = cache_path
        self.do_infer_persona = do_infer_persona

        openai.api_key = api  # Set the API key

        self.chat_history: list[dict[str, str]] = []
        self.user_persona: list[str] = []

    def infer_persona(self, chat_history: list[str]) -> list[str]:
        """
        Infer the persona of the user from the chat history of the conversation.
        The last message of the history must be from the user.
        """
        # Just prompt ChatGPT with few-shot examples
        ...

        raise NotImplementedError

    def add_user_message(self, msg: str) -> str:
        """
        Add a message from the user to the chat history. Perform persona
        inference, and respond to the user.

        chat_history: [
            {"role": "user", "content": "..."},
            {"role": "assistant", "content": "..."},
            {"role": "user", "content": "..."},
        ]

        Args:
            msg (str): The user message.
        """
        # Infer persona
        ...

        # Save persona
        ...

        # Make the chat request, but augment the prompt with the persona
        ...

        # Save chat history
        ...

        raise NotImplementedError

    def save_states(self):
        '''Save states to the cache directory.'''
        raise NotImplementedError
