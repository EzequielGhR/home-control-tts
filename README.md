# home-control-tts
Some files for home control automation using tts for google home

# How to
The instructions assumes you're using Linux sorry about that but Ubuntu is my sauce.

- Create a directory for your files for example `mkdir ~/.home_control`
- Put `home_control.sh` and `tts_scripts` in said directory. In my case `cp -t ~/.home_control home_control.sh tts_script.py`
- You'll need to install some things:
    - pyaudio: `sudo apt install python3-pyaudio`
    - espeak: `sudo apt install espeak`
    - espeak-ng: `sudo apt install espeak-ng`
    - mbrola: sudo `apt-get install mbrola`
    - mbrola voices: `sudo apt install mbrola-*`
- python requirements:
    I suggest using the env provided `.hcenv` with `source .hcenv/bin/activate`, but if you want to use your own you should be able as follows:
    - `python -m venv .hcenv`
    - `source {your_env_name}/bin/activate`
    - `pip install pyttsx==2.91 deep-translator==1.11.4`
    - If you get issues with setProperty on pyttsx3 you should install form source:
        - clone the source repo: `git clone https://github.com/nateshmbhat/pyttsx3.git`
        - Execute setup.py: `python setup.py install`
- Add execution permissions to main sheel script. In my case `chmod +x ~/.home_control/home_control.sh`
- Add the command to load the scripts to Run Control (`.profile` or `.bashrc`):
    - Open your rc file, in my case I'll use nano: `nano ~/.bashrc`
    - Add the line at the end to load your scripts. In my case: `source ~/.home_control/home_control.sh`
    - Save and close. In nano Ctrl+S and then Ctrl+X.
    - Reload session `source ~/.bashrc`
- You should be able to run the commands (functions inside home_control.sh)

# Commands
Documentation in progress lol. But some examples:
- `hc-lights`:
    - `hc-lights -a -s on`: TTS to turn on all lights
    - `hc-lights -s off -i office`: TTS to turn off the office light
    - `hc-lights -s on -i out-bed`: TTS to turn on the out and bed lights
- `hc-lights-intensity`:
    Google home can't change color and intensity at the same time so this command will do 2 speeches, one for color and one for brightness
    - `hc-lights-intensity -i office-bed -v 50 -c red`: TTS to turn office and bed lights red with a brightness of 50%.
    - `hc-lights-intensity -a -v 90 -c blue`: TTS to turn all lights blue with a brightness of 90%.
- `hc-music`:
    - `hc-music`: TTS to play any music on youtube music (I don't use spotify but maybe I can implement it later)
    - `hc-music -b "Frank Sinatra"`: TTS to play music from Frank Sinatra
    - `hc-music -s "Killer Whales"`: TTS to play the song killer whales (probably will find small pools' one)
    - `hc-music -s "Into your arms" -b "The maine"`: TTS to play Into your arms by The Maine.
    - `hc-music -s "vienes y te vas" -b "La base" -l es`: TTS to play vienes y te vas by la base. The flag -l is the speech language, since this son is in spanish makes sense to ask in spanish, hence the "es" arg.


