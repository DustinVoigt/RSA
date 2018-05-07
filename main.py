def encrypt(e,n):
  message=''
  encrypted_message = ''
  message=input("Whats your message?")
  for x in message: 
    numerize = ord(x)
    encrypt = pow(numerize, e, n)
    denumerize = chr(encrypt)
    encrypted_message += denumerize
    
  print (encrypted_message)

def decrypt(d,n):
  decrypted_message = ""
  encrypted_message=input("Whats your encrypted message?")
  for x in encrypted_message: 
    numerize = ord(x)
    decrypt = pow(numerize, d, n)
    denumerize = chr(decrypt)
    decrypted_message  += denumerize
    
  print (decrypted_message)
 
def menu():
  x = 2
  while x !=1:
    print ("Choose What You Want To Do")
    print ("A) Encrypt")
    print ("B) Decrypt")
    print ("C) Exit")
    z = input("Whats your choice?")
    if z == "A)":
      e=int(input("Whats your e?"))
      n=int(input("Whats your n?"))
      encrypt (e,n) 
    elif z == "B)":
      d=int(input("Whats your d?"))
      n=int(input("Whats your n?"))
      decrypt (d,n)
    elif z == "C)": 
      x = 1
    else: 
      print ("Unknown Command")
      z = input("Whats your choice?")
  print ("Thanks for playing")