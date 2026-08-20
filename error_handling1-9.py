# def withdraw_amount():
#     while True:
#         mount_duit = input('masukkan angka duit yg ingin dikeluarkan : ')
#         try : 
#             mount_duit = int(mount_duit)
#         except ValueError:
#             print('sila masukkan dalam bentuk angka') 
#             continue
#         try : 
#             if mount_duit <= 0 :
#                 raise ValueError('sila masukkan angka sekurang kurangnya 1')
#         except ValueError as error :
#             print(error)
#             continue
#         else : 
#             return f"duit sebanyak {mount_duit} berjaya dikeluarkan"
# print(withdraw_amount())

# def baca_config(nama_fail):
#     try : 
#         with open(nama_fail,'r') as openFile :
#             kandungan = openFile.read()
#             fail_yang_ambil = nama_fail

#     except FileNotFoundError : 
#         defult = {
#             'port' : '101:099:100',
#             'ID Server' : 'D001',
#             'IP ADDRESS' : 'B9101A'
#         }
#         kandungan = defult
#         fail_yang_ambil = 'defult'
#     finally : 
#         print(f'setting sudah dipasang meggunakana fail {fail_yang_ambil}')

#     return kandungan


# baca_config('tes1.txt')

# def proses_markah(senarai_markah):
#     markah_yang_valid = []
#     for markah in senarai_markah : 
#         try : 
#             if not isinstance(markah, int) : 
#                 raise TypeError(markah)
#             else : 
#                 markah_yang_valid.append(markah)
#         except  TypeError as e : 
#             print(f"ankga ini tidak valid : {e}")
#             continue
#     return f'markah yang valid {markah_yang_valid}'

# print(proses_markah([85, '42', None, 90, 'abc']))

# server_config = {
#     'server1': {'ip': '192.168.1.1', 'port': 8080},
#     'server2': {'ip': '192.168.1.2'}  # TIADA 'port'!
# }

# def dapatkan_port(config, nama_server):
#     try : 
#         server = config[nama_server]
#     except KeyError : 
#         print(f'{nama_server} tidak wujud')
#         port = 0 
#         return port
#     try :
#         port = server['port']
#     except KeyError : 
#         print(f'port pada {nama_server} tiada : pakai port defult')
#         port = 80
#     return port

# print(dapatkan_port(server_config, 'server5'))
# dapatkan_port(server_config, 'server2')
# senarai_log = ['Isnin: OK', 'Selasa: Error', 'Rabu: OK']

# def dapatkan_log_hari(senarai_log, index_hari):
#     try : 
#         if len(senarai_log) <= index_hari : 
#             raise IndexError(f"log hari ke{index_hari} belum disenarai")

#     except IndexError as error : 
#         return error

#     hari_yg_diinginkan = senarai_log[index_hari]
#     return hari_yg_diinginkan

# print(dapatkan_log_hari(senarai_log, 0))
# print(dapatkan_log_hari(senarai_log, 2)) 
# print(dapatkan_log_hari(senarai_log, 5))

# class InsufficientFundsError(Exception):
#     def __init__(self, baki_akaun ,jumlah_keluar,) :  
#         kurang_berapa = jumlah_keluar - baki_akaun
#         self.kurang_berapa = kurang_berapa
#         self.baki_akaun = baki_akaun
#         self.jumlah_keluar = jumlah_keluar

# def keluarkan_wang(baki_akaun, jumlah_keluar): 
#     try :
#         if baki_akaun < jumlah_keluar :
#             raise InsufficientFundsError(baki_akaun, jumlah_keluar)
#     except InsufficientFundsError as error : 
#         return f'baki tidak cukup lagi {error.kurang_berapa}'

#     akaun_semasa = baki_akaun - jumlah_keluar 
#     return f'akaun semasa: {akaun_semasa}'


# print(keluarkan_wang(1000, 500))    # baki cukup, ada baki lebih - expect BERJAYA
# print(keluarkan_wang(1000, 1500))   # baki tak cukup - expect GAGAL
# print(keluarkan_wang(500, 500))     # keluar SEMUA baki - expect GAGAL (sebab akaun tak boleh 0)
    
# database = {
#     'user1': {'nama': 'Ali', 'umur': 17},
#     'user2': {'nama': 'Aina'}  # TIADA 'umur'!
# }

# def simpan_data(database, key):
#     try:
#         umur = database[key]['umur']
#         return umur
    
#     except KeyError as e:
#         raise ValueError('gagal simpan data ke database') from e
# print(simpan_data(database, 'user2')) 
   
# database_pengguna = {
#     'ali123': 'password123',
#     'aina456': 'kucing789'
# } 

# def login(username, password, database_pengguna):
#     try:
#         password_sebenar = database_pengguna[username]
#         if password_sebenar == password : 
#             return 'berjaya login' 
#         else : 
#             return 'password salah'
#     except ValueError:
#         raise ValueError('Username atau password salah.') from None
# print(login('ali123', 'password123', database_pengguna))  # username BETUL, password BETUL - BERJAYA
# print(login('ali123', 'salahpassword', database_pengguna))  # username BETUL, password SALAH - GAGAL
# print(login('hacker99', 'apa-apa', database_pengguna))     # username TAK WUJUD - GAGAL (trigger KeyError)

database_pengguna = {
    'ali123': {'password': 'password123', 'nama': 'Ali bin Ahmad', 'cubaan_gagal': 0},
    'aina456': {'password': 'kucing789', 'nama': 'Aina binti Hassan', 'cubaan_gagal': 0}
}

def cuba_login(username, password_input, database_pengguna):

    try:

        rekod_pengguna = database_pengguna[username]
        if password_input != rekod_pengguna['password'] : 
            raise ValueError('Username atau password salah.') from None
        return f'login berjaya dgn nama {rekod_pengguna['nama']}'

    except KeyError:
        raise ValueError('Username atau password salah.') from None

try : 
    print(cuba_login('ali123', 'password123', database_pengguna))
except ValueError as error :
    print(f"error yang ada ialah {error}")