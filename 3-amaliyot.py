with open("pi_million_digits.txt", "r") as file:
    pi_text = file.read()

pi_text = pi_text.replace("\n", "").replace(" ", "").replace(".", "")

def check_birthday(day, month, year, pi_digits):
    raqam = f"{day:02d}{month:02d}{year}"
    if raqam in pi_digits:
        print(f"{raqam} π ichida uchradi!")
    else:
        print(f"{raqam} π ichida uchramadi.")

check_birthday(27, 5, 2004, pi_text)










import pickle

pi_float = float("3." + pi_text[1:20])   # million xonani float qila olmaydi, shuning uchun qisqa qismi

with open("pi_float.pkl", "wb") as f:
    pickle.dump(pi_float, f)

print("Float ko‘rinishida pickle fayl saqlandi: pi_float.pkl")







while True:
    malumot = input("Ma'lumot kiriting (chiqish uchun 'exit'): ")

    if malumot.lower() == "exit":
        print("Dastur tugadi.")
        break

    with open("malumotlar.txt", "a", encoding="utf-8") as f:
        f.write(malumot + "\n")

    print("Ma'lumot faylga yozildi!\n")












