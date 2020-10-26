bindo = int(input("Masukkan nilai Bhs Indonesia : "))
ipa   = int(input("Masukkan nilai IPA           : "))
mat   = int(input("Masukkan nilai Matematika    : "))


if(bindo >= 0) and (bindo <= 100) and (ipa >= 0) and (ipa <= 100) and (mat >= 0) and (mat <= 100):
    if(bindo >= 60) and (ipa >= 60) and (mat > 70):
        print("LULUS")
    else:
        print("TIDAK LULUS")
else:
    print("Maaf input ada yang tidak valid")

