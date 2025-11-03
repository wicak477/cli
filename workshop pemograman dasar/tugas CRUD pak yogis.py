# Program CRUD Data Mahasiswa

mahasiswa = []  # list untuk menyimpan data mahasiswa


def tampilkan_data():
    print("\n=== DATA MAHASISWA ===")
    if len(mahasiswa) == 0:
        print("Belum ada data.")
    else:
        print(f"{'No':<4}{'NIM':<15}{'Nama':<25}{'Jurusan'}")
        print("-" * 60)
        for i, mhs in enumerate(mahasiswa, start=1):
            print(f"{i:<4}{mhs['nim']:<15}{mhs['nama']:<25}{mhs['jurusan']}")


def tambah_data():
    print("\n=== TAMBAH DATA MAHASISWA ===")
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    jurusan = input("Masukkan Jurusan: ")
    mahasiswa.append({"nim": nim, "nama": nama, "jurusan": jurusan})
    print("✅ Data berhasil ditambahkan!")


def ubah_data():
    tampilkan_data()
    if len(mahasiswa) == 0:
        return
    try:
        print("\nKetik 0 untuk batal dan kembali ke menu utama.")
        indeks = int(input("Masukkan nomor data yang ingin diubah: ")) - 1

        if indeks == -1:
            print("❌ Ubah data dibatalkan.")
            return

        if 0 <= indeks < len(mahasiswa):
            print("\nMasukkan data baru (kosongkan jika tidak ingin diubah):")
            nim_baru = input("NIM baru: ")
            nama_baru = input("Nama baru: ")
            jurusan_baru = input("Jurusan baru: ")

            if nim_baru:
                mahasiswa[indeks]['nim'] = nim_baru
            if nama_baru:
                mahasiswa[indeks]['nama'] = nama_baru
            if jurusan_baru:
                mahasiswa[indeks]['jurusan'] = jurusan_baru

            print("✅ Data berhasil diubah!")
        else:
            print("Nomor tidak valid!")
    except ValueError:
        print("Input harus berupa angka!")


def hapus_data():
    tampilkan_data()
    if len(mahasiswa) == 0:
        return
    try:
        indeks = int(input("\nMasukkan nomor data yang ingin dihapus (0 untuk batal): ")) - 1
        if indeks == -1:
            print("❌ Penghapusan dibatalkan.")
            return
        if 0 <= indeks < len(mahasiswa):
            terhapus = mahasiswa.pop(indeks)
            print(f"🗑️ Data {terhapus['nama']} berhasil dihapus!")
        else:
            print("Nomor tidak valid!")
    except ValueError:
        print("Input harus berupa angka!")


# === MENU UTAMA ===
while True:
    print("\n===== MENU CRUD DATA MAHASISWA =====")
    print("1. Tambah Data")
    print("2. Ubah Data")
    print("3. Hapus Data")
    print("4. Tampilkan Data")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        tambah_data()
    elif pilihan == "2":
        ubah_data()
    elif pilihan == "3":
        hapus_data()
    elif pilihan == "4":
        tampilkan_data()
    elif pilihan == "5":
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")
