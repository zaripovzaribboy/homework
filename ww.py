class Shaxs:
    odamlar_soni = 0

    def __init__(self, ism, yosh):
        self.__ism = ism
        self.__yosh = yosh
        Shaxs.odamlar_soni += 1

    def get_ism(self):
        return self.__ism

    def set_ism(self, ism):
        self.__ism = ism

    @classmethod
    def get_odamlar_soni(cls):
        return cls.odamlar_soni


class Talaba(Shaxs):
    talabalar_soni = 0

    def __init__(self, ism, yosh, id_raqam):
        super().__init__(ism, yosh)
        self.__id = id_raqam
        Talaba.talabalar_soni += 1

    def get_id(self):
        return self.__id

    def set_id(self, id_raqam):
        self.__id = id_raqam

    @classmethod
    def get_talabalar_soni(cls):
        return cls.talabalar_soni


# Ob'ektlar yaratish
talaba1 = Talaba("Ali", 20, "T001")
talaba2 = Talaba("Vali", 21, "T002")

print("Odamlar soni:", Shaxs.get_odamlar_soni())
print("Talabalar soni:", Talaba.get_talabalar_soni())