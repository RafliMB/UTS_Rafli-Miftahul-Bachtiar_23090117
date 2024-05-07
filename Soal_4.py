import BMI as func

berat_badan = int(input("Masukkan berat badan (Kg)  : "))
tinggi_badan = int(input("Masukkan tinggi badan (m) : "))
hasil_bmi = berat_badan / tinggi_badan ** 2

print(f"Berat badan     : {berat_badan}")
print(f"Tinggi badan    : {tinggi_badan}")
print(f"Nilai BMI Anda  : {func.bmi()}")