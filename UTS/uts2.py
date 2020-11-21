def jarak_per_detik(v0,a):
    t = 1
    while (t <= 10):
        hasil_per_detik = (v0 * t) + (a*t**2/2)
        print("t = ",t,"    S(t) = ",hasil_per_detik)
        t += 1

kec_mula   = int(input("Masukkan kecepatan mula-mula : "))
percepatan = int(input("Masukkan percepatan          : "))

jarak_per_detik(kec_mula,percepatan)
