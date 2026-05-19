def merge_sort_asc(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort_asc(arr[:mid])
    right = merge_sort_asc(arr[mid:])

    return merge_asc(left, right)


def merge_asc(left, right):

    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def merge_sort_desc(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort_desc(arr[:mid])
    right = merge_sort_desc(arr[mid:])

    return merge_desc(left, right)


def merge_desc(left, right):

    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] >= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def merge_sort_nama(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort_nama(arr[:mid])
    right = merge_sort_nama(arr[mid:])

    return merge_nama(left, right)


def merge_nama(left, right):

    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i].lower() <= right[j].lower():
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


while True:

    print("\n========== MENU MERGE SORT ==========")
    print("1. Sorting Angka Ascending")
    print("2. Sorting Angka Descending")
    print("3. Sorting Nama")
    print("4. Keluar")
    print("=====================================")

    pilihan = input("Masukkan pilihan menu: ")

    if pilihan == "1":

        jumlah = int(input("Masukkan jumlah angka: "))

        data = []

        for i in range(jumlah):
            angka = int(input("Masukkan angka ke-" + str(i + 1) + ": "))
            data.append(angka)

        hasil = merge_sort_asc(data)

        print("\nData sebelum sorting:")
        print(data)

        print("Data setelah sorting ascending:")
        print(hasil)

    elif pilihan == "2":

        jumlah = int(input("Masukkan jumlah angka: "))

        data = []

        for i in range(jumlah):
            angka = int(input("Masukkan angka ke-" + str(i + 1) + ": "))
            data.append(angka)

        hasil = merge_sort_desc(data)

        print("\nData sebelum sorting:")
        print(data)

        print("Data setelah sorting descending:")
        print(hasil)

    elif pilihan == "3":

        jumlah = int(input("Masukkan jumlah nama: "))

        nama = []

        for i in range(jumlah):
            data_nama = input("Masukkan nama ke-" + str(i + 1) + ": ")
            nama.append(data_nama)

        hasil = merge_sort_nama(nama)

        print("\nDaftar nama sebelum sorting:")
        print(nama)

        print("Daftar nama setelah sorting:")
        print(hasil)

    elif pilihan == "4":

        print("\nProgram selesai. Terima kasih.")
        break

    else:

        print("\nPilihan tidak tersedia.")