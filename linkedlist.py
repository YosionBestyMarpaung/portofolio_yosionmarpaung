"""
Nama: Yosion Besty Marpaung - 23091397168
Kelas: 2023E
Prodi: D4 Manajemen Informatika

"""

# Harga Awal
total_harga = 0

# Menampilkan Menu Topping
print("""
Pilihan Topping :
1. Frankfurter BBQ
2. Meat Monsta
3. Super Supreme
4. Super Supreme Chicken
""")

# Memilih Topping
topping_input = int(input("Pilih Topping Pizza (1-4): "))
if topping_input == 1:
    topping_pizza = "Frankfurter BBQ"
elif topping_input == 2:
    topping_pizza = "Meat Monsta"
elif topping_input == 3:
    topping_pizza = "Super Supreme"
elif topping_input == 4:
    topping_pizza = "Super Supreme Chicken"
else:
    print("Pilihan topping tidak valid.")
    exit()

total_harga += 43637  # Semua topping punya harga sama

# Menampilkan Menu Crust dan Ukuran
print("""
Pilihan Crust :
1. Pan
2. StuffedCrust Cheese
3. StuffedCrust Sausage
4. Cheesy Bites
5. Crown Crust

Pilihan Ukuran :
1. Personal
2. Reguler
3. Large
""")

# Memilih Crust
crust_input = int(input("Pilih Crust Pizza (1-5): "))

crust_dict = {
    1: ("Pan", 0, [0, 57273, 89091]),
    2: ("StuffedCrust Cheese", 11818, [0, 65455, 104545]),
    3: ("StuffedCrust Sausage", 9091, [0, 64545, 102727]),
    4: ("Cheesy Bites", 13636, [0, 66364, 107273]),
    5: ("Crown Crust", 11818, [0, 65455, 104545])
}

if crust_input in crust_dict:
    crust_pizza, crust_harga, size_harga_list = crust_dict[crust_input]
    total_harga += crust_harga
else:
    print("Pilihan crust tidak valid.")
    exit()

# Memilih Ukuran
size_input = int(input("Pilih Ukuran Pizza (1-3): "))
size_nama = {1: "Personal", 2: "Reguler", 3: "Large"}

if size_input in [1, 2, 3]:
    total_harga += size_harga_list[size_input - 1]
    size_pizza = size_nama[size_input]
else:
    print("Pilihan ukuran tidak valid.")
    exit()

# Tambahan Keju
extra_cheese = input("Tambah Keju? (y/n): ").lower()
if extra_cheese == "y":
    if size_input == 1:
        total_harga += 13636
    elif size_input == 2:
        total_harga += 16364
    elif size_input == 3:
        total_harga += 19091

# Output Pesanan
print("\n--- STRUK PESANAN ---")
print("Terima kasih telah membeli Pizza di Pizza Hut!")
print(f"Topping       : {topping_pizza}")
print(f"Crust         : {crust_pizza}")
print(f"Ukuran        : {size_pizza}")
print(f"Tambahan Keju : {'Ya' if extra_cheese == 'y' else 'Tidak'}")
print(f"Total Harga   : Rp {total_harga:,}")
