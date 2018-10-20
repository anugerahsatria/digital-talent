hargabuku = input("Masukkan harga terbaru buku: ")
diskon = input ("Masukkan diskon toko: ")

hargaawal=  int (hargabuku) * float (diskon)

hargaakhir = int ((hargaawal) + 9000) + int(((hargaawal) + 3000) *59)   
print('Harga untuk pengiriman 60 eksemplar adalah: ', hargaakhir)
