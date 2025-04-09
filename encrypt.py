from replacements import encrypt

text = input("Enter your plaintext:\n").lower()

encrypted = ""
for char in text:
    if char in encrypt:
        encrypted += encrypt[char]
    else:
        print(f"Character not supported: {char}")
        exit()

print("\nEncrypted text:")
print(encrypted)
