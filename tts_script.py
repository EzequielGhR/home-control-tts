import pyttsx3
import argparse

from time import sleep
from deep_translator import GoogleTranslator as GT

def turn_on_off(status:str, engine:pyttsx3.Engine, ids:list, all_:bool=True) -> None:
    """
    Turns lights on or off.
        status: "on" | "off"
        engine: pyttsx3 engine,
        ids: ["out", "office", "bed"] depends on your identifiers
        all_: if True, override identifiers to turn all the lights on
    """
    if status not in ("on", "off"):
        engine.say(f"Invalid status: {status}")
    else:
        engine.say("Hey Google!")
        sleep(1)
        if all_:
            engine.say(f"Please turn {status} the lights")
        else:
            phrase = f"Please turn {status} the {ids.pop(0)} light"
            for id_ in ids:
                phrase = phrase.rsplit("light")[0]
                phrase += f"and the {id_} lights"
            engine.say(phrase)
        engine.runAndWait()

def change_intensity(color:str, value:int, ids:list, engine:pyttsx3.Engine, all_:bool=True) -> None:
    """
    changes lights intensity/brightness and color.
        color: "blue"|"red"|"pink" etc
        value: brightness as a percentage
        ids: ["out", "office", "bed"] depends on your identifiers
        all_: if True, override identifiers to apply changes on all lights

    """
    if value not in range(1, 101):
        engine.say(f"Invalid intensity percentage: {value}")
        engine.runAndWait()
        exit(1)
    
    for i, (k, v) in enumerate({"color": color, "brightness": str(value)+"%"}.items()):
        engine.say("Hey Google!")
        sleep(1)

        if all_:
            engine.say(f"Please set the lights {k} to {v}")

        else:
            phrase = f"Please set the {ids[0]} light"
            for id_ in ids[1:]:
                phrase = phrase.rsplit(" light")[0]
                phrase+=f", and the {id_} lights"
            phrase += f"{k} to {v}"
            engine.say(phrase)
        engine.runAndWait()

        if not i:
            sleep(7)

def play_music(song:str, band:str, lamg:str, engine:pyttsx3.Engine) -> None:
    engine.say("Hey Google!")
    sleep(1)

    phrase = "Can you play '{}', by '{}'"
    parts = ["some music?", "on 'YouTube Music'?", "music", "by"]
    if lang in (langs:=("en", "es", "pr", "fr")):
        engine.setProperty("voice", f"mb-{lang}1")
        phrase = GT(source="auto", target=lang).translate(phrase)
        translated = [
            GT(source="auto", target=lang).translate(part)
            for part in parts
        ]
        parts = translated
    else:
        print(f"language not provided or not in {langs}. Defaults to \"en\"")

    
    if (not song) and (not band):
        phrase = phrase.format("_split_", "")
        phrase = phrase.split("'_split_'")[0] + parts[0]
    elif song and band:
        phrase = phrase.format(song, band)
    elif song:
        phrase = phrase.format(song, "_split_")
        phrase = phrase.split(parts[3]+" '_split_'")[0] + parts[1]
    else:
        phrase = phrase.format("_", band).replace("'_'", parts[2])
        
    engine.say(phrase)
    engine.runAndWait()
        

def run(
    status:str,
    color:str,
    band:str,
    song:str,
    lang:str,
    value:int=100,
    identifier:str="",
    all_:bool=True
) -> None:
    
    ids = identifier.split('-')
    engine = pyttsx3.init()

    engine.setProperty("voice", "mb-en1")
    engine.setProperty("rate", 100)
    engine.setProperty("pitch", 30)
    engine.setProperty("volume", 2)

    if status:
        turn_on_off(status, engine, ids, all_)
    elif color:
        change_intensity(color, value, ids, engine, all_)
    else:
        play_music(song, band, lang, engine)

    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--all", type=str, help="all lights")
    parser.add_argument("--status", type=str, help="on or off")
    parser.add_argument("--identifier", type=str, help="specific lights hyphen separated")
    parser.add_argument("--value", type=str, help="light intensity percentage")
    parser.add_argument("--color", type=str, help="color of the light")
    parser.add_argument("--band", type=str, help="musical band")
    parser.add_argument("--song", type=str, help="song to search")
    parser.add_argument("--language", type=str, help="language for tts [en, es, fr, pr]")

    args = parser.parse_args()

    color = args.color
    band = args.band
    song = args.song
    identifier = args.identifier or ""
    lang = args.language or ""
    all_ = eval(args.all.lower().capitalize()) if args.all else False
    status = args.status.lower() if args.status else ""
    value = int(args.value) if args.value else None

    run(
        status=status,
        color=color,
        band=band,
        song=song,
        lang=lang,
        value=value,
        identifier=identifier,
        all_=all_
    )