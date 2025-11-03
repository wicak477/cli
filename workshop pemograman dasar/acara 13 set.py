# Membuat Set dengan kurung kurawal
setNomor = {1, 2, 3, 4, 5}
print("setNomor =", setNomor)

# Membuat set dengan fungsi set()
setKata = set(['senin', 'selasa', 'rabu', 'kamis', 'jumat'])
print("setKata =", setKata)

# Membuat set kosong harus dengan fungsi set(), bukan dengan kurawal
setKosong = set([])
print("setKosong =", setKosong)

# Set tidak dapat berisi item yang duplikat
setDup = {7, 1, 2, 3, 6, 4, 5, 6, 3}
print("setDup =", setDup)

# Membuat set dengan tipe data campuran
setMix = {1.5, 2.5, 3.5, 'coba', (4, 5, 6)}  # tuple (4,5,6) bukan list
print("setMix =", setMix)

# Contoh error: list tidak bisa menjadi anggota set
# setList = {1.5, 2.5, 3.5, 'coba', [4,5,6]}  # <-- ini akan error

# Jalankan program dua kali untuk melihat urutan elemen set yang berubah

#buat set baru kemudian tampilkan
numSet = {1, 2, 3}
print(numSet)

#menambah item
numSet.add(4)
print(numSet)

#mengupdate item pada set, tidak akan diupdate jika ada duplikasi
numSet.update([5, 1, 6, 2, 7])
print(numSet)

#menghapus anggota set dengan discard dan remove
numSet.discard(6)
print(numSet)

numSet.remove(7)
print(numSet)
#menghapus anggota set sebelah kiri dengan pop()
numSet.pop()
print(numSet)

print(numSet.pop())
print(numSet)
#mengosongkan set menggunakan clear()
numSet.clear()
print(numSet)

a = {1, 2, 3, 4, 5} 
b = {4, 5, 6, 7, 8} 

print (a|b)
print (a.union(b))
print (b.union(a))

print (a&b)
print (a.intersection(b))
print (b.intersection(a))

print (a-b)
print (b-a)
print (a.difference(b))
print (b.difference(a))

print(a^b)
a.symmetric_difference(b)

print(b^a)
b.symmetric_difference(a)

nested = {frozenset(a), frozenset(b)}
print(nested)