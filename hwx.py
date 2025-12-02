#Asosiy klass 
class Shaxs:
    def __init__(self, ism, familiya, t_yil):
        self.ism = ism
        self.familiya = familiya
        self.t_yil = t_yil

    def get_info(self):
        return f"{self.ism} {self.familiya}, {self.t_yil}-yilda tug'ilgan"


#Fan klass
class Fan:
    def __init__(self, nomi):
        self.nomi = nomi

    def __repr__(self):
        return self.nomi


#Talaba klass
class Talaba(Shaxs):
    def __init__(self, ism, familiya, t_yil):
        super().__init__(ism, familiya, t_yil)
        self.fanlar = [] 

    def fanga_yozil(self, fan_obj):
        """Tələbaga fan qo'shish"""
        self.fanlar.append(fan_obj)

    def remove_fan(self, fan_obj):
        """Tələbadan fan olib tashlash"""
        if fan_obj in self.fanlar:
            self.fanlar.remove(fan_obj)
        else:
            print("Siz bu fanga yozilmagansiz!")

    def get_info(self):
        info = super().get_info()
        fanlar = ", ".join([fan.nomi for fan in self.fanlar]) or "Fan yo'q"
        return info + f"\nO'quvchi fanlari: {fanlar}"






class Foydalanuvchi(Shaxs):
    def __init__(self, ism, familiya, t_yil, username):
        super().__init__(ism, familiya, t_yil)
        self.username = username

    def get_info(self):
        return super().get_info() + f"\nUsername: @{self.username}"






class Admin(Foydalanuvchi):
    def __init__(self, ism, familiya, t_yil, username, huquq="to'liq"):
        super().__init__(ism, familiya, t_yil, username)
        self.huquq = huquq

    def ban_user(self, user_obj):
        print(f"Foydalanuvchi bloklandi: @{user_obj.username}")

    def get_info(self):
        return super().get_info() + f"\nAdmin huquqi: {self.huquq}"



matematika = Fan("Matematika")
fizika = Fan("Fizika")
ingliz = Fan("Ingliz tili")


talaba1 = Talaba("Ali", "Karimov", 2005)


talaba1.fanga_yozil(matematika)
talaba1.fanga_yozil(fizika)


talaba1.remove_fan(ingliz)

print(talaba1.get_info())

print("\n")
admin = Admin("Olim", "Rasulov", 1990, "olim_admin")
user = Foydalanuvchi("Jasur", "Aliyev", 2002, "jasur2002")

admin.ban_user(user)

print("\n Admin haqida")
print(admin.get_info())
