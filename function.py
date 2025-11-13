# kvadrat va kub topish
def kvadrat_va_kub():
    """kvadrat va kubni aniqlovchi funk"""
    s = 5
    n = float(s)
    print(f"Siz kiritgan son: {n}")
    print(f"Kvadrati: {n**2}")
    print(f"Kubi: {n**3}")

kvadrat_va_kub()



#juft yoki toq aniqlash

def juft_yoki_toq():
    """Juft yoki toq son ekanligini aniqlovchi funksiya"""
    s = 8
    n = int(s)
    if n % 2 == 0:
        print(f"{n} juft son")
    else:
        print(f"{n} toq son")

juft_yoki_toq()



# #katta sonni chiqarish

def katta_sonni_chiqar():
    """katta va kichik sonni aniqlovchi funksiya"""
    a_str = 6
    b_str = 7
    a = float(a_str)
    b = float(b_str)

    if a > b:
        print(f"Katta son: {a}")
    elif b > a:
        print(f"Katta son: {b}")
    else:
        print("Sonlar teng")

katta_sonni_chiqar()
