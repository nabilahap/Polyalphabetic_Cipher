def polyalphabetic_cipher_encrypt(plaintext, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in plaintext:
        if char in alphabet:
            char_index = alphabet.index(char)
            key_char = key[char_index % len(key)]
            encrypted_text += key_char

    return encrypted_text

def polyalphabetic_cipher_decrypt(ciphertext, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decrypted_text = ''

    for char in ciphertext:
        if char in alphabet:
            key_char_index = key.index(char)
            char_index = key_char_index % len(key)
            decrypted_text += alphabet[char_index]

    return decrypted_text

abjad = "abcdefghijklmnopqrstuvwxyz"
kunci = input("Masukkan kunci: ").lower()
hasil = kunci + abjad
key = "".join(dict.fromkeys(hasil))

while True:
    print("\nMenu:")
    print("1. Enkripsi")
    print("2. Dekripsi")
    print("3. Keluar")

    choice = input("Pilih menu (1/2/3): ")

    if choice == '1':
        plaintext = input("Masukkan plaintext: ").lower()
        encrypted_text = polyalphabetic_cipher_encrypt(plaintext, key)
        print("Hasil Enkripsi:", encrypted_text)
    elif choice == '2':
        ciphertext = input("Masukkan ciphertext: ").lower()
        decrypted_text = polyalphabetic_cipher_decrypt(ciphertext, key)
        print("Hasil Dekripsi:", decrypted_text)
    elif choice == '3':
        print("Terima Kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
