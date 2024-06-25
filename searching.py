def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

def main_binary_search():
    arr = list(map(int, input("Masukkan daftar elemen yang sudah terurut (pisahkan dengan spasi): ").split()))
    x = int(input("Masukkan elemen yang akan dicari: "))
    result = binary_search(arr, x)

    if result != -1:
        print(f"Elemen ditemukan pada indeks {result}")
    else:
        print("Elemen tidak ditemukan dalam daftar")

def sequential_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def main_sequential_search():
    pasien_harian = input("Masukkan daftar nama pasien yang datang pada hari ini (pisahkan dengan koma): ").split(",")
    nama_cari = input("Masukkan nama pasien yang akan dicari: ").strip()
    result = sequential_search(pasien_harian, nama_cari)

    if result != -1:
        print(f"Pasien ditemukan pada indeks {result}")
    else:
        print("Pasien tidak ditemukan dalam daftar")

def tugas_binary_ppt():
    # Implementasi spesifik untuk tugas binary ppt
    arr = list(map(int, input("Masukkan daftar elemen yang sudah terurut (pisahkan dengan spasi): ").split()))
    x = int(input("Masukkan elemen yang akan dicari: "))
    result = binary_search(arr, x)

    if result != -1:
        print(f"Elemen ditemukan pada indeks {result}")
    else:
        print("Elemen tidak ditemukan dalam daftar")

def main():
    while True:
        print("\nMenu Pencarian")
        print("1. Binary Search (Pencarian Biner)")
        print("2. Sequential Search (Pencarian Linier)")
        print("3. Tugas Binary PPT")
        print("4. Keluar")

        pilihan = input("Pilih jenis pencarian (1/2/3/4): ")

        if pilihan == '1':
            main_binary_search()
        elif pilihan == '2':
            main_sequential_search()
        elif pilihan == '3':
            tugas_binary_ppt()
        elif pilihan == '4':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
