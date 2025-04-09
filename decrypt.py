from replacements import decrypt

ciphertext = input("Enter your ciphertext:\n").replace(" ","")

if len(ciphertext) % 11 != 0:
    print("Invalid ciphertext length. It must be a multiple of 11.")
    exit()

decrypted = ""
for i in range(0, len(ciphertext), 11):
    chunk = ciphertext[i:i+11]
    if chunk in decrypt:
        decrypted += decrypt[chunk]
    else:
        print(f"Invalid chunk found: {chunk}")
        exit()

print("\nDecrypted text:")
print(decrypted)
