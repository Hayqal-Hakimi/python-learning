def withdraw_amount():
    while True:
        mount_duit = input('masukkan angka duit yg ingin dikeluarkan : ')
        try : 
            mount_duit = int(mount_duit)
        except ValueError:
            print('sila masukkan dalam bentuk angka') 
            continue
        try : 
            if mount_duit <= 0 :
                raise ValueError('sila masukkan angka sekurang kurangnya 1')
        except ValueError as error :
            print(error)
            continue
        else : 
            return f"duit sebanyak {mount_duit} berjaya dikeluarkan"
print(withdraw_amount())