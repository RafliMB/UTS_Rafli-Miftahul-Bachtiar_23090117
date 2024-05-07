jumlah_barang = int(input("Masukkan jumlah barang : "))

ulang = 0
total = 0
while jumlah_barang > 0:
    harga_barang = int(input(f"Masukkan harga barang : "))
    if jumlah_barang == 0:
        break
    total += harga_barang
    jumlah_barang -= 1

print("Total Belanjaan :",f"Rp.{total:.0f}")