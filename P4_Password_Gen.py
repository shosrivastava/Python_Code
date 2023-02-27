print("Thos code generates a random password in Uppercase, Lowercase and including numbers.\n")

from random import randint

password = ""

for i in range(5):
    i = chr(randint(65, 90))
    j = chr(randint(65, 90)).lower()
    k = randint(0, 10)
    password = str((password) + i + j + str(k))

print(f"The randomly generated password is {password}\n")
print(f"The length of the generated password is {len(password)}.")