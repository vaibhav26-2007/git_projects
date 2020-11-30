import string
import random

if __name__ == '__main__':
    S1 = string.ascii_lowercase
    S2 = string.ascii_uppercase
    S3 = string.digits
    S4 = string.punctuation

    try:
        passwordLen = int(input("Enter The Length Of Your Password:\n"))
        s = []
        s.extend(list(S1))
        s.extend(list(S2))
        s.extend(list(S3))
        s.extend(list(S4))

        random.shuffle(s)
        print("Your Password Is:\n")
        print("".join(s[0:passwordLen]))
    except:
        print("Please Enter A Valid Number :)  ")
