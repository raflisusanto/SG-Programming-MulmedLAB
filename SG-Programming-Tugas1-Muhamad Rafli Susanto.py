status = True
while status:
    bangun = input("Bangun Ruang yang ingin dicari volume dan luasnya (balok/tabung/kerucut): ")
    bangun = bangun.lower()
    if bangun == "balok":
        status = False
        p = float(input("Masukkan Panjang Balok: "))
        l = float(input("Masukkan Lebar Balok: "))
        t = float(input("Masukkan Tinggi Balok: "))
        volume = p * l * t
        luas = 2 * ((p * l)+(p * t)+(l * t))
    elif bangun == "tabung":
        status = False
        r = float(input("Masukkan Jari-Jari Tabung: "))
        t = float(input("Masukkan Tinggi Tabung: "))
        if r % 7 == 0:
            volume = 22/7 * (r**2) * t
            luas = 2 * 22/7 * r * (r+t)
        else:
            volume = 3.14 * (r ** 2) * t
            luas = 2 * (3.14) * r * (r + t)
    elif bangun == "kerucut":
        status = False
        r = float(input("Masukkan Jari-Jari Kerucut: "))
        t = float(input("Masukkan Tinggi Kerucut: "))
        s = ((r**2)+(t**2))**1/2
        if r % 7 == 0:
            volume = 1/3 * 22/7 * (r**2) * t
            luas = (22/7 * (r**2)) + (22/7 * r * s)
        else:
            volume = 1 / 3 * 3.14 * (r ** 2) * t
            luas = (3.14 * (r ** 2)) + (22 / 7 * r * s)
    else:
        print("Bangun tidak ditemukan, silahkan coba input kembali.")
        print()

volume = float("{:.2f}".format(volume))
luas = float("{:.2f}".format(luas))
print()
print(" {:12} | {:12}".format("Volume", "Luas"))
print("-"*30)
print(" {:12} | {:12}".format(volume, luas))