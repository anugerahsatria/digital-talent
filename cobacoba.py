hargaBuku= int (input("Masukkan harga buku: " ))
diskon = 0.4
ongkirPertama= 9000
ongkirKedua = 3000
eksemplar= 60
hargaDiskon =  hargaBuku *  diskon
print("hargaDiskon", hargaDiskon)

hargaAsli= int (hargaBuku) - int (hargaDiskon) 
hargaOngkir = int (ongkirPertama) + int (ongkirKedua)* 59
