def selection_sort_dua_iterasi(arr):
    """
    Program untuk menampilkan
    dua iterasi pertama Selection Sort.
    """

    n = len(arr)

    print("=" * 65)
    print("          PROGRAM DUA ITERASI PERTAMA")
    print("=" * 65)
    print("Data Awal :", arr)
    print()

    for i in range(n - 1):

        min_idx = i

        print("-" * 65)
        print(f"ITERASI KE - {i + 1}")
        print("-" * 65)

        for j in range(i + 1, n):

            print(
                f"Membandingkan {arr[j]} dengan "
                f"{arr[min_idx]}"
            )

            if arr[j] < arr[min_idx]:

                min_idx = j

                print(
                    f"Nilai terkecil sementara "
                    f"menjadi {arr[min_idx]}"
                )

        print()

        if min_idx != i:

            print(
                f"Pertukaran dilakukan antara "
                f"{arr[i]} dan {arr[min_idx]}"
            )

            arr[i], arr[min_idx] = arr[min_idx], arr[i]

        else:

            print(
                "Tidak terjadi pertukaran data"
            )

        print()
        print("Array Sekarang :", arr)
        print()

        if i == 1:

            print("=" * 65)
            print("HASIL SETELAH DUA ITERASI PERTAMA")
            print("=" * 65)

            print("Elemen Terurut     :", arr[:2])
            print("Elemen Belum Urut  :", arr[2:])
            print()

            break

    return arr


data = [7, 3, 9, 1, 5]

selection_sort_dua_iterasi(data.copy())