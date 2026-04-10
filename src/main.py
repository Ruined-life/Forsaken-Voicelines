import random, time, os, subprocess, threading, numpy as np
import pyautogui, pytesseract, sounddevice as sd
from scipy.io import wavfile
from pathlib import Path
from pynput import keyboard


# TO-DO:
#Later down the line other features i can add:
#1) Death sounds (by just checking if the health from the OCR is 0)

#HIGH PRIORITY
    #CHECK IF THE PLAYER IS TABBED INTO ROBLOX BEFORE PLAYING A SOUND
    #COMMIT WHEN YOU GET A MVP RUNNING (HIGH PRIORITY)
    #READ CURRENT CHARACTER DONE
    #GET GUI WORKING AGAIN DONE
    #ADD TAPHS VOICELINES
    #FIX THE bug WHERE CHANGING CHARACTERS STILL USES REQUESTS USING YOUR PREVIOUS CHARACTER
    #IN THE GUI LET THE USER TOGGLE ON KEY LISTENING SO THEY CAN TYPE AS NORMAL WHILE THE SCRIPT IS RUNNING
    #MAKE SURE TO VALIDATE THE USERS CHARACTER BEFORE TRYING TO PLAY A SOUND FOR A CHARACTER. 
    #(otherwise you might play a pizza throw sound for two time which causes an error)

#Change folder categories in veeronica audio to match correctly (Damaged, Action, Abilities, Idle, Request) DONE
#Increase volume on all files so its clearer (temp fix unless i implement a standard way to play them) DONE
#Change veeronicas audio formats from mp3 to wav DONE
#Add folders for each characters abilities so they can be played DONE

current_character = None

previous_health = None
last_keypress_time = time.time()  # replaces key_timer entirely
idle_delay = 30               # 60 seconds of no input → idle sound

BASE_DIR = Path(__file__).resolve().parent.parent
AUDIO_DIR = BASE_DIR / "src" / "audio"

#print("AUDIO DIRECTORY: ", AUDIO_DIR)
print("BASE DIRECTORY: ", BASE_DIR)

# -----------------------------
# GUI
# -----------------------------
def run_gui():
    subprocess.run(["python3", "gui.py"], cwd=BASE_DIR / "src")


# -----------------------------
# Get Current Character
# -----------------------------
def get_character():
    TARGET_FILE = BASE_DIR / "src" / "Character.txt"
    with open(TARGET_FILE, "r") as file:
        return file.read().strip()
        

# -----------------------------
# Get Sound Files
# -----------------------------
audio_files = []
def get_audio_files(character, mode, ability=None):
    audio_files.clear()
   
    if ability is None:
        TARGET_DIR = AUDIO_DIR / character / mode
    else:
        TARGET_DIR = AUDIO_DIR / character / mode / ability

    if not TARGET_DIR.exists():
        print("Invalid path:", TARGET_DIR)
        return

    for file in TARGET_DIR.iterdir():
        print(file.name)
        audio_files.append(file)

    
def play(mode, ability=None):
    get_audio_files(current_character, mode, ability)

    #probably check here if audio_files is empty so you dont try to play something from an empty list
    if not audio_files:
        print("LIST IS EMPY! NOT PLAYING ANY SOUND!")
        return
    else:
        rand_file = random.choice(audio_files)
        fs, data = wavfile.read(rand_file)

        # 1. Ensure float processing
        data = data.astype(np.float32)

        # 2. Peak normalization
        peak = np.max(np.abs(data))
        if peak > 0:
            data /= peak

        # 3. Gain (safe headroom)
        data *= 0.9

        # 4. Play
        sd.stop()
        sd.play(data, fs, blocking=True)
        

    
