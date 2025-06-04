def jumlah_digit_rekursif(n):
    if n < 10:
        return n
    else:
        return n % 10 + jumlah_digit_rekursif(n // 10)

try:
    angka = int(input("Masukkan bilangan: "))
    hasil = jumlah_digit_rekursif(angka)
    print(f"Jumlah digit dari {angka} adalah {hasil}")
except ValueError:
    print("Masukkan bilangan bulat yang valid.")