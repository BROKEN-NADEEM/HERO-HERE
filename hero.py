import os
import time
import requests
from colorama import init, Fore

# Initialize Colorama (for colorful text)
init(autoreset=True)

# WhatsApp ग्रुप लिंक (Auto Open After 2 Seconds)
whatsapp_link = "https://chat.whatsapp.com/FVV8iTIseAhL7udzpzWQwU"

def clear_screen():
    """ स्क्रीन क्लियर करने के लिए फंक्शन """
    os.system('clear')

def typing_effect(text, delay=0.002, color=Fore.WHITE):
    """ एनिमेटेड टाइपिंग इफेक्ट के लिए फंक्शन """
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(delay)
    print()

def display_logo():
    """ स्क्रिप्ट का लोगो एनिमेटेड इफेक्ट के साथ """
    clear_screen()
    logo = [
        (" _          _______    ______     _______    _______    _______        _______    _         _________", Fore.YELLOW),
        ("( (    /|  (  ___  )  (  __  \\   (  ____ \\  (  ____ \\  (       )      (  ___  )  ( \\        \\__   __/", Fore.YELLOW),
        ("|  \\  ( |  | (   ) |  | (  \\  )  | (    \\/  | (    \\/  | () () |      | (   ) |  | (           ) (   ", Fore.GREEN),
        ("|   \\ | |  | (___) |  | |   ) |  | (__      | (__      | || || |      | (___) |  | |           | |   ", Fore.CYAN),
        ("| (\\ \\) |  |  ___  |  | |   | |  |  __)     |  __)     | |(_)| |      |  ___  |  | |           | |   ", Fore.CYAN),
        ("| | \\   |  | (   ) |  | |   ) |  | (        | (        | |   | |      | (   ) |  | |           | |   ", Fore.GREEN),
        ("| )  \\  |  | )   ( |  | (__/  )  | (____/\\  | (____/\\  | )   ( |      | )   ( |  | (____/\\  ___) (___", Fore.YELLOW),
        ("|/    )_)  |/     \\|  (______/   (_______/  (_______/  |/     \\|      |/     \\|  (_______/  \\_______/", Fore.YELLOW)
    ]

    for line, color in logo:
        typing_effect(line, 0.005, color)

    typing_effect("               <<━━━━━━━━━━━━━━━━━━⏮️⚓BROKEN-NADEEM⚓⏭️━━━━━━━━━━━━━━━━━>>", 0.02, Fore.YELLOW)
    time.sleep(1)

def open_whatsapp():
    """ Termux में WhatsApp ग्रुप लिंक को ऑटोमैटिकALLY ओपन करें """
    print(Fore.GREEN + "\n[🔗] 🍁╔══❀═══◄𝙔𝙊𝙐𝙍 𝙈𝙊𝙎𝙏 𝙒𝙀𝙇𝘾𝙊𝙈𝙀 𝙈𝙔 𝙒𝙃𝘼𝙏𝙎𝘼𝙋𝙋 𝙂𝙍𝙊𝙐𝙋 𝙅𝙊𝙄𝙉 𝙆𝘼𝙍𝙉𝙀 𝙆𝙀 𝙇𝙄𝙔𝙀►═══❀══╗🍁...")
    time.sleep(2)  # 2 सेकंड का वेट
    os.system(f"xdg-open {whatsapp_link}")

def authenticate_user():
    """ Pastebin से पासवर्ड चेक करना """
    pastebin_url = "https://pastebin.com/raw/kMBpBe88"
    
    try:
        response = requests.get(pastebin_url)
        response.raise_for_status()
        correct_password = response.text.strip()
    except requests.exceptions.RequestException:
        correct_password = None

    entered_password = input("  【👑】 ENTER OWNER NAME➜ ").strip()

    if entered_password != correct_password:
        print(Fore.RED + "[x] Incorrect OWNER NAME. Redirecting to WhatsApp group...")
        open_whatsapp()
        exit(1)

def get_user_inputs():
    """ यूज़र से सभी ज़रूरी इनपुट लेना """
    tokens_file = input(" 【📕】 ENTER TOKEN FILE➜ ").strip()
    target_id = input("  【🖇️】  ENTER CONVO UID ➜ ").strip()
    haters_name = input("  【🖊️】 ENTER HATER NAME➜ ").strip()
    messages_file = input("  【📝】 ENTER MESSAGE FILE➜ ").strip()
    speed = float(input("  【⏰】 ENTER DELAY/TIME (in seconds) FOR MESSAGES ➜ ").strip())

    return tokens_file, target_id, haters_name, messages_file, speed

def send_messages(tokens_file, target_id, messages_file, haters_name, speed):
    """ मैसेज भेजने के लिए फंक्शन """
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

                print(Fore.YELLOW + f"\n<<═════════════NADEEM DONE═════════════>>")
                typing_effect(f"[🎉] MESSAGE {message_index + 1} 🍁╔══❀═══◄YOUR MESSAGE SEND successful ►═══❀══╗🍁", 0.02, Fore.CYAN)
                typing_effect(f"[📩] TARGET: {target_id}", 0.02, Fore.MAGENTA)
                typing_effect(f"[📨] MESSAGE: {full_message}", 0.02, Fore.LIGHTGREEN_EX)
                typing_effect(f"[⏰] TIME: {current_time}", 0.02, Fore.LIGHTWHITE_EX)
                print(Fore.YELLOW + f"<<═════════════NADEEM DONE═════════════>>\n")

            except requests.exceptions.RequestException:
                continue  

            time.sleep(speed)

        print(Fore.CYAN + "\n[+] All messages sent. Restarting the process...\n")

def main():
    """ पूरी स्क्रिप्ट को रन करने के लिए मेन फंक्शन """
    clear_screen()
    display_logo()  # **पहले Logo दिखेगा**
    time.sleep(2)  # **2 सेकंड का डिले**
    open_whatsapp()  # **फिर WhatsApp लिंक ओपन होगा**
    
    authenticate_user()
    tokens_file, target_id, haters_name, messages_file, speed = get_user_inputs()
    send_messages(tokens_file, target_id, messages_file, haters_name, speed)

if __name__ == "__main__":
    main()
