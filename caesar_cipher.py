def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        # Encrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # Non-alphabetic characters are added unchanged
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

if __name__ == "__main__":
    plaintext = "Hello World! This is a CTF flag."
    shift = 3  # Caesar cipher shift value

    # Encrypt the message
    encrypted_text = caesar_encrypt(plaintext, shift)
    print(f"Encrypted text: {encrypted_text}")

    # Decrypt the message
    decrypted_text = caesar_decrypt(encrypted_text, shift)
    print(f"Decrypted text: {decrypted_text}")
