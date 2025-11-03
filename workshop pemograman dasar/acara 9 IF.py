angka = int(input('masukkan sebuah angka :'))

if(angka > 3):
    print('angka yang diinputkan lebih dari 3')
print('bagian ini akan selalu di tampilkan')

if(angka <= 3):
    print('angka yang diinputkan sama atau kurang dari 3')
print('bagian ini juga akan selalu ditampilkan')

usia = int(input("Masukkan usia anda : "))

if (usia >= 17):
    print("Kamu boleh membuat SIM")
else:
    print("Kamu belum boleh membuat SIM")
bilangan = int(input('masukkan sebuah bilangan :'))

if bilangan > 0:
    print("Bilangan yang anda input adalah bilangan positif")
elif bilangan == 0:
    print("Nol")
else:
    print("Bilangan yang anda input adalah bilangan negatif")

hari_ini = input('masukkan nama hari :')

if(hari_ini == "senin"):
    print("Saya akan kuliah")
elif(hari_ini == "selasa"):
    print("Saya akan kuliah")
elif(hari_ini == "rabu"):
    print("Saya akan kuliah")
elif(hari_ini == "kamis"):
    print("Saya akan kuliah")
elif(hari_ini == "jumat"):
    print("Saya akan kuliah")
elif(hari_ini == "sabtu"):
    print("Saya akan libur")
elif(hari_ini == "minggu"):
    print("Saya akan libur")
else:
    print("""inputan hanya boleh menggunakan huruf kecil,
atau yang anda inputkan bukan merupakan nama hari""")

try:
    usia = int(input('masukkan usia anda :'))

    if (usia >= 17):
        kerja = input('apakah anda sudah bekerja atau masih kuliah? (kerja/kuliah) ')
        if kerja == "kerja":
            print("Anda sudah memiliki penghasilan")
        elif kerja == "kuliah":
            print("Semangat menjalani kuliah")
        else:
            print("Yang anda masukkan salah")
    elif (4 < usia < 17):
        print("Anda adalah seorang siswa")
    else:
        print("Anda adalah balita")

except:
    print("Yang anda masukkan bukan angka")
