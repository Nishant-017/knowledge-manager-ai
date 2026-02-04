import json
import os

DATA_FILE = "data/notes.json"


def load_notes():
    """Load all notes from JSON file"""
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_notes(notes):
    """Save all notes to JSON file"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(notes, f, indent=4, ensure_ascii=False)


def add_note(original_text, summary, tags):
    notes = load_notes()

    if notes:
        new_id = max(note["id"] for note in notes) + 1
    else:
        new_id = 1

    note = {
        "id": new_id,
        "original_text": original_text,
        "summary": summary,
        "tags": tags,
    }

    notes.append(note)
    save_notes(notes)



def update_note(index, original_text, summary, tags):
    notes = load_notes()

    if index < 0 or index >= len(notes):
        return False

    notes[index]["original_text"] = original_text
    notes[index]["summary"] = summary
    notes[index]["tags"] = tags

    save_notes(notes)
    return True



def delete_note(index):
    notes = load_notes()

    if index < 0 or index >= len(notes):
        return False

    notes.pop(index)
    save_notes(notes)
    return True
