def prima(n, pembagi=2):
    if n <= 1:
        return False
    if pembagi * pembagi > n:
        return True
    if n % pembagi == 0:
        return False
    return prima(n, pembagi + 1)

angka = int(input("Masukkan sebuah angka: "))
if prima(angka):
    print(f"{angka} adalah bilangan prima.")
else:
    print(f"{angka} bukan bilangan prima.")
