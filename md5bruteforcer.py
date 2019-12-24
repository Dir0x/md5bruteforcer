import hashlib

hashtodecrypt = input("Enter your hash: ")
wordlist = input("Enter your wordlist: ")

with open(wordlist) as file:
    for line in file:
        leng = len(line)
        line2 = line[:leng - 1]
        result = hashlib.md5(line2.encode())
        result2 = result.hexdigest()
        if result2 == hashtodecrypt:
            print(hashtodecrypt + ' is the hash of: ' + line2)
