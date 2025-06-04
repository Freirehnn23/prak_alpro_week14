def palindrom(kalimat):
    kalimat = ''.join(kata.lower() for kata in kalimat if kata.isalpha or kata.isdigit)

    if len(kalimat) <= 1:
        return True
    if kalimat[0] != kalimat[-1]:
        return False
    return palindrom(kalimat[1:-1])

kalimat = input("Masukkan kalimat: ")
if palindrom(kalimat):
    print("Kalimat tersebut adalah palindrom.")
else:
    print("Kalimat tersebut bukan palindrom.")
