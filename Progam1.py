import random
element = " ajsijkjsdfkjsdkjlsjajpafpm1234567890+-=!@#$%^&*()_+"
panjang_password = int(input("Passwordnya mau berapa karakter, bang?"))

password = ""
for i in range(panjang_password):
    password += random.choice(element)

print(password)
