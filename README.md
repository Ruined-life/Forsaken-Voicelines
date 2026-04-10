# Forsaken Voicelines

## Overview
This is a script that will bring the survivors to life. Adding voicelines for specific actions.

NOTE:
The voicelines I used are from people I found on youtube so all credits go to them (you can look at each person in the CREDITS file)

RECOMMEND VOLUME TO PLAY AT

<img src="volume.png" width="300">

---

## Features
Voice lines upon ability activation
Idle voice lines

TO BE ADDED
Damage sounds

---

## Project Structure
```md
src -> main logic
gui -> displays gui and grabs character
audio -> houses all the voicelines for each character
CREDITS -> the owners of the voicelines
requirements -> packages needed to run the program
```
---

## Requirements
```md
Python 3.12
```
---

## Build Instructions
```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
sudo apt install tesseract-ocr python3-gi
```

### Clone the repository
```bash
git clone <https://github.com/Ruined-life/Veeronica-Voicelines.git>
cd Forsaken-Voicelines
