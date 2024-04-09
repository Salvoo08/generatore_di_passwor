import random
caratteri = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

x = int(input("Inserisci la lungezza della passworld: "))

password = ""

for i in range(x):
    password = password +  random.choice(caratteri)
print(password)