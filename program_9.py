# contoh masalah 1; menghitung gaji karyawan dengan bonus

# input data
nilai_kinerja = "baik"
tahun_bekerja = 6
gaji_pokok = 5000000

# percabangan bersarang untuk menghitung bonus
if nilai_kinerja == "baik":
    if tahun_bekerja > 5:
        bonus = 0.1 * gaji_pokok 
    else: 
        bonus = 0
elif nilai_kinerja == "cukup":
     if tahun_bekerja > 3:
         bonus = 0.05 * gaji_pokok
     else: 
         bonus = 0
else: 
    bonus = 0 
    
# Hitung gaji total
total_gaji = gaji_pokok + bonus

#output
print("gaji pokok;", gaji_pokok)
print("bonus:", bonus)
print("total gaji:", total_gaji)
