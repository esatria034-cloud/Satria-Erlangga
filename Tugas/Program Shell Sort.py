def shell_sort_nama(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap].lower() > temp.lower():
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        gap //= 2


def tampilkan_proses(arr, gap, langkah):
    print(f"\n  [Langkah {langkah}] Gap = {gap}")
    print(f"  Array saat ini : {arr}")


def shell_sort_dengan_proses(arr):
    n = len(arr)
    gap = n // 2
    langkah = 1

    print("\n  *** Detail Proses Pengurutan ***")
    print(f"  Array awal     : {arr}")

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap].lower() > temp.lower():
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        tampilkan_proses(arr, gap, langkah)
        langkah += 1
        gap //= 2


def validasi_nama(nama):
    if len(nama) == 0:
        return False, "Nama tidak boleh kosong."
    if any(char.isdigit() for char in nama):
        return False, "Nama tidak boleh mengandung angka."
    if len(nama) < 2:
        return False, "Nama terlalu pendek, minimal 2 karakter."
    return True, ""


def input_nama():
    print("\n" + "=" * 55)
    print("       PROGRAM PENGURUTAN NAMA SECARA ALFABETIS")
    print("          Menggunakan Algoritma Shell Sort")
    print("=" * 55)

    print("\n  Petunjuk Penggunaan:")
    print("  - Masukkan nama satu per satu lalu tekan Enter")
    print("  - Nama tidak boleh mengandung angka")
    print("  - Minimal masukkan 3 nama untuk diurutkan")
    print("  - Ketik 'selesai' jika sudah selesai input nama")
    print("-" * 55)

    daftar_nama = []

    while True:
        nama_input = input(f"\n  Masukkan nama ke-{len(daftar_nama) + 1} : ").strip()

        if nama_input.lower() == "selesai":
            if len(daftar_nama) < 3:
                print(f"\n  [!] Anda baru memasukkan {len(daftar_nama)} nama.")
                print("  [!] Minimal masukkan 3 nama sebelum mengetik 'selesai'.")
                continue
            break

        valid, pesan = validasi_nama(nama_input)

        if not valid:
            print(f"\n  [!] Input tidak valid : {pesan}")
            print("  [!] Silakan masukkan nama yang benar.")
            continue

        nama_formatted = nama_input.title()

        if nama_formatted in daftar_nama:
            print(f"\n  [!] Nama '{nama_formatted}' sudah ada dalam daftar.")
            print("  [!] Silakan masukkan nama yang berbeda.")
            continue

        daftar_nama.append(nama_formatted)
        print(f"  [✓] Nama '{nama_formatted}' berhasil ditambahkan.")
        print(f"  [i] Total nama yang dimasukkan : {len(daftar_nama)}")

    return daftar_nama


def tampilkan_hasil_akhir(nama_sebelum, nama_sesudah):
    print("\n" + "=" * 55)
    print("               HASIL PENGURUTAN NAMA")
    print("=" * 55)

    print("\n  Daftar Nama SEBELUM Diurutkan :")
    print("  " + "-" * 35)
    for i, nama in enumerate(nama_sebelum, 1):
        print(f"  {i}. {nama}")

    print("\n  Daftar Nama SESUDAH Diurutkan (Alfabetis) :")
    print("  " + "-" * 35)
    for i, nama in enumerate(nama_sesudah, 1):
        print(f"  {i}. {nama}")

    print("\n" + "=" * 55)
    print("  Pengurutan selesai! Nama telah tersusun alfabetis.")
    print("=" * 55)


def cari_nama(daftar, kata_kunci):
    hasil = []
    for nama in daftar:
        if kata_kunci.lower() in nama.lower():
            hasil.append(nama)
    return hasil


def fitur_pencarian(daftar_terurut):
    print("\n" + "-" * 55)
    print("  FITUR PENCARIAN NAMA")
    print("-" * 55)

    while True:
        pilihan = input("\n  Apakah ingin mencari nama tertentu? (ya/tidak) : ").strip().lower()

        if pilihan == "tidak":
            print("\n  Terima kasih telah menggunakan program ini!")
            break

        elif pilihan == "ya":
            kata_kunci = input("  Masukkan nama atau huruf yang dicari : ").strip()

            if len(kata_kunci) == 0:
                print("  [!] Kata kunci tidak boleh kosong.")
                continue

            hasil_cari = cari_nama(daftar_terurut, kata_kunci)

            if len(hasil_cari) == 0:
                print(f"\n  [!] Nama dengan kata kunci '{kata_kunci}' tidak ditemukan.")
            else:
                print(f"\n  [✓] Ditemukan {len(hasil_cari)} nama dengan kata kunci '{kata_kunci}' :")
                for i, nama in enumerate(hasil_cari, 1):
                    print(f"      {i}. {nama}")

        else:
            print("  [!] Pilihan tidak valid. Ketik 'ya' atau 'tidak'.")


def tampilkan_statistik(daftar_nama):
    print("\n" + "-" * 55)
    print("  STATISTIK DAFTAR NAMA")
    print("-" * 55)
    print(f"  Total nama yang diurutkan  : {len(daftar_nama)} nama")
    print(f"  Nama paling awal (A)       : {daftar_nama[0]}")
    print(f"  Nama paling akhir (Z)      : {daftar_nama[-1]}")

    panjang_nama = [(nama, len(nama)) for nama in daftar_nama]
    nama_terpanjang = max(panjang_nama, key=lambda x: x[1])
    nama_terpendek = min(panjang_nama, key=lambda x: x[1])

    print(f"  Nama terpanjang            : {nama_terpanjang[0]} ({nama_terpanjang[1]} karakter)")
    print(f"  Nama terpendek             : {nama_terpendek[0]} ({nama_terpendek[1]} karakter)")


if __name__ == "__main__":

    daftar_nama_input = input_nama()

    nama_sebelum_diurutkan = daftar_nama_input.copy()

    pilihan_proses = input("\n  Tampilkan detail proses pengurutan? (ya/tidak) : ").strip().lower()

    if pilihan_proses == "ya":
        shell_sort_dengan_proses(daftar_nama_input)
    else:
        shell_sort_nama(daftar_nama_input)

    tampilkan_hasil_akhir(nama_sebelum_diurutkan, daftar_nama_input)

    tampilkan_statistik(daftar_nama_input)

    fitur_pencarian(daftar_nama_input)