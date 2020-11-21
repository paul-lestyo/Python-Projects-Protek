def hitung_BMI(bb,tb):
    return bb/(tb*tb)

def cek_status_BMI(bmi):
    if(bmi >= 35): 
        return "OBESITAS MORBID"
    elif(bmi >= 27):
        return "OBESITAS"
    elif(bmi >= 23):
        return "GEMUK"
    elif(bmi >= 18):
        return "IDEAL"
    else:
        return "KURUS"

berat  = int(input("Masukkan berat badan (Kg)  :"))
tinggi = int(input("Masukkan tinggi badan (cm) : "))

if(berat > 0) and (tinggi > 0):
    bmi = hitung_BMI(berat,tinggi/100)
    print("Status berat badan anda adalah", cek_status_BMI(bmi))
else:
    print("Input yang dimasukkan tidak valid")


