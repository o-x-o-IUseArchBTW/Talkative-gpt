import json
import os
from time import sleep
from openai import OpenAI


# =========================
# Configuration
# =========================

MODEL = "gpt-5-nano"

INST_DIR = "inst"
CHAT_DIR = "chat"
OpenAI.API_KEY = "YOUR_KEY_HERE"
os.makedirs(INST_DIR, exist_ok=True)
os.makedirs(CHAT_DIR, exist_ok=True)


# =========================
# Helpers
# =========================

def safe_name(name):
    """Prevent paths from being entered as the name."""
    return "".join(c for c in name if c.isalnum() or c in ("-", "_"))


def load_instructions(name):
    name = safe_name(name)
    path = os.path.join(INST_DIR, f"{name}.json")

    if not os.path.exists(path):
        instructions = input(
            f'Instructions file "{path}" does not exist.\n'
            "Enter instructions to create >>>: "
        )

        data = {
            "name": name,
            "instructions": instructions
        }

        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        print(f"Created {path}")
        return instructions

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data.get("instructions", "")


def load_chat(name):
    name = safe_name(name)
    path = os.path.join(CHAT_DIR, f"{name}.json")

    if not os.path.exists(path):
        data = {
            "name": name,
            "messages": []
        }

        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        return data

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_chat(name, chat_data):
    name = safe_name(name)
    path = os.path.join(CHAT_DIR, f"{name}.json")

    with open(path, "w", encoding="utf-8") as f:
        json.dump(chat_data, f, indent=4, ensure_ascii=False)


def add_message(name, chat_data, role, content):
    chat_data["messages"].append({
        "role": role,
        "content": content
    })

    save_chat(name, chat_data)


# =========================
# OpenAI
# =========================

client = OpenAI()


# =========================
# Select files
# =========================
chat_name = input("chat >>>: ")
inst_name = input("instructions >>>: ")

instructions = load_instructions(inst_name)
chat_data = load_chat(chat_name)

print()
print(f"Instructions: inst/{safe_name(inst_name)}.json")
print(f"Memory:       chat/{safe_name(chat_name)}.json")
print()


# =========================
# Chat loop
# =========================

while True:

    prompt = input("prompt >>>: ")

    if prompt.lower() in ("exit", "quit"):
        break

    # Save user message
    add_message(
        chat_name,
        chat_data,
        "user",
        prompt
    )

    # Send entire saved conversation as input
    response = client.responses.create(
        model=MODEL,
        instructions=instructions,
        input=chat_data["messages"]
    )

    answer = response.output_text

    print()
    print(answer)
    print()

    # Save assistant response
    add_message(
        chat_name,
        chat_data,
        "assistant",
        answer
    )

    sleep(1)