import locale

try:
    locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')
except:
    # Jika locale tidak tersedia di sistem, pakai default
    pass

print('Hutang (Rp): ')
hutang = float(input())

print('Bunga (%): ')
persen_bunga = float(input())

print('Jumlah Hari: ')
jumlah_hari = int(input())

hari = 0
while hari < jumlah_hari:
    hari = hari + 1
    hutang = hutang + (hutang * (persen_bunga / 100))

def format_rupiah(angka):
    return "Rp {:,}".format(int(angka)).replace(",", ".")

print("\n=== HASIL AKHIR ===")
print(f"bunga       : {persen_bunga}%")
print(f"hutang akhir: {format_rupiah(hutang)}")