# 1-misol


pochtalar = ["user1@gmail.com", "user2yahoo.com", "user3@outlook.com"]

for email in pochtalar:
    if "@" not in email:
        print(f"Noto'g'ri email: {email}")
    else:
        print(f"To‘g‘ri email: {email}")



#2-misol

parollar = ["password123", "Qwerty!", "admin", "StrongPass1!"]

for parol in parollar:
    if len(parol) < 8:
        print(f"{parol} → Juda qisqa")
    elif parol.isalpha() or parol.isdigit():
        print(f"{parol} → Kuchsiz parol")
    else:
        print(f"{parol} → Kuchli parol")



# 3-misol

haroratlar = [20, 22, 19, 24, 25, 23, 21]

# O‘rtacha haroratni hisoblash
ortalacha = sum(haroratlar) / len(haroratlar)
print(f"O‘rtacha harorat: {ortalacha:.1f}°C")

for harorat in haroratlar:
    if harorat > 22:
        print(f"{harorat}°C → Iliq kun")
    else:
        print(f"{harorat}°C → Salqin kun")



# 4-misol

taomlar = ["Osh", "Shashlik", "Manti", "Lag'mon"]
buyurtma = input("Buyurtmangizni kiriting: ")

for taom in taomlar:
    if buyurtma.lower() == taom.lower():
        print("Buyurtmangiz qabul qilindi ✅")
        break
else:
    print("Kechirasiz, bunday taom yo‘q ❌")


# 5misol

yoshlari = [16, 21, 17, 30, 25]

for yosh in yoshlari:
    if yosh < 18:
        print(f"{yosh} yosh → Yosh chegarasiga yetmagan ❗")
    else:
        print(f"{yosh} yosh → Xush kelibsiz 🎉")


# 6 misol

xabarlar = ["Yangi xabar", "Batareya past", "Yangilanish mavjud"]

for xabar in xabarlar:
    if xabar == "Batareya past":
        print("Telefoningizni quvvatlang 🔋")


# 7-misol

fayllar = ["kitob.jpg", "ko'jiguli.mp3", "tabiat.jpg", "malohat.mp3", "iphone16.jpg"]
musiqalar = []
rasmlar = []

for fayl in fayllar:
    if fayl.find(".jpg") != -1:
        rasmlar.append(fayl)
    elif fayl.find(".mp3") != -1:
        musiqalar.append(fayl)

print("📸 Rasmlar:", rasmlar)
print("🎵 Musiqalar:", musiqalar)