def audio_player(character, mode, key=None):
    global current_character
    current_character = get_character()
    print("DEBUG character:", repr(character))
    print("DEBUG key:", repr(key))

    match character:
        case "Noob":
            if mode == "Damaged":
                print("You been damaged!")
                play("Damaged")
            elif mode == "Idle":
                print("You are idle!")
                play("Idle")
            elif mode == "Abilities":
                if key == "q":
                    print("You activated bloxy cola!")
                    play("Abilities", "Cola")
                elif key == "e":
                    print("You activated slateskin!")
                    play("Abilities", "Slateskin")
                elif key == "r":
                    print("You activated ghost burger!")
                    play("Abilities", "Ghost Burger")


        case "Shedletsky":
            if mode == "Damaged":
                print("You been damaged!")
                play("Damaged")
            elif mode == "Idle":
                print("You are idle!")
                play("Idle")
            elif mode == "Abilities":
                if key == "q":
                    print("You activated sword slash!")
                    play("Abilities", "Sword")
                elif key == "e":
                    print("You activated chicken!")
                    play("Abilities", "Chicken")
                

        case "Elliot":
            if mode == "Damaged":
                print("You been damaged!")
                play("Damaged")
            elif mode == "Idle":
                print("You are idle!")
                play("Idle")
            elif mode == "Abilities":
                if key == "q":
                    print("You activated pizza throw!")
                    play("Abilities", "Pizza")
                elif key == "e":
                    print("You activated rush hour!")
                    play("Abilities", "Rush Hour")
                

        case "Jane Doe":
            if mode == "Damaged":
                print("You been damaged!")
                play("Damaged")
            elif mode == "Idle":
                print("You are idle!")
                play("Idle")
            elif mode == "Abilities":
                if key == "q":
                    print("You activated crystal pitch!")
                    play("Abilities", "")
                elif key == "e":
                    print("You activated hatchet!")
                    play("Abilities")
                    
                

        case "Builderman":
            if mode == "Damaged":
                print("You been damaged!")
                play("Damaged")
            elif mode == "Idle":
                print("You are idle!")
                play("Idle")
            elif mode == "Abilities":
                if key == "q":
                    print("You activated sentry!")
                    play("Abilities", "Sentry")
                elif key == "e":
                    print("You activated dispenser!")
                    play("Abilities", "Dispenser")

        
        case "007n7":
            if mode == "Damaged":
                print("You been damaged!")
                play("Damaged")
            elif mode == "Idle":
                print("You are idle!")
                play("Idle")
            elif mode == "Abilities":
                if key == "q":
                    print("You activated clone!")
                    play("Abilities", "Clone")
                elif key == "e":
                    print("You activated coolgui")
                    play("Abilities", "Coolgui")
                elif key == "r":
                    print("You activated ghost inject")
                    play("Abilities", "Inject")


        case "Two Time":
            if mode == "Damaged":
                print("You been damaged!")
                play("Damaged")
            elif mode == "Idle":
                print("You are idle!")
                play("Idle")
            elif mode == "Abilities":
                if key == "q":
                    print("You activated dagger!")
                    play("Abilities", "Dagger")
                elif key == "e":
                    print("You activated crouch!")
                    play("Abilities", "Crouch")
                elif key == "r":
                    print("You activated ritual")
                    play("Abilities", "Ritual")


        case "Guest":
            if mode == "Damaged":
                print("You been damaged!")
                play("Damaged")
            elif mode == "Idle":
                print("You are idle!")
                play("Idle")
            elif mode == "Abilities":
                if key == "q":
                    print("You activated block!")
                    play("Abilities", "Block")
                elif key == "e":
                    print("You activated charge")
                    play("Abilities", "Charge")
                elif key == "r":
                    print("You activated punch")
                    play("Abilities", "Punch")


        case "Taph":
            if mode == "Damaged":
                print("You been damaged!")
                play("Damaged")
            elif mode == "Idle":
                print("You are idle!")
                play("Idle")
            elif mode == "Abilities":
                if key == "q":
                    print("You activated tripwire!")
                    #TO BE IMPLEMENTED
                elif key == "e":
                    print("You activated subspace mine!")
                    #TO BE IMPLEMENTED


        case "Dusekkar":
            if mode == "Damaged":
                print("You been damaged!")
                play("Damaged")
            elif mode == "Idle":
                print("You are idle!")
                play("Idle")
            elif mode == "Abilities":
                if key == "q":
                    print("You activated spawn protection!")
                    play("Abilities", "Shield")
                elif key == "e":
                    print("You activated plasma beam!")
                    play("Abilities", "Plasma Beam")


        case "Veeronica":
            if mode == "Damaged":
                print("You been damaged!")
                play("Damaged")
            elif mode == "Idle":
                print("You are idle!")
                play("Idle")
            elif mode == "Abilities":
                if key == "q":
                    print("You activated vandalism!")
                    play("Abilities", "Graffiti")
                elif key == "e" or key == " ":
                    print("You activated skate!")
                    play("Abilities", "Skate")
                elif key == "t":
                    print("You activated battery!")
                    play("Abilities", "Battery")


        case "Chance":
            if mode == "Damaged":
                print("You been damaged!")
                play("Damaged")
            elif mode == "Idle":
                print("You are idle!")
                play("Idle")
            elif mode == "Abilities":
                if key == "q":
                    print("You activated coin flip")
                    play("Abilities")
                elif key == "e":
                    print("You activated shoot!")
                    play("Abilities")
                elif key == "r":
                    print("You activated reroll!")
                    play("Abilities")
                elif key == "t":
                    print("You activated hat fix!")
                    play("Abilities")
               
                




