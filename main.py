import whisper  # noqa: D100
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

import config


def transcribe_audio(audio_file: str) -> str:
    """Transcribe the audio file using Whisper ASR model.

    Args:
        audio_file (str): Path to the audio file.

    Returns:
        str: The transcribed text.
    """
    print("Loading Whisper ASR model...")
    model = whisper.load_model("base")
    print("Transcribing audio...")
    result = model.transcribe(audio_file)
    return result["text"]

if __name__ == "__main__":
    audio_file = config.AUDIO_FILEPATH

    transcript = transcribe_audio(audio_file)
    print("\nTranscript:\n", transcript)

    llm = OllamaLLM(model=config.LLM_MODEL)

    SUMMARIZER_TEMPLATE = """
    You have to summarize and extract action points of the following transcript:
    {transcript}

    Some background information:
    {background_info}
    """

    prompt = ChatPromptTemplate.from_template(SUMMARIZER_TEMPLATE)

    summary_chain = prompt | llm | StrOutputParser()
    background_info = config.BACKGROUND_INFO
    print("Elaborating the transcript...")
    result = summary_chain.invoke({"transcript": transcript, "background_info": background_info})
    print(f"AI BOT reply:\n {result}")

