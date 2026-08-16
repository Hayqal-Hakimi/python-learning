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

def baca_config(nama_fail):
    try : 
        with open(nama_fail,'r') as openFile :
            kandungan = openFile.read()
            fail_yang_ambil = nama_fail

    except FileNotFoundError : 
        defult = {
            'port' : '101:099:100',
            'ID Server' : 'D001',
            'IP ADDRESS' : 'B9101A'
        }
        kandungan = defult
        fail_yang_ambil = 'defult'
    finally : 
        print(f'setting sudah dipasang meggunakana fail {fail_yang_ambil}')

    return kandungan


baca_config('tes1.txt')