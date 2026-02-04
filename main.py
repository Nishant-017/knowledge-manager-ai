from agent import generate_summary, generate_tags, heavy_model
from storage import add_note, load_notes

chat_history = []  # to maintain conversation context

def show_menu():
    print("\n--- AI Knowledge Manager ---")
    print("add  - Add new knowledge")
    print("list - Show saved knowledge")
    print("ask  - Ask a question")
    print("search - Search by keyword")
    print("edit - update a document")
    print("delete - delete a document")
    print("exit - Quit")


def add_knowledge():
    print("\nPaste your knowledge (type END on a new line when finished):")

    lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)

    text = "\n".join(lines)

    print("\nAI is summarizing...")
    summary = generate_summary(text)

    print("AI is generating tags...")
    tags = generate_tags(text)

    add_note(text, summary, tags)

    print("\nSaved successfully!")
    print("Summary:", summary)
    print("Tags:", tags)


def list_knowledge():
    notes = load_notes()

    if not notes:
        print("\nNo knowledge saved yet.")
        return

    print("\n--- Saved Knowledge ---")
    for i, note in enumerate(notes, 1):
        print(f"ID {note['id']} - {note['summary']} | Tags: {', '.join(note['tags'])}")




def ask_question():
    global chat_history

    notes = load_notes()

    if not notes:
        print("\nNo knowledge available to ask from.")
        return

    # Combine notes 
    all_notes_text = ""

    for note in notes:
        all_notes_text += f"- {note['original_text']}\n"

    question = input("\nAsk your question:\n")

    # Add user message to history
    chat_history.append(f"User: {question}")

    # Keep only last 6 messages (3 turns)
    chat_history = chat_history[-6:]

    history_text = "\n".join(chat_history)

    prompt = f"""
You are an AI knowledge assistant.

Use ONLY the knowledge notes and the conversation history to answer.

If the answer is not in the notes, say:
"I don't have enough information in the saved knowledge."

Conversation History:
{history_text}

Knowledge Notes:
{all_notes_text}

Now carefully answer ALL parts of the latest user question.
If the question contains multiple parts, answer each part separately.

Question: {question}

Answer:
"""


    print("\nAI is thinking...")
    answer = heavy_model.run(prompt)

    # Add AI response to history
    chat_history.append(f"AI: {answer}")

    print("\nAnswer:")
    print(answer)

    # print(history_text)


def search_knowledge():
    notes = load_notes()

    if not notes:
        print("\nNo knowledge saved yet.")
        return

    keyword = input("\nEnter keyword to search: ").lower()

    found = False

    print("\n--- Search Results ---")

    for i, note in enumerate(notes, 1):
        combined_text = (
            note["original_text"] +
            " " +
            note["summary"] +
            " " +
            " ".join(note["tags"])
        ).lower()

        if keyword in combined_text:
            print(f"ID {note['id']} - {note['summary']} | Tags: {', '.join(note['tags'])}")
            found = True

    if not found:
        print("No matching knowledge found.")

def show_notes():
    notes = load_notes()

    if not notes:
        print("\nNo knowledge saved yet.")
        return None

    print("\n--- Knowledge List ---")
    for i, note in enumerate(notes, 1):
        print(f"{i}. {note['summary']} | Tags: {', '.join(note['tags'])}")

    return notes


def edit_knowledge():
    notes = show_notes()

    if not notes:
        return

    try:
        note_id = int(input("Enter note ID to edit: "))
        choice = next((i for i, n in enumerate(notes) if n["id"] == note_id), None)
        if choice is None:
            print("Invalid ID.")
            return
    except ValueError:
        print("Invalid input.")
        return

    if choice < 0 or choice >= len(notes):
        print("Invalid number.")
        return

    new_text = input("\nEnter new knowledge text:\n")

    print("\nAI is summarizing...")
    summary = generate_summary(new_text)

    print("AI is generating tags...")
    tags = generate_tags(new_text)

    from storage import update_note
    success = update_note(choice, new_text, summary, tags)

    if success:
        print("\nUpdated successfully!")
    else:
        print("\nFailed to update.")


def delete_knowledge():
    notes = show_notes()

    if not notes:
        return

    try:
        note_id = int(input("Enter note ID to delete: "))
        choice = next((i for i, n in enumerate(notes) if n["id"] == note_id), None)
        if choice is None:
            print("Invalid ID.")
            return

    except ValueError:
        print("Invalid input.")
        return

    from storage import delete_note
    success = delete_note(choice)

    if success:
        print("\nDeleted successfully!")
    else:
        print("\nFailed to delete.")




def main():
    while True:
        show_menu()
        choice = input("\nEnter command: ").strip().lower()

        if choice == "add":
            add_knowledge()
        elif choice == "list":
            list_knowledge()
        elif choice == "ask":
            ask_question()
        elif choice == "search":
            search_knowledge()
        elif choice == "edit":
            edit_knowledge()
        elif choice == "delete":
            delete_knowledge()
        elif choice == "exit":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid command. Try again.")

if __name__ == "__main__":
    main()
