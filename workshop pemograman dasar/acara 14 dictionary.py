mahasiswa = {
    "nama": "andi",
    "usia": "17",
    "hobi": "berenang",
    "kuliah": {
        "jurusan": "teknologi informasi",
        "prodi": "teknik komputer"
    }
}

# mengakses item pada dictionary menggunakan get
print('Nama Mahasiswa:', mahasiswa.get('nama'))

# mengakses item pada dictionary menggunakan kurung siku []
print('Usia Mahasiswa:', mahasiswa['usia'])
print('prodi Mahasiswa:', mahasiswa['kuliah']['prodi'])

# mengakses item pada dictionary menggunakan fungsi berantai untuk dictionary bertingkat
print('Jurusan Mahasiswa:', mahasiswa.get('kuliah').get('jurusan'))

# menampilkan isi dictionary menggunakan perulangan 
for key in mahasiswa:
    print(key, '=', mahasiswa[key])

# mengubah nilai item
print('Nama Awal:', mahasiswa.get('nama'))
mahasiswa['nama'] = 'andi brian'
print('Nama setelah diubah:', mahasiswa.get('nama'))

# menambah item 
print('Alamat:', mahasiswa.get('alamat'))
mahasiswa['Alamat'] = 'Jember'
print('Mahasiswa {} beralamat di {}' .format(
    mahasiswa.get('nama'),
    mahasiswa.get('Alamat')
))

# menghapus item 
del mahasiswa['nama']
print('Nama Mahasiswa:', mahasiswa.get('nama'))

mahasiswa.pop('usia')
print('Usia Mahasiswa:', mahasiswa.get('usia'))

usia = mahasiswa.pop('usia')
print('usia mahasiswa:', usia)
