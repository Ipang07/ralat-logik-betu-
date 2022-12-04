#menu
def menu():
    print("\n" +("*"*46))
    print("\tMenu Mengira Isi padu dan Luas")
    print("*"*46)
    print("1. Luas")
    print("2. Isipadu")
    print("3. Tamat")
    print("\n"+("*"*46))
    return 3


#menu isipadu
def menuIsipadu():
    print("\n" +("*"*46))
    print("Menu Mengira Isi padu")
    print("*"*46)
    print("1. Kuboid")
    print("2. Silinder")
    print("3. Kon")
    print("4. Sfera")
    print("\n" +("*"*46))
    return 4


#menu luas
def menuLuas():
    print("\n" +("*"*46))
    print("Menu Mengira Luas")
    print("*"*46)
    print("1. Segi empat tepat")
    print("2. Segi tiga")
    print("3. Trapezium")
    print("4. Bulatan")
    print("\n" +("*"*46))
    return 4


#Menerima pilihan pengguna
def dptPilihan(bil_pilihan):
    no_pilihan = 0
    pilihan = range(1, bil_pilihan + 1)
    while no_pilihan not in pilihan:
            no_pilihan = int(input(f"Pilihan anda [{pilihan[0]} - {pilihan[-1]}] : ___ "))
    return no_pilihan


def dptFormula(pilihan):
    pil1, pil2 = pilihan
    if pil1 == 1:
        if pil2 == 1:
            return ["panjang*lebar", ["panjang", "lebar"]]
        elif pil2 == 2:
            return ["(1/2)*tapak*tinggi", ["tapak", "tinggi"]]
        elif pil2 == 3:
            return ["(1/2)*(panjang sisi pertama+panjang sisi kedua)*tinggi", ["panjang sisi pertama", "panjang sisi kedua", "tinggi"]]
        elif pil2 == 4:
            return ["pi*jejari**2", ["jejari"]]
    elif pil1 == 2:
        if pil2 == 1:
            return ["panjang*tapak**tinggi", ["panjang", "tapak", "tinggi"]]
        elif pil2 == 2:
            luas_tapak = "pi*jejari**2"
            return [f"{luas_tapak}*tinggi", ["jejari", "tinggi"]]
        elif pil2 == 3:
            luas_tapak = "pi*jejari**2"
            return [f"(1/3)*{luas_tapak}*tinggi", ["jejari", "tinggi"]]
        elif pil2 ==4:
            return ["(4/3)*pi*jejari**3", ["jejari"]]


    
#Menerima nombor
def dptNilai(pilihan):
    formula, PU = dptFormula(pilihan)
    if pilihan[0] == 1:
        jenis_opr = "Luas"
    elif pilihan[0] == 2:
        jenis_opr = "Isi padu"
    for i in PU:
        formula = formula.replace(i, input(f"Masukkan {i}:"))
    return formula , jenis_opr

#Kira dan Cetak
def KiraCetak(formula, jenis_opr):
    pi = 3.142
    print(jenis_opr ,"ialah", eval(formula), "\n")


while True:
    pilihan = []
    pilihan.append(dptPilihan(menu()))
    if pilihan[0] == 1:
         pilihan.append(dptPilihan(menuLuas()))
    elif pilihan[0] == 2:
         pilihan.append(dptPilihan(menuIsipadu()))
    elif pilihan[0] == 3:
        print("\n" +("*"*46))
        print("Terima Kasih kerana menggunakan atur cara ini.")
        print("*"*46)
        exit()
    nilai = dptNilai(pilihan)
    KiraCetak(nilai[0], nilai[1])
