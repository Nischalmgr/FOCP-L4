'''Write a program that decrypts messages encoded as above.'''
from four import encrypts
from five import random_interval_encrypt

def decrypt_with_interval_but_with_filler(encrypted_message, filler_letter, interval):
    
    
    decrypted_message = encrypted_message[interval - 1::interval]
    return decrypted_message

 
if __name__ == "__main__":
    test_message = input("Enter a message: ")
    
    if not test_message.strip():
        print("The message cannot be empty.")
    else:
        reversed_message = encrypts(test_message)
        filler_letter = input("Enter a filler letter (default is 'x'): ") or "x"
        if len(filler_letter) != 1:
            print("Filler letter must be a single character. Using default 'x'.")
            filler_letter = "x"
        encrypted_message, interval = random_interval_encrypt(reversed_message, filler_letter)
        
        print(f"\nOriginal Message: {test_message}")
        print(f"Reversed Message: {reversed_message}")
        print(f"Encrypted Message: {encrypted_message}")
        print(f"Interval Used: {interval}\n")
        decrypted_message = decrypt_with_interval_but_with_filler(encrypted_message, filler_letter, interval)
        print(f"Decrypted Message (Reversed): {decrypted_message}")
        final_message = decrypted_message[::-1]
        print(f"Final Decrypted Original Message: {final_message}")
