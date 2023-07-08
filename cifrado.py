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

def main():
    print("Bienvenido al cifrador Vigenère")
    option = input("Ingrese 'C' para cifrar o 'D' para descifrar: ")

    if option.upper() == 'C':
        plain_text = input("Ingrese el texto a cifrar: ")
        key = input("Ingrese la clave: ")

        encrypted_text = encrypt_vigenere(plain_text, key)
        print("Texto cifrado:", encrypted_text)

    elif option.upper() == 'D':
        encrypted_text = input("Ingrese el texto a descifrar: ")
        key = input("Ingrese la clave: ")

        decrypted_text = decrypt_vigenere(encrypted_text, key)
        print("Texto descifrado:", decrypted_text)

    else:
        print("Opción no válida. Por favor, ingrese 'C' o 'D'.")

main()
