import pyttsx3
import argparse

from deep_translator import GoogleTranslator

engine = pyttsx3.init()
engine.setProperty("rate", 100)
engine.setProperty("pitch", 30)
engine.setProperty("volume", 2)

langs = ["en", "es", "pt", "de", "fr"]

def translate(text:str, lang:str, source:str="auto") -> str:
    return GoogleTranslator(source=source, target=lang).translate(text)

def from_text(text:str, lang:str, source:str="auto", tts:bool=True) -> None:
    translated = translate(text, lang, source)
    print("T > "+translated)
    if tts:
        engine.setProperty("voice", f"mb-{lang}1")
        engine.say(translated)
        engine.runAndWait()

def from_voice() -> None:
    print("NYI")

def run(text:str, lang:str, source:str="auto", tts:bool=True, audio:bool=False) -> None:
    if (lang not in langs):
        print(f"'{lang}' not in {langs}, but will try to translate text only")
        tts = False
    if (source not in langs) and (source!="auto"):
        print(f"source '{source}' not in {langs}. Will be preset to 'auto'")
        source = "auto"
    
    if audio:
        return from_voice()
    
    print("Y > "+text)
    print(f"Y > translate to '{lang}' from '{source}'")
    return from_text(text, lang, source, tts)

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", type=str, help="Text to be translated")
    parser.add_argument("--language", type=str, help="Target translation language")
    parser.add_argument("--source", type=str, help="source language from which to translate")
    parser.add_argument("--tts", type=str, help="Bool stating if text to speech respond should be used")
    parser.add_argument("--audio", type=str, help="Indicator for audio input")

    args = parser.parse_args()

    text = args.text
    language = args.language
    source = args.source or "auto"
    tts = eval(args.tts.lower().capitalize())
    audio = eval(args.audio.lower().capitalize())

    run(text, language, source, tts, audio)

    