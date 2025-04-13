
chars = """~`! @#$%^&*()_-+={[}]|\:;"'<,>.?/"""
def encrypt(msg):
    res = ''
    for i in msg:
        if i.isupper():
            res += chr((ord(i) + 3 - 65) % 26 + 65)
        elif i.islower():
            res += chr((ord(i) + 3 - 97) % 26 + 97)
        elif i.isdigit():
            res += chr((ord(i) + 3 - 48) % 10 + 48)
        elif i in chars:
            res += chr((ord(i) + 3 - 32) % len(chars) + 32)
        else:
            res += i
    return res

def decrypt(msg):
    res = ''
    for i in msg:
        if i.isupper():
            res += chr((ord(i) - 3 - 65) % 26 + 65)
        elif i.islower():
            res += chr((ord(i) - 3 - 97) % 26 + 97)
        elif i.isdigit():
            res += chr((ord(i) - 3 - 48) % 10 + 48)
        elif i in chars:
            res += chr((ord(i) - 3 - 32) % len(chars) + 32)
        else:
            res += i
    return res

q = 0
while q == 0:
    msg = input("Enter the message: ")
    en = encrypt(msg)
    de = decrypt(en)
    print(f"Encrypted message: {en}")
    print(f"Decrypted message: {de}")
    q = int(input("Press 0 to continue or 1 to exit: "))