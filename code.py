from stegano import lsb
import sys

def encodePicture(message: str, imgPath: str, output: str = "secret.png"):
    # Hide the secret message
    secret = lsb.hide(imgPath, message)
    secret.save(f"{output}")
    return output

print("[+] Welcome to Steganocrypt - LSB")
print("[+] Works best on PNG, you can try JPG but not guaranteed")

message = ""
imgPath = ""
output = ""
if len(sys.argv) > 2:
    message = sys.argv[1]
    imgPath = sys.argv[2]
else:
    message = input("[+] Give a message to hide inside Picture: \n[+] ")
    imgPath = input("[+] Give a path to img that you want to hide message in: \n[+] ")
    decide = input("[+] Do you want to choose file name for output [y/n]\n[+] ")
    while decide not in ["y", "Y", "n", "N"]:
        decide = input("[+] The answer should be: 'y'/'n'\n[+] ")
    if decide in ["y", "Y"]:
        output = input("[+] Give a file name for output include extension:\n[+] ")


print("[+] Executing crypting function...")
if output != "":
    encodePicture(message, imgPath, output)
else:
    output = encodePicture(message, imgPath)
print(f"[+] Done! \n[+] Saved as {output}")
# Reveal the message
clear_message = lsb.reveal(output)
print(clear_message)
