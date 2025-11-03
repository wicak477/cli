tupleKosong = ()
tupleSingleton = ('satu',)
tupleSingleton2 = (1,)
tupleSingleton3 = 'satu',
tupleBulan = ('Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni')
#tuple bisa dibuat tanpa tanda kurung
tupleAngka = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

print(tupleKosong)
print(tupleSingleton)
print(tupleSingleton2)
print(tupleSingleton3)
print(tupleBulan)
print(tupleAngka)

print('\n')
#Cek tipe data. apakah sudah benar bertipe data tuple?
print(type(tupleSingleton))
print(type(tupleSingleton2))
print(type(tupleSingleton3))
print(type(tupleAngka))

#menggabungkan 2 tuple menjadi 1
tupleGap = tupleSingleton3 + tupleAngka
print(tupleGap)

#mengakses data tuple
print(tupleBulan[0])
print(tupleBulan[3])
print(tupleBulan[5])
print(tupleAngka[-1])
print(tupleAngka[-3])
print(tupleAngka[-5])

tupleAngka = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

#slicing tuple
print(tupleAngka[0:3])
print(tupleAngka[1:-1]) #memotong indeks ke 1 hingga -1
print(tupleAngka[1:-1])
print('\n')

#slicing tanpa batas
print(tupleAngka[2:])
print(tupleAngka[5:])
print(tupleAngka[8:])
print(tupleAngka[:0])
print(tupleAngka[:1])
print(tupleAngka[:3])
print(tupleAngka[:5])

tupleAngka = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

#indeks kelipatan
#dari indeks awal hingga akhir, kelipatan indeks 2 langkah
print(tupleAngka[::2])
#dari indeks 1 hinngga -8, kelipatan indeks 3 langkah
print(tupleAngka[1:3:8])


tuple1 = (1, 2, 3)
tuple2 = ('satu', 'dua', 'tiga')
tuple3 = ('jalu', 23, 68.5)
tuple4 = (tuple1, tuple2, tuple3)

print(tuple1)
print(tuple2)
print(tuple3)
print(tuple4)
print(tuple4[1][2])
print(tuple4[2][0])

nama, usia, berat = tuple3
print('nama: ', nama)
print('usia: ', usia)
print('berat: ', berat)

print(max(tuple1))
print(min(tuple1))
print(len(tuple1))

tupleBulan = ('Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni')
for month in tupleBulan:
    print(month)