from pathlib import Path
import json
from datetime import datetime

NOTES_DIR = Path('data')
NOTES_FILE = NOTES_DIR / 'notes.json'


def ensure_notes_file():
    NOTES_DIR.mkdir(exist_ok=True)

    if not NOTES_FILE.exists():
        with NOTES_FILE.open ('w', encoding='utf-8') as f:
            f.write ('[]')


def load_notes():
    with NOTES_FILE.open ('r', encoding='utf-8') as f:
        return json.load(f)

def save_notes(notes):
    with NOTES_FILE.open ('w', encoding='utf-8') as f:
        json.dump (notes, f, indent =2)


def add_note(text):
    notes = load_notes()

    note = {
        "id":len(notes) + 1,
        "text": text,
        "created": datetime.now().isoformat(timespec="seconds")
    }

    notes.append(note)
    save_notes(notes)

def list_notes():
    notes = load_notes()
    for note in notes:
        print (f"{note['id']}: {note['text']} {note['created']}\n")

if __name__ == '__main__':
    ensure_notes_file()

    while True:
        command = input ('add / list / quit: ').strip().lower()


        if command == "add":
                text = input("Note text: ")
                add_note(text)

        elif command == "list":
                list_notes()

        elif command == "quit":
                break
