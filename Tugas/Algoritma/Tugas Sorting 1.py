def selection_sort_ascending_detail(arr):
    """
    Program Selection Sort Ascending
    dengan tampilan langkah yang lebih detail
    dan menarik di terminal.
    """

    n = len(arr)

    print("=" * 65)
    print("         PROGRAM SELECTION SORT ASCENDING")
    print("=" * 65)
    print("Data Awal :", arr)
    print()

    for i in range(n - 1):

        min_idx = i

        print("-" * 65)
        print(f"ITERASI KE - {i + 1}")
        print("-" * 65)

        print("Bagian Terurut      :", arr[:i])
        print("Bagian Belum Terurut:", arr[i:])
        print()

        print(f"Mencari nilai terkecil dari indeks {i} sampai {n - 1}")
        print()

        for j in range(i + 1, n):

            print(
                f"Membandingkan {arr[j]} dengan "
                f"{arr[min_idx]}"
            )

            if arr[j] < arr[min_idx]:
                min_idx = j
                print(
                    f"Nilai terkecil baru ditemukan "
                    f"yaitu {arr[min_idx]}"
                )

        print()
        print(
            f"Elemen terkecil pada iterasi ini "
            f"adalah {arr[min_idx]}"
        )

        if min_idx != i:

            print(
                f"Menukar {arr[i]} dengan "
                f"{arr[min_idx]}"
            )

            arr[i], arr[min_idx] = arr[min_idx], arr[i]

        else:
            print(
                f"{arr[i]} sudah berada "
                f"di posisi yang benar"
            )

        print()
        print("Hasil sementara :", arr)
        print()

    print("=" * 65)
    print("HASIL AKHIR PENGURUTAN ASCENDING")
    print("=" * 65)
    print(arr)
    print("=" * 65)

    return arr


data = [80, 10, 50, 70, 60, 20]

selection_sort_ascending_detail(data.copy())