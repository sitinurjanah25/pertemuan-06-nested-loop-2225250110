while True:
    try:
        n = int(input("Masukkan bilangan positif n: "))

        if n > 0:
            break

        print("n harus lebih besar dari 0.")
    except ValueError:
        print("Masukkan bilangan bulat yang valid.")

total_semua = 0
count_genap = 0

for i in range(1, n + 1):
    total_baris = 0

    for j in range(1, n + 1):
        hasil = i * j
        print(hasil, end="\t")

        total_baris += hasil
        total_semua += hasil

        if hasil % 2 == 0:
            count_genap += 1

    print(f" | Jumlah baris: {total_baris}")

    print()
print(f"Total semua hasil: {total_semua}")
print(f"Jumlah hasil genap: {count_genap}")