# Polyalphabetic_Cipher
## Profil
| #               | Biodata                 |
| --------------- | ----------------------- |
| **Nama**        | Nabilah Ananda Putri    |
| **NIM**         | 312110263               |
| **Kelas**       | TI.21.A.1               |
| **Mata Kuliah** | Kriptografi             |

### Tugas
- Butlah program untuk enkripsi dan dekripsi menggunakan metode polyalphabetic cipher!

### Hasil
- ![Screenshot (209)](https://github.com/nabilahap/Polyalphabetic_Cipher/assets/92380488/a2c1e107-c51e-44a2-883e-e0027852f62b)
- ![Screenshot (210)](https://github.com/nabilahap/Polyalphabetic_Cipher/assets/92380488/818f3b02-58d3-4c54-afc6-7ab0ad886fb7)


#### 1. Fungsi polyalphabetic_cipher_encrypt
- Fungsi ini digunakan untuk mengenkripsi teks dengan metode polyalphabetic cipher.
- Parameter `plaintext` adalah teks yang akan dienkripsi, dan parameter key adalah kunci yang digunakan dalam enkripsi.
- Variabel alphabet berisi alfabet dalam huruf kecil.
- Variabel `encrypted_text` akan menyimpan hasil enkripsi.
- Fungsi ini mengiterasi melalui setiap karakter dalam plaintext.

```py
for char in plaintext:
```

- Jika karakter tersebut terdapat dalam alfabet, maka indeks karakter dalam alfabet dihitung.

```py
if char in alphabet:
    char_index = alphabet.index(char)
```

- Selanjutnya, karakter kunci yang sesuai diambil berdasarkan indeks karakter dalam alfabet dan panjang kunci.

```py
key_char = key[char_index % len(key)]
```

- Karakter kunci ini ditambahkan ke dalam `encrypted_text`.

```py
encrypted_text += key_char
```

- Akhirnya, teks hasil enkripsi dikembalikan.

#### 2. Fungsi polyalphabetic_cipher_decrypt
- Fungsi ini digunakan untuk mendekripsi teks yang telah dienkripsi menggunakan metode polyalphabetic cipher.
- Parameter ciphertext adalah teks yang akan didekripsi, dan parameter `key` adalah kunci yang digunakan dalam dekripsi.
- Fungsi ini memiliki struktur serupa dengan fungsi enkripsi, tetapi sebaliknya.

#### 3. Inisialisasi Alfabet dan Kunci
- Program ini menginisialisasi alfabet sebagai `abcdefghijklmnopqrstuvwxyz`.
- Pengguna diminta untuk memasukkan kunci (key) melalui input.

```py
kunci = input("Masukkan kunci: ").lower()
```

- Kunci ini digabungkan dengan alfabet untuk membuat kunci lengkap yang akan digunakan dalam enkripsi dan dekripsi.

```py
hasil = kunci + abjad
key = "".join(dict.fromkeys(hasil))
```

#### 4. Perulangan While
- Program utama berjalan dalam perulangan tak terbatas (selama True).
- Program menampilkan menu pilihan kepada pengguna.

```py
print("\nMenu:")
print("1. Enkripsi")
print("2. Dekripsi")
print("3. Keluar")
```

-Pengguna diminta untuk memilih salah satu opsi dengan memasukkan nomor yang sesuai dalam variabel `choice`.

```py
choice = input("Pilih menu (1/2/3): ")
```

- Program akan merespons berdasarkan pilihan pengguna.

#### 5. Pilihan Enkripsi
- Jika pengguna memilih opsi '1' (Enkripsi), program meminta pengguna untuk memasukkan teks yang akan dienkripsi.
  
```py
plaintext = input("Masukkan plaintext: ").lower()
```

- Fungsi `polyalphabetic_cipher_encrypt` dipanggil untuk melakukan enkripsi.
- Hasil enkripsi ditampilkan kepada pengguna.

#### 6. Pilihan Dekripsi
- Jika pengguna memilih opsi '2' (Dekripsi), program meminta pengguna untuk memasukkan teks yang akan didekripsi.

```py
ciphertext = input("Masukkan ciphertext: ").lower()
```

- Fungsi `polyalphabetic_cipher_decrypt` dipanggil untuk melakukan dekripsi.
- Hasil dekripsi ditampilkan kepada pengguna.

#### 7. Pilihan Keluar
- Jika pengguna memilih opsi '3' (Keluar), program akan mengakhiri perulangan dan mencetak pesan "Terima Kasih!".

#### 8. Kesalahan Pilihan
- ika pengguna memasukkan pilihan yang tidak valid, program akan mencetak pesan "Pilihan tidak valid. Silakan pilih 1, 2, atau 3."
