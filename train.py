import speech_recognition as sr
import language_tool_python
import os

def speech_to_text(audio_path):
    r = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = r.record(source)
    return r.recognize_google(audio)

def grammar_score(text):
    tool = language_tool_python.LanguageToolPublicAPI('en-US')
    matches = tool.check(text)
    errors = len(matches)
    words = len(text.split())
    score = max(0, 100 - (errors * 10))
    return score, errors, words

def process_audio(audio_path):
    if not os.path.exists(audio_path):
        raise FileNotFoundError("Audio file not found")

    text = speech_to_text(audio_path)
    score, errors, words = grammar_score(text)

    return {
        "text": text,
        "words": words,
        "errors": errors,
        "score": score
    }
