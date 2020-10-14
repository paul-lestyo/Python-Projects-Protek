kotaA_ke_B = 125
kecepatanKotaA_ke_B = 62

kotaB_ke_C = 256
kecepatanKotaB_ke_C = 70

waktuJamKotaA_ke_B   = kotaA_ke_B // kecepatanKotaA_ke_B
waktuMenitKotaA_ke_B = round((kotaA_ke_B % kecepatanKotaA_ke_B) / kecepatanKotaA_ke_B * 60)

waktuJamkotaB_ke_C = kotaB_ke_C // kecepatanKotaB_ke_C
waktuMenitKotaB_ke_C = round((kotaB_ke_C % kecepatanKotaB_ke_C) / kecepatanKotaB_ke_C * 60)

waktuJamBerangkat   = 6
waktuMenitBerangkat = 0 

waktuMenitRehat = 45

waktuJamSampai   = (waktuJamBerangkat + waktuJamKotaA_ke_B + waktuJamkotaB_ke_C)
waktuMenitSampai = (waktuMenitBerangkat + waktuMenitKotaA_ke_B + waktuMenitKotaB_ke_C + waktuMenitRehat)

if (waktuMenitSampai >= 60):
    waktuJamSampai += 1
    waktuMenitSampai -= 60

print("Waktu sampai yaitu %d.%d" % (waktuJamSampai,waktuMenitSampai))


