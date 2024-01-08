# Dictionary berisi opsi makanan dan harganya
menu = {
    'Nasi Uduk': 10000,
    'Mie goreng telor': 9000,
    'Ayam penyet': 18000,
    'baso pentol' : 8000,
    'Es Teh': 4000,
    'Es Kopi': 5000,
    'Air Mineral': 3000
}

def tampilkan_menu():
    print("Menu Makanan/Minuman:")
    for item, harga in menu.items():
        print(f"{item}: Rp {harga}")

def hitung_total(harga, jumlah):
    return harga * jumlah

def main():
    pesanan = {}

    while True:
        tampilkan_menu()
        pilihan = input("Masukkan nama makanan/minuman yang ingin dipesan (ketik : 'sudah' untuk menampilkan struk): ")

        if pilihan.lower() == 'sudah':
            break

        if pilihan in menu:
            jumlah = int(input(f"Masukkan jumlah {pilihan}: "))
            harga_total = hitung_total(menu[pilihan], jumlah)
            pesanan[pilihan] = {'jumlah': jumlah, 'harga_total': harga_total}
        else:
            print("Menu tidak ada. Silakan pilih menu yang tersedia.")

    # Tampilkan struk pembelian
    print("\nStruk Pembelian:")
    total_pembelian = 0
    for item, detail in pesanan.items():
        print(f"{item} x{detail['jumlah']}: Rp {detail['harga_total']}")
        total_pembelian += detail['harga_total']

    print(f"\nTotal Pembelian: Rp {total_pembelian}")

if __name__ == "__main__":
    # Your code here
    # This block will be executed when the script is run directly

    main()