def encrypt(message, key):
    result = ""
    for letter in message:
        position = ord(letter) - ord("A")
        new_postion = (position + key) % 26
        new_letter =chr(new_postion + ord("A"))
        result += new_letter
    return result

message = "CYBERSECURITY"
key = 5 

ciphertext = encrypt(message, key)

print ("plaintext:", message)
print ("ciphertext:", ciphertext)