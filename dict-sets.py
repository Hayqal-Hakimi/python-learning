# inventori = {
#     'Beras': 50,
#     'Gula': 30,
#     'Garam': 20
# }

# print(inventori['Beras'])

# # jangan letak = sebab python jangka anda nak tukar isi dari dict
# inventori.update({ 'Minyak': 15})
# inventori['Gula'] = 25

# # dict tiada index
# print(list(inventori.items()))

# server_config = {
#     'ip': '192.168.1.1',
#     'port': 8080
# }

# print(server_config.get('ip'))
# print(server_config.get('timeout', 30))

# fail_saiz = {
#     'log1.txt': 1200,
#     'log2.txt': 3400,
#     'log3.txt': 800
# }

# for key, value in fail_saiz.items() : 
#     print(f'{key}: {value} KB')

# harga_produk = {
#     'Kemeja': 50,
#     'Seluar': 80,
#     'Kasut': 120
# }

# for key, value in harga_produk.items() :
#     value = value * 0.9
#     harga_produk[key] = round(value)

# print(harga_produk)

# senarai_email = ['ali@mail.com', 'siti@mail.com', 'ali@mail.com', 'kamal@mail.com', 'siti@mail.com']

# print(set(senarai_email))

# server_aktif = {'server1', 'server2', 'server3', 'server4'}


# while True :
#     nama_server = str(input('Masukkan nombor Server : ')).lower()
#     if nama_server == 'keluar' :
#         print('Terima Kasih')
#         break
#     if nama_server in server_aktif : 
#         print('aktif')
#     else: 
#         print('tidak aktif')

# user_dibenarkan = {'admin', 'user1', 'user2'}
# user_dibenarkan.add('user3')
# user_dibenarkan.discard('user1')
# user_dibenarkan.discard('user99')
# print(user_dibenarkan)

# fail_semalam = {'file1.txt', 'file2.txt', 'file3.txt'}
# fail_hari_ini = {'file2.txt', 'file3.txt', 'file4.txt'}

# fail_ditambah = fail_hari_ini - fail_semalam
# fail_dibuang = fail_semalam - fail_hari_ini

# print(fail_ditambah, fail_dibuang)

# semua_produk = {
#     'Laptop': 'Elektronik',
#     'Roti': 'Makanan',
#     'Telefon': 'Elektronik',
#     'Susu': 'Makanan',
#     'Tablet': 'Elektronik'
# }
# kategori_dicari = 'Elektronik'
# elektronik = set()

# for key, value in semua_produk.items() :
#     if value == kategori_dicari :
#         elektronik.add(key)

# print(elektronik)
