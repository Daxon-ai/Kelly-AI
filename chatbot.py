from instagrapi import Client
from transformers import pipeline
import time

# CONFIG
USERNAME = "Kellyai2026"
PASSWORD = "kel254"
AUTO_BIO = "This is Kelly AI created by @eliud_lesta 😎"
GROUP_ID = "your_group_thread_id"

cl = Client()
cl.login(USERNAME, PASSWORD)
cl.account_set_bio(AUTO_BIO)

chatbot = pipeline('text-generation', model='gpt2')

def ai_reply(text):
    reply = chatbot(text, max_length=50)[0]['generated_text']
    return reply

def auto_reply():
    dms = cl.direct_threads(selected_filter="unread")
    for dm in dms:
        cl.direct_mark_seen(dm['thread_id'])
        msg = dm['last_seen_at'][0]['item']['text']
        reply = ai_reply(msg)
        cl.direct_answer(dm['thread_id'], reply)
        print(f"AI replied to {dm['users'][0]['username']}")

def auto_approve_group():
    pending = cl.direct_pending_inbox()
    for req in pending:
        cl.direct_approve(req['thread_id'])
        print(f"Approved join: {req['thread_title']}")

def group_management():
    # Auto-react, auto-typing, etc. (add logic)
    cl.direct_react(GROUP_ID, "❤️")
    cl.direct_indicator_send(GROUP_ID, "typing")

while True:
    auto_reply()
    auto_approve_group()
    group_management()
    time.sleep(60)
