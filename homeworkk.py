#  Oila a'zolari lug'ati
oilam = {
    "otam": {
        "ism": "Mavludtin",
        "tugilgan_yil": 1982,
        "shahar": "Samarqand"
    },
    "onam": {
        "ism": "Zulayho",
        "tugilgan_yil": 1983,
        "shahar": "Buxoro"
    }
}

# Ota haqida ma'lumotni chiqarish
print(f"Otamning ismi {oilam['otam']['ism']}, {oilam['otam']['tugilgan_yil']}-yilda, {oilam['otam']['shahar']} viloyatida tug'ilgan.\n")

#  Oila a'zolarining sevimli taomlari
taomlar = {
    "Ali": "osh",
    "Vali": "manti",
    "Gulnoza": "shashlik",
    "Aziza": "lag'mon",
    "Shavkat": "somsa"
}

# Har birining sevimli taomini chiqarish
for ism, taom in taomlar.items():
    print(f"{ism}ning sevimli taomi {taom}")
print()

#  Python izohli lug‘ati
python_lugat = {
    "integer": "Butun son",
    "float": "O'nlik son",
    "string": "Matn",
    "boolean": "Mantiqiy qiymat (True/False)",
    "list": "Ro'yxat",
    "tuple": "O'zgarmas ro'yxat",
    "dictionary": "Lug'at",
    "if": "Shart operatori",
    "else": "Aks holda",
    "for": "Takrorlanish operatori"
}

#  Foydalanuvchidan so'z kiritishni so'rash
kalit = input("Kalit so'z kiriting: ").lower()

#  if-else orqali tekshirish va natijani chiqarish
if kalit in python_lugat:
    print(f"{kalit.capitalize()} so'zi {python_lugat[kalit]} deb tarjima qilinadi.")
else:
    print("Bunday so'z mavjud emas.")
