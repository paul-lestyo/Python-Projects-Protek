from operation import *


print('2 + 4 * 6 - 4', '=', kurang(jumlah(2,kali(4,6)),4))
print('(4 + 7) * (6 - 9)', '=', kali(jumlah(4,7),kurang(6,9)))
print('(10 + 2) / (7 + 5) / (12 - 34)','=',bagi(bagi(jumlah(10,2),jumlah(7,5)),kurang(12,34)))