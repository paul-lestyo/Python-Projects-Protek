bindo = int(input("Masukkan nilai Bhs Indonesia : "))
ipa   = int(input("Masukkan nilai IPA           : "))
mat   = int(input("Masukkan nilai Matematika    : "))

if(bindo >= 0) and (bindo <= 100) and (ipa >= 0) and (ipa <= 100) and (mat >= 0) and (mat <= 100):
    if(bindo >= 60) and (ipa >= 60) and (mat > 70):
        print("LULUS")
    else:
        sebab = ""
        if(bindo < 60):
            sebab += "- Nilai bahasa indonesia kurang dari 60\n"
        if(ipa < 60):
            sebab += "- Nilai IPA kurang dari 60\n"
        if(mat <= 70):
            sebab += "- Nilai Matematika kurang dari sama dengan 70\n"
        print("\nTIDAK LULUS")
        print("Sebab : ")
        print(sebab)
else:
    print("Maaf input ada yang tidak valid")

