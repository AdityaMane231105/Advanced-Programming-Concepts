def caesar_encrypt(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

msg = input("Enter message: ")
shift = int(input("Enter shift: "))
enc = caesar_encrypt(msg, shift)
print("Encrypted:", enc)
print("Decrypted:", caesar_decrypt(enc, shift))
