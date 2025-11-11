

davlatlar = {
    "O'zbekiston": {
        "poytaxt": "Toshkent",
        "hudud": "448978 kv.km",
        "aholi": "33000000",
        "pul_birligi": "so'm"
    },
    "Rossiya": {
        "poytaxt": "Moskva",
        "hudud": "17098246 kv.km",
        "aholi": "144000000",
        "pul_birligi": "rubl"
    },
    "AQSH": {
        "poytaxt": "Vashington",
        "hudud": "9631418 kv.km",
        "aholi": "327000000",
        "pul_birligi": "dollar"
    },
    "Malayziya": {
        "poytaxt": "Kuala-Lumpur",
        "hudud": "329750 kv.km",
        "aholi": "25000000",
        "pul_birligi": "rinngit"
    }
}


davlat_nomi = input("Davlat nomini kiriting: ").title()





if davlat_nomi in davlatlar:
    info = davlatlar[davlat_nomi]
    print(f"\n{davlat_nomi}ning poytaxti {info['poytaxt']}")
    print(f"Hududi: {info['hudud']}")
    print(f"Aholisi: {info['aholi']}")
    print(f"Pul birligi: {info['pul_birligi']}")
else:
    print("\nBizda bu davlat haqida ma'lumot mavjud emas")

