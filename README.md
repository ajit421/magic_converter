# 🔐 Magic Converter

A fun and secure **custom 11-bit character encryption & decryption tool** using Python!  
Each character is mapped to a unique 11-character string using special characters and emojis (if you like), making it a personalized and playful cipher.

## ✨ Features

- Custom 11-bit encoding per character
- Lightweight and dependency-free
- Space is ignored during encryption, allowed freely in decryption
- Easy-to-read and modular Python code
- Supports all lowercase letters (`a-z`), digits (`0-9`), and space
- Ideal for beginner-friendly cryptography experiments



## 📂 Project Structure

```
magic_converter/
├── encrypt.py        # Script to encrypt plaintext input
├── decrypt.py        # Script to decrypt encoded text
├── replacements.py   # Dictionary of character-to-11bit-string mapping
└── README.md         # Project documentation
```

---

## ⚙️ How It Works

### Encryption
Each character from the input is replaced by a unique 11-character string using a custom dictionary defined in `replacements.py`.

### Decryption
The encoded string is split into 11-character chunks and matched back to their original characters using a reverse lookup.

---

## 🚀 Usage

### 1. Encrypt Text
```bash
python encrypt.py
```
**Input:**
```
hello ajit
```
**Output:**
```
Encrypted text:

Hjl;'658v3|E7!+p9=qWw)zx=vbn=,./7zx=vbn=,./7xzcv#,._/+n*@/#|^v@,:d~!@1$*2&*()J1!q2#3e4r5Iza_+@}}[]i&*()_+|i|=6
```

### 2. Decrypt Text
```bash
python decrypt.py
```
**Input:**
```

Hjl;'658v3|E7!+p9=qWw)zx=vbn=,./7zx=vbn=,./7xzcv#,._/+n*@/#|^v@,:d~!@1$*2&*()J1!q2#3e4r5Iza_+@}}[]i&*()_+|i|=6
```
**Output:**
```
decrypted text:
hello ajit
```

---

## ✅ Requirements

- Python 3.x
- No external libraries required
---

## 👤 Author
 **Ajit Kumar** — [GitHub](https://github.com/ajit421)

---

## ⭐ Star This Repo
If you found this project helpful, please consider giving it a ⭐ on GitHub!

