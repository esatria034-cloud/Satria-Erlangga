def bubble_sort_nama(data):
    n = len(data)

    for i in range(n - 1):
        swapped = False

        for j in range(n - i - 1):
            if data[j].lower() > data[j + 1].lower():
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True

        if not swapped:
            break

    return data


while True:
    print("\n" + "=" * 50)
    print("PROGRAM PENGURUTAN NAMA PESERTA MENGGUNAKAN BUBBLE SORT")
    print("=" * 50)

    jumlah = int(input("Masukkan jumlah peserta (maksimal 20): "))

    if jumlah > 20:
        print("Jumlah peserta tidak boleh lebih dari 20 orang!")
        continue

    daftar_peserta = []

    print("\nMasukkan nama peserta:")

    for i in range(jumlah):
        nama = input(f"Peserta ke-{i+1}: ")
        daftar_peserta.append(nama)

    print("\nDaftar Nama Sebelum Diurutkan")
    print("-" * 30)

    for i, nama in enumerate(daftar_peserta, start=1):
        print(f"{i}. {nama}")

    bubble_sort_nama(daftar_peserta)

    print("\nDaftar Nama Setelah Diurutkan (A-Z)")
    print("-" * 30)

    for i, nama in enumerate(daftar_peserta, start=1):
        print(f"{i}. {nama}")

    print("\nJumlah peserta :", len(daftar_peserta))
    print("Pengurutan berhasil dilakukan menggunakan Bubble Sort.")

    ulang = input("\nApakah ingin mengurutkan data lagi? (y/t): ")

    if ulang.lower() != 'y':
        print("\nTerima kasih telah menggunakan program ini.")
        break