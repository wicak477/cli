# Membuat list kosong
listKosong = []

# Membuat list berisi 1 item
listSatuItem = ['satuItem']

# Membuat list dengan banyak item dengan satu tipe data
listKata = ["mangga", "jambu", "apel", "anggur"]
listAngka = [23, 11, 94]

# Membuat list dengan berbagai tipe data
listMix = [23, "November", 94]

# Membuat list berisi list (list bersarang)
listNested = ["Mahasiswa", ["Dian", 17, 160.5], "Lulus"]
listGabungan = [listKata, listAngka]

# Mencetak List
print(listKosong)
print(listSatuItem)
print(listKata)
print(listAngka)
print(listMix)
print(listNested)
print(listGabungan)

print(listKata[0])
print(listKata[1])
print(listKata[2])
print(listKata[3])

print(listKata[-0])
print(listKata[-1])
print(listKata[-2])
print(listKata[-3])

print(listKata[0])
print(listKata[1])
print(listKata[1][0])
print(listKata[1][1])
print(listKata[1][2])
print(listKata[2])

listKata = ["mangga", "jambu", "apel", "anggur"]

print(listKata[0:1])
print(listKata[0:2])
print(listKata[0:3])
print(listKata[0:4])
print(listKata[0:-1])
print(listKata[-3:-1])
print(listKata[-4:-3])
print(listKata[-3::-1])

asd = ['nol', 'satu', 'dua', 'tiga', 'empat', 'mintiga', 'mindua', 'minsatu']

print(asd[1:3])
print(asd[0:-1])
print(asd[-1:-3])
print(asd[-1:3])
print(asd[-3::-1])
print(asd[-4::-1])
print(asd[-4:-2])

listKata = ["mangga", "jambu", "apel", "anggur"]

print(listKata[0:])
print(listKata[1:])
print(listKata[2:])
print(listKata[3:])
print(listKata[:0])
print(listKata[:1])
print(listKata[:2])
print(listKata[:3])
print(listKata[:4])
print()
print(listKata[-1:])
print(listKata[-2:])
print(listKata[-3:])
print(listKata[:0])
print(listKata[:-1])
print(listKata[:-2])
print(listKata[:-3])
print(listKata[:-4])

listKata = ["mangga", "jambu", "apel", "anggur"]
print(listKata)

# Mengubah indeks ke 1
print('Sesudah indeks ke 1 diubah :')
listKata[1] = "rambutan"
print(listKata)

# Menambah list pada listKata tetapi tidak disimpan
print('List juga bisa ditambahkan :')
print(listKata + ["delima", "melon", "pear"])

# Menambah list pada listKata lalu disimpan
print('List juga bisa ditambahkan kemudian disimpan :')
listKata = listKata + ["delima", "melon", "pear"]
print(listKata)

# Mengalikan list
print('List juga bisa dikalikan :')
print(listKata * 2)

# Memeriksa item dalam list
print("mangga" in listKata)
print("salak" not in listKata)
if "melon" in listKata:
    print("ada melon di dalam listKata")

nomor = [1, 5, 7, 9, 11]

# Menghitung jumlah item
print('Menghitung jumlah item pada list:')
print(len(nomor))

# Menambahkan item di akhir list
print('Menambah angka 13 menggunakan append:')
nomor.append(13)
print(nomor)

# Menyisipkan item pada indeks tertentu
print('Menyisipkan angka 3 pada indeks ke-1 menggunakan insert:')
indeks = 1
nomor.insert(indeks, 3)
print(nomor)

# Menambah list menggunakan extend
print('Menambah list berisi 15, 17, 19 pada list nomor:')
nomor.extend([15, 17, 19])
print(nomor)

# Cek indeks ke berapa
print('Cek angka 1 di indeks ke berapa? angka 2 di indeks ke berapa?')
print(nomor.index(1))



listHari = ['hari', 'senin', 'selasa', 'maret', 'rabu', 'kamis', 'juni']
print(listHari)

# remove
print('Menghapus maret dari list :')
listHari.remove('maret')
print(listHari)

# del
print('Menghapus indeks ke 0 yaitu hari :')
del listHari[0]
print(listHari)

# pop dengan indeks
print('Menghapus indeks ke 4 yaitu juni menggunakan pop :')
listHari.pop(4)
print(listHari)

# pop terakhir
print('Menghapus indeks terakhir (kamis) menggunakan pop :')
listHari.pop()
print(listHari)

# mencetak nilai yang dihapus
print('Mencetak nilai yang dihapus pop pada indeks ke 0 yaitu senin :')
print(listHari.pop(0))

listAngka = [3, 5, 8, 1, 2, 9, 7, 4, 6]
listHuruf = ['doni', 'caca', 'eva', 'bobi', 'ani', 'faruk']
print(listAngka)
print(listHuruf)

# sort
print('Marilah kita urutkan :')
listAngka.sort()
listHuruf.sort()
print(listAngka)
print(listHuruf)

# reverse
print('Membalik urutan indeks :')
listAngka.reverse()
listHuruf.reverse()
print(listAngka)
print(listHuruf)

list_minuman = [
    ["Kopi", "Susu", "Teh"],
    ["Jus Apel", "Jus Melon", "Jus Jeruk"],
    ["Es Kopi", "Es Campur", "Es Teler"]
]

print(list_minuman)
print('\n')

# Mengakses list multidimensi
print("Menampilkan salah satu menu dengan menunjuk nomor indeks :")
print(list_minuman[2][0])
print(list_minuman[0][1])
print('\n')

# Menampilkan isi list satu per satu
print("Menampilkan isi list :")
for menu in list_minuman:
    print(menu)

# Menampilkan isi list di dalam list satu per satu
print('\nMenampilkan isi list di dalam list :')
for menu in list_minuman:
    for menu2 in menu:
        print(menu2)
