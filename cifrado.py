def encrypt_vigenere(plain_text, key):
    encrypted_text = ""
    key_index = 0
    for char in plain_text:
        if char.isalpha():
            char = char.upper()
            shift = ord(key[key_index].upper()) - ord('A')
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_text += encrypted_char
            key_index = (key_index + 1) % len(key)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_vigenere(encrypted_text, key):
    decrypted_text = ""
    key_index = 0
    for char in encrypted_text:
        if char.isalpha():
            char = char.upper()
            shift = ord(key[key_index].upper()) - ord('A')
            decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            decrypted_text += decrypted_char
            key_index = (key_index + 1) % len(key)
        else:
            decrypted_text += char
    return decrypted_text

# Ingreso del texto y la clave por parte del usuario
plain_text = input("Ingrese el texto a cifrar: ")
key = input("Ingrese la clave: ")

encrypted_text = encrypt_vigenere(plain_text, key)
print("Texto cifrado:", encrypted_text)

decrypted_text = decrypt_vigenere(encrypted_text, key)
print("Texto descifrado:", decrypted_text)
