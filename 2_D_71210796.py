#Program sederhana perhitungan semen untuk rumah Duni

AA = int(input("Masukkan alas atap: "))
TA = int(input("Masukkan tinggi atap: "))
T = int (input("Masukkan tinggi tembok: "))
L = (0.5*AA*TA)+(0.5*T*TA)
print ("rumah tersebut membutuhkan", L, "sak semen")