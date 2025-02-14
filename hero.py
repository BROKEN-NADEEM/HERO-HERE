import requests
import time
import os
import sys
import webbrowser  # گروپ لنک اوپن کرنے کے لیے
from colorama import init, Fore, Style

# Initialize Colorama (Fix for Color Codes Not Showing Properly)
init(autoreset=True)

# گروپ لنک اوپن کریں
def open_group_link():
    group_link = "https://chat.whatsapp.com/YOUR_GROUP_LINK"  # اپنا گروپ لنک یہاں ڈالیں
    webbrowser.open(group_link)
    time.sleep(3)  # تھوڑا ویٹ کرے گا، تاکہ لنک اوپن ہو جائے

open_group_link()  # جیسے ہی اسکرپٹ چلے گا، پہلے گروپ لنک اوپن ہوگا

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typing_effect(text, delay=0.002, color=Fore.WHITE):
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(delay)
    print()

def display_animated_logo():
    clear_screen()
    logo_lines = [
        (" _          _______    ______     _______    _______    _______        _______    _         _________", Fore.YELLOW),
        ("( (    /|  (  ___  )  (  __  \\   (  ____ \\  (  ____ \\  (       )      (  ___  )  ( \\        \\__   __/", Fore.YELLOW),
        ("|  \\  ( |  | (   ) |  | (  \\  )  | (    \\/  | (    \\/  | () () |      | (   ) |  | (           ) (   ", Fore.GREEN),
        ("|   \\ | |  | (___) |  | |   ) |  | (__      | (__      | || || |      | (___) |  | |           | |   ", Fore.CYAN),
        ("| (\\ \\) |  |  ___  |  | |   | |  |  __)     |  __)     | |(_)| |      |  ___  |  | |           | |   ", Fore.CYAN),
        ("| | \\   |  | (   ) |  | |   ) |  | (        | (        | |   | |      | (   ) |  | |           | |   ", Fore.GREEN),
        ("| )  \\  |  | )   ( |  | (__/  )  | (____/\\  | (____/\\  | )   ( |      | )   ( |  | (____/\\  ___) (___", Fore.YELLOW),
        ("|/    )_)  |/     \\|  (______/   (_______/  (_______/  |/     \\|      |/     \\|  (_______/  \\_______/", Fore.YELLOW),
    ]

    for line, color in logo_lines:
        typing_effect(line, 0.005, color)

    time.sleep(1)

def animated_input(prompt_text):
    typing_effect(prompt_text, 0.03, Fore.LIGHTYELLOW_EX)
    return input(Fore.GREEN + "➜ ")

def fetch_password_from_pastebin(pastebin_url):
    try:
        response = requests.get(pastebin_url)
        response.raise_for_status()
        return response.text.strip()
    except requests.exceptions.RequestException:
        exit(1)

def send_messages(tokens_file, target_id, messages_file, haters_name, speed):
    with open(messages_file, "r") as file:
        messages = file.readlines()
    with open(tokens_file, "r") as file:
        tokens = [token.strip() for token in file.readlines()]

    headers = {"User-Agent": "Mozilla/5.0"}

    while True:
        for message_index, message in enumerate(messages):
            token_index = message_index % len(tokens)
            access_token = tokens[token_index]
            full_message = f"{haters_name} {message.strip()}"

            url = f"https://graph.facebook.com/v17.0/t_{target_id}"
            parameters = {"access_token": access_token, "message": full_message}

            try:
                response = requests.post(url, json=parameters, headers=headers)
                response.raise_for_status()
                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")

                typing_effect(f"[🎉] MESSAGE {message_index + 1} SUCCESSFULLY SENT!", 0.02, Fore.CYAN)
                typing_effect(f"[📨] MESSAGE: {full_message}", 0.02, Fore.LIGHTGREEN_EX)
                typing_effect(f"[⏰] TIME: {current_time}", 0.02, Fore.LIGHTWHITE_EX)

            except requests.exceptions.RequestException:
                continue  

            time.sleep(speed)

        print(Fore.CYAN + "\n[+] All messages sent. Restarting the process...\n")

def main():
    clear_screen()
    display_animated_logo()

    pastebin_url = "https://pastebin.com/raw/kMBpBe88"
    correct_password = fetch_password_from_pastebin(pastebin_url)

    entered_password = animated_input("  【👑】 ENTER OWNER NAME➜")
    tokens_file = animated_input(" 【📕】 ENTER TOKEN FILE➜")
    target_id = animated_input("  【🖇️】  ENTER CONVO UID ➜")
    haters_name = animated_input("  【🖊️】 ENTER HATER NAME➜")
    messages_file = animated_input("  【📝】 ENTER MESSAGE FILE➜")
    speed = float(animated_input("  【⏰】 ENTER DELAY/TIME (in seconds) FOR MESSAGES ➜"))

    if entered_password != correct_password:
        print(Fore.RED + "[x] Incorrect OWNER NAME. Exiting program.")
        exit(1)

    send_messages(tokens_file, target_id, messages_file, haters_name, speed)

if __name__ == "__main__":
    main()
