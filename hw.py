#  Foydalanuvchi login tanlaydi
foydalanuvchilar = ["anvar", "umid", "umidaxon", "aziz", "malika"]

login = input("Yangi login tanlang: ")

if login in foydalanuvchilar:
    print("Login band, yangi login tanlang!")
else:
    foydalanuvchilar.append(login)
    print(f"Xush kelibsiz, {login}!")


#  Juft son kiritish
son = int(input("Juft son kiriting: "))

if son % 2 == 0:
    print("Rahmat!")
else:
    print("Bu son juft emas.")


#  Ikkita sonni solishtirish
a = float(input("\nBirinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))

if a < b:
    print(f"{a} < {b}")
elif a > b:
    print(f"{a} > {b}")
else:
    print(f"{a} = {b}")

