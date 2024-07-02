import json
import os

library = []

def load_library():
    if os.path.exists('library.json'):
        with open('library.json', 'r') as file:
            return json.load(file)
    return []

def save_library():
    with open('library.json', 'w') as file:
        json.dump(library, file)

def add_book():
    # Fungsi untuk menambahkan buku ke dalam perpustakaan
    title = input('Masukkan judul buku: ')
    author = input('Masukkan nama penulis: ')
    year = input('Masukkan tahun terbit: ')
    
    book = {"title": title, "author": author, "year": year}
    library.append(book)
    save_library()
    print(f'Buku "{title}" berhasil ditambahkan ke perpustakaan')

def search_books(keyword):
    results = []
    for book in library:
        if (keyword.lower() in book['title'].lower() or
            keyword.lower() in book['author'].lower() or
            keyword in book['year']):
            results.append(book)
    return results

def display_books(books):
    if not books:
        print('Tidak ada buku yang ditemukan.')
    else:
        print('Buku yang ditemukan:')
        for book in books:
            print(f"Judul: {book['title']}, Penulis: {book['author']}, Tahun: {book['year']}")

def main():
    global library
    library = load_library()
    while True:
        print('\nMenu Perpustakaan:')
        print('1. Tambah Buku')
        print('2. Cari Buku')
        print('3. Lihat Semua Buku')
        print('4. Keluar')
        choice = input('Pilih menu (1/2/3/4): ')
        
        if choice == '1':
            add_book()
        elif choice == '2':
            keyword = input('Masukkan kata kunci yang ingin dicari: ')
            results = search_books(keyword)
            display_books(results)
        elif choice == '3':
            display_books(library)
        elif choice == '4':
            print('Terima kasih telah mengunjungi perpustakaan saya')
            break
        else:
            print('Input tidak valid')

if __name__ == "__main__":
    main()