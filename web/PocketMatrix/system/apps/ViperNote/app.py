# ViperNote App
# Authentication Phrase: "what eats to live but never drinks"
import os
import time

def save_note(note_content, auth_phrase):
    if auth_phrase != "what eats to live but never drinks":
        return "Auth Failed"

    note_dir = "/data/data/com.termux/files/home/KAI_9000/WEB_UI/notes_ce"
    os.makedirs(note_dir, exist_ok=True)
    filename = f"note_{int(time.time())}.md"
    with open(os.path.join(note_dir, filename), 'w') as f:
        f.write(note_content)
    return "Note Saved"
