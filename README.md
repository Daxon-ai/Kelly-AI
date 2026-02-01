
# Kelly AI
by Eliud_Lesta

A simple AI chatbot with IG features.

![Followers](https://img.shields.io/github/followers/Daxon-ai?style=social)
![Forks](https://img.shields.io/github/forks/Daxon-ai/Kelly-AI?style=social)
![Last Commit](https://img.shields.io/github/last-commit/Daxon-ai/Kelly-AI)

## About
Kelly AI manages IG profiles.

## Termux Setup
1. `pkg update && pkg upgrade`
2. `pkg install git python`
3. `git clone https://github.com/Eliud_Lesta/Kelly-AI.git`
4. `cd Kelly-AI`
5. `python -m venv env`
6. `source env/bin/activate`
7. `pip install -r requirements.txt`
8. Set IG_PASSWORD in env (e.g., `export IG_PASSWORD='your_pw'`)

## Run
```bash
python chatbot.py


## Termux Steps
1. `pkg update && pkg upgrade`
2. `pkg install git python`
3. `git clone https://github.com/Eliud_Lesta/Kelly-AI.git`
4. `cd Kelly-AI`
5. `python -m venv env`
6. `source env/bin/activate`
7. `pip install -r requirements.txt`
8. `export IG_PASSWORD='your_ig_password'`
9. `python chatbot.py`
10. Test: "show ig profile", "update ig bio"
11. `git add .`, `git commit`, `git push
