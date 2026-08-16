class Tiket:
    def __init__(individu, nombor_kerusi, nama_wayang, harga):
        individu.nombor_kerusi = nombor_kerusi
        individu.nama_wayang = nama_wayang
        individu.harga = harga
tiket1 = Tiket("A5", "Avengers", 15)
tiket2 = Tiket("B3", "Frozen", 12)

print(tiket1.nombor_kerusi)  # sepatutnya keluar: A5
print(tiket2.nama_wayang)     # sepatutnya keluar: Frozen