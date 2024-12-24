'''Another way to hide a message is to include the letters that make it up within
seemingly random text. The letters of the message might be every filw character,
for example. Write and test a function that does such encryption. It should
randomly generate an interval (between 2 and 20), space the message out
accordingly, and should fill the gaps with random letters. The function should
return the encrypted message and the interval used.'''
import random
def encrypts(message):
    no_spaces=message.replace(" ","")
    encrypt_msg=no_spaces[::-1]
    return encrypt_msg
 
def random_interval_encrypt(message, filler_letter):
    
    interval = random.randint(2, 20)
    
     
    stripped_message = message.replace(" ", "")
     
    encrypted_message = []
    
 
    for char in stripped_message:
         
        encrypted_message.extend(filler_letter * (interval - 1))
        encrypted_message.append(char)
    encrypted_message.extend(filler_letter * (interval - 1))
    return ''.join(encrypted_message), interval

 
if __name__ == "__main__":
    test_message = input("enter a message")
    message=encrypts(test_message)
    filler_letter = "xyz"   
    encrypted, interval = random_interval_encrypt(message, filler_letter)
    print(f"Original Message: {test_message}")
    print(f"Encrypted Message: {encrypted}")
    print(f"Interval Used: {interval}")