# -----------------------------
# OCR Health Scanner
# -----------------------------
# def screenshot_health():
#     region = (437, 911, 90, 26)
#     screenshot = pyautogui.screenshot(region=region)

#     text = pytesseract.image_to_string(
#         screenshot,
#         config="--psm 7 -c tessedit_char_whitelist=0123456789"
#     ).strip()

#     try:
#         return int(text)
#     except ValueError:
#         return None


# -----------------------------
# Keypress listener
# -----------------------------
pressed_keys = set()
def on_press(key):
    try:
        if key.char in pressed_keys:
            return  # ignore repeats

        pressed_keys.add(key.char)

        if key == keyboard.Key.space:
            print("space pressed")
            audio_player(current_character, "Abilities", key.char)
            

        elif key.char == "q":
            print("q pressed")
            audio_player(current_character, "Abilities", key.char)
            

        elif key.char == "e":
            print("e pressed")
            audio_player(current_character, "Abilities", key.char)

        
        elif key.char == "r":
            print("r pressed")
            audio_player(current_character, "Abilities", key.char)
            
        
        elif key.char == "t":
            print("t pressed")
            audio_player(current_character, "Abilities", key.char)

    except AttributeError:
        pass


def on_release(key):
    try:
        pressed_keys.discard(key.char)
    except AttributeError:
        pass


# -----------------------------
# Main Loop
# -----------------------------
listener = keyboard.Listener(on_press=on_press, on_release=on_release) 
listener.daemon = True 
listener.start()

def main():
    global last_keypress_time
    while True:
        # ---------------------
        # Idle sound system
        # --------------------- 
        if time.time() - last_keypress_time >= idle_delay and current_character != None: 
            print("Idle timeout reached → playing idle sound") 
            audio_player(current_character, "Idle") 
            #Reset timer so it doesn't loop spam idle 
            last_keypress_time = time.time() 
            time.sleep(1)
        

if __name__ == "__main__":
    gui_thread = threading.Thread(target=run_gui) 
    gui_thread.start()
    main()
    


# while True:
#     pass

    # ---------------------
    # Health scanning
    # ---------------------
    # current_health = screenshot_health()

    # if current_health is not None:
    #     print("Current health:", current_health)

    #     # First-time setup for previous health
    #     if previous_health is None:
    #         previous_health = current_health

    #     else:
    #         # Damage detection with threshold
    #         if current_health < previous_health:
    #             difference = previous_health - current_health

    #             if difference >= 5:  # threshold can be tuned
    #                 print(f"Health decreased by {difference}!")
                    
    #             else:  
    #                 print(f"Health decreased by {difference}!")  
                    

    #         previous_health = current_health

    # else:
    #     print("OCR failed this frame.")

    # time.sleep(1.0)  # smoother + less CPU




