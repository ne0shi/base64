import base64
import sys
_author_ = "Shin"
_credits_ = ["WeebSec", "Abdullah"]
_version_ = 2.7
def banner():
    print(r"""\    
   _____ __    _     
  / ___// /_  (_)___ 
  \__ \/ __ \/ / __ \
 ___/ / / / / / / / /
/____/_/ /_/_/_/ /_/ 
                     """)
banner()
print("1: Encode with base64")
print("2: Decode with base64")
choice = int(input("Enter your choice: "))
try:
    if choice == 1:
        messageEncode = raw_input("Enter the string that you want to encode: ")
        x = base64.b64encode(messageEncode)
        print("The string has been encoded: " + x)

    if choice == 2:
        messageDecode = raw_input("Enter the string you want to decode: ")
        x = base64.b64decode(messageDecode)
        print("The string has been decoded: " + x)
except:
    print("Please make sure to input a b64encode message")
sys.exit()