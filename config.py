"""Configuration file for setting up the environment and parameters for audio processing and language modeling tasks.

- AUDIO_FILEPATH (str): The relative path to the audio file that will be processed.
- LLM_MODEL (str): The language model to be used for analyzing or generating text based on the input.
- BACKGROUND_INFO (str): Relevant background information that provides context for the task.
"""

AUDIO_FILEPATH: str = "./example/EarningsCall.wav"
LLM_MODEL: str = "llama3"
BACKGROUND_INFO: str = ""
