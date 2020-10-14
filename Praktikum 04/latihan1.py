tarifSewaPertama = 200000
tarifSewaLanjut  = 10000

rentalJamAwal      = 6
rentalJamSelesai   = 23

rentalMenitAwal    = 0
rentalMenitSelesai = 50

lamaRental = int((rentalJamSelesai - rentalJamAwal) + (rentalMenitSelesai - rentalMenitAwal) / 60)
lamaRentahLanjut = lamaRental - 12

tarifRentalLanjut = lamaRentahLanjut * tarifSewaLanjut
totalTarif = tarifSewaPertama + tarifRentalLanjut
print(totalTarif)

