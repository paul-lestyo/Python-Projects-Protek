bindo = int(input("Masukkan nilai Bhs Indonesia : "))
ipa   = int(input("Masukkan nilai IPA           : "))
mat   = int(input("Masukkan nilai Matematika    : "))


if(bindo >= 60) and (mat >= 60) and (mat > 70):
    print("LULUS")
else:
    print("TIDAK LULUS")