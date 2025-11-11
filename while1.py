
# son=1
# while son<=5:
#     print(son, end=',')
#     son = son+1



# print("Kiritilgan sonning kvadratini qaytaruvchi dastur:")
# savol = "Istalgan son kiriting:"
# savol +="(dasturni to'xtatish uchun 'exit' deb yozing):"

# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#         print(float(qiymat)**2)


# while True:
#     print("Salom")


# print("hello")





# sonlar = list(range(1,10))
# for son in sonlar:
#     if son == 5:
#         break
#     print(f"{son} ning kvadrati {son**2} ga teng")




# ismlar = []

# print("yaqin jigarlar ro'yxatini tuzamiz:")
# n=1
# while True:
#     savol = f"{n}-do'stingizni ismini kiriting:"
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("yana ism qo'shamizmi? (ha/yoq)")
#     if javob =='ha':
#         n+=1
#         continue
#     else:
#         break
#     print(ismlar)



# print("Do'stlaringiz yoshini saqlaymiz:")
# dostlar = {}
# ishora = True

# while ishora:
#     ism = input("Do'stingiz ismini kiriting: ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism] = int(yosh)

#     javob = input("Yana malumot qo'shasizmi? (ha/yo'q): ")
#     if javob == "yo'q":
#         ishora = False

# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")




# cars= ['lacetti','nexia','toyota','nexia','audi','jeep','nexia']
# while 'nexia' in cars:
#     cars.remove('nexia')
#     print(cars)


# talabalar = ['jonibek', 'husan', 'olim', 'asror']
# baholangan_talabalar = {}

# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi.")
#     baholangan_talabalar[talaba] = baho

# print(baholangan_talabalar)