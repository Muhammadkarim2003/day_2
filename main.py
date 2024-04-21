print("Welcome!")

bill = float(input("Umumiy hisob qancha edi $"))

tip = int(input("10, 12 yoki 15 ga qancha maslahat berishni xohlaysiz? "))

odamlar = int(input("hisobni necha kishiga bo'lish kerak? "))

foiz = tip / 100
umumiy_miqdor = bill * foiz
umumiy_hisob = bill + umumiy_miqdor
kishi_boshiga_hisob = umumiy_hisob / odamlar
ohirgi_natija = round(kishi_boshiga_hisob, 2)
# ohirgi_natija = "{:.2f}"

print(f"Kishi boshiga {ohirgi_natija}$ dan")

