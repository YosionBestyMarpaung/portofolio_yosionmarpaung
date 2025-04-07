"""
Nama: Yosion Besty Marpaung - 23091397168
Kelas: 2023E
Prodi: D4 Manajemen Informatika

"""
class Node:
    def __init__(self, menu, harga):
        self.menu = menu
        self.harga = harga
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def tambah_pesanan(self, menu, harga):
        new_node = Node(menu, harga)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
def tampilkan_pesanan(self):
        current = self.head
        if not current:
            print("Keranjang masih kosong")
        else:
            index = 1
            while current:
                print(f"{index}. {current.menu} {current.harga} rupiah")
                current = current.next
                index += 1

    def total_harga(self):
        current = self.head
        total = 0
        while current:
            total += current.harga
            current = current.next
        return total
# Menu Miexue dan Harganya
menu_miexue = {
    "Miexue Ice Cream": 5000,
    "Boba Shake": 16000,
    "Mi Sundae": 14000,
    "Mi Ganas": 11000,
    "Creamy Mango Boba": 22000
}

# Membuat instance dari linked list
keranjang = LinkedList()

# Contoh penggunaan
keranjang.tambah_pesanan("Miexue Ice Cream", menu_miexue["Miexue Ice Cream"])
keranjang.tambah_pesanan("Mi Ganas", menu_miexue["Mi Ganas"])
print("miexue ice cream sudah ditambahkan ke keranjang")
print("mi ganas sudah ditambahkan ke keranjang")

keranjang.tampilkan_pesanan()
print(f"Total biaya yang harus dibayarkan adalah {keranjang.total_harga()} rupiah, terimakasih sudah memesan")
