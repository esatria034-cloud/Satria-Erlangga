def selection_sort_string(arr):
    """
    Program Selection Sort
    untuk data string atau teks.
    """

    n = len(arr)

    print("=" * 65)
    print("          PROGRAM SELECTION SORT STRING")
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
                f"Membandingkan "
                f"{arr[j]} dengan {arr[min_idx]}"
            )

            if arr[j] < arr[min_idx]:

                min_idx = j

                print(
                    f"Urutan alfabet lebih kecil "
                    f"ditemukan yaitu {arr[min_idx]}"
                )

        print()

        if min_idx != i:

            print(
                f"Menukar {arr[i]} "
                f"dengan {arr[min_idx]}"
            )

            arr[i], arr[min_idx] = arr[min_idx], arr[i]

        else:

            print(
                f"{arr[i]} sudah berada "
                f"di posisi alfabet yang benar"
            )

        print()
        print("Hasil sementara :", arr)
        print()

    print("=" * 65)
    print("HASIL AKHIR PENGURUTAN STRING")
    print("=" * 65)

    print(arr)

    print("=" * 65)

    return arr


buah = [
    "Mangga",
    "Apel",
    "Durian",
    "Jeruk",
    "Pisang",
    "Anggur"
]

selection_sort_string(buah.copy())