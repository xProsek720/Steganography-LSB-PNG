from stegano import lsb
print("[+] Welcome to Steganodecrypt - LSB")
print("[+] Works best on PNG")

fileName = input("[+] Give a Image File Path that supposed to have a secret: \n[+] ")
clear_message = ""
try:
    # Reveal the message
    clear_message = lsb.reveal(fileName)
except Exception as e:
    print(f"[+] ERR: {e}")
if clear_message != "":
    print(f"[+] Secret text: \n[+] {clear_message}")
