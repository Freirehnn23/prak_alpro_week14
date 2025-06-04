def kombinasi(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return kombinasi(n - 1, k - 1) + kombinasi(n - 1, k)


n = int(input("Masukkan nilai n: "))
k = int(input("Masukkan nilai k: "))
hasil = kombinasi(n, k)
print(f"Hasilnya Kombinasinya adalah {hasil}")
