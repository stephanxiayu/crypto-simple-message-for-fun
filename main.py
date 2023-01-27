
from crypto import crypto
from alpha import alphabet

print(f"{crypto}\n")
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encode(plain_text, shift_amount):
  cipher_text=""
  for letter in plain_text:
    position=alphabet.index(letter)
    new_position=position+shift_amount
    new_letter=alphabet[new_position]
    cipher_text+=new_letter
  print(f"dein text ist {cipher_text}")  
   

def decode(cipher_text, shift_amount):
  plain_text=""
  for letter in cipher_text:
    position=alphabet.index(letter)
    new_position=position-shift_amount
    new_letter=alphabet[new_position]
    plain_text+=new_letter
  print(f"dein text ist {plain_text}")      

   
def richtung():
  if direction=="encode":
    encode(plain_text=text, shift_amount=shift)
  elif direction=="decode":
    decode(cipher_text=text, shift_amount=shift)
  else: 
    print("alter, bist du dämlich?")  
   
richtung()
