
import nltk
from nltk.stem import WordNetLemmatizer
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
import random
import instaloader
import os

nltk.download('punkt')
nltk.download('wordnet')

intents = {
    'greetings': ['hi', 'hello', 'hey'],
    'goodbye': ['bye', 'see you', 'goodbye'],
    'ig_profile': ['show ig profile', 'ig data'],
    'ig_bio': ['update ig bio', 'change bio'],
}

lemmatizer = WordNetLemmatizer()
# ... (rest of chatbot code)

def get_ig_profile(username):
    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(L.context, username)
    return f"IG: {profile.full_name}, Followers: {profile.followers}, Following: {profile.following}"

def update_ig_bio(username, new_bio):
    L = instaloader.Instaloader()
    L.login(username, os.getenv('IG_PASSWORD')) # need IG creds
    profile = instaloader.Profile.from_username(L.context, username)
    profile.set_biography(new_bio)
    return f"Bio updated to: {new_bio}"

# ...
print("Kelly AI running. Type 'quit' to exit.")
while True:
    msg = input("You: ")
    if msg.lower() == 'quit':
        break
    intent = get_response(msg)
    if intent == 'ig_profile':
        print(f"Kelly AI: {get_ig_profile('your_ig_username')}")
    elif intent == 'ig_bio':
        new_bio = input("Enter new bio: ")
        print(f"Kelly AI: {update_ig_bio('your_ig_username', new_bio)}")
    else:
        print(f"Kelly AI: {intent}")


