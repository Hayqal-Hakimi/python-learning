import random

senarai_pekerja_baharu = [
    {'nama': 'Ali bin Ahmad', 'email': 'ali@syarikat.com', 'umur': 25, 'jabatan': 'IT'},
    {'nama': 'Aina binti Hassan', 'email': 'aina-tiada-at.com', 'umur': 30, 'jabatan': 'HR'},
    {'nama': 'Kumar', 'email': 'kumar@syarikat.com', 'umur': 30, 'jabatan': 'Kewangan'},
    {'nama': 'Siti', 'email': 'siti@syarikat.com', 'umur': 28, 'jabatan': 'Pemasaran'},
]

class DataTidakSahError(Exception):
    def __init__(self,jenisError, sebab):
        self.error = jenisError
        self.sebab = sebab

        super().__init__(f"data yang diberi {self.error} kerana {self.sebab}")

class SambunganGagalError(Exception):
    pass
    

def validate_pekerja(rekod):
    email = rekod['email']
    if '@' not in email : 
        raise DataTidakSahError('email', 'tidak ada @ (format penulisan email)')
    umur = rekod['umur']
    if not isinstance(umur, int) : 
        raise DataTidakSahError('umur', 'umur pastikan di dalam integer')
    if umur <= 18 : 
        raise DataTidakSahError('Umur', 'umur masih belum mencapai minimum syarat')
    

def daftar_ke_sistem(rekod):
    peratus = random.random()
    if not peratus >= 0.5 : 
        raise SambunganGagalError()
    return f"rekod untuk {rekod['nama']} berjaya didaftar"
    

def proses_onboarding(senarai_pekerja):
    senarai_berjaya = []
    senarai_gagal = []
    ringkasan_sebab_gagal = []
    for rekod in senarai_pekerja :
        percubaan  = 0 
        status = False
        try : 
            validate_pekerja(rekod)
        except DataTidakSahError as e:
            ringkasan_sebab_gagal.append(str(e))
            senarai_gagal.append(rekod['nama'])
            continue 
        while not status and percubaan < 3 :
            percubaan += 1
            try : 
                daftar_ke_sistem(rekod)
                status = True
                senarai_berjaya.append(f"{rekod['nama']} dgn cubaan {percubaan} kali")
                break
            except SambunganGagalError :
                print(f"Percubaan ke-{percubaan} gagal untuk {rekod['nama']}. Cuba lagi...")
            finally:
                print(f"[LOG] Selesai proses percubaan {percubaan} untuk {rekod['nama']}")
        else : 
            senarai_gagal.append(rekod['nama'])
    return f"yang berjaya : {senarai_berjaya} | jumlah yang gagal : {len(senarai_gagal)} | sebab {ringkasan_sebab_gagal}"



    # DataTidakSahError -> terus masuk senarai gagal, JANGAN retry
    # guna while + try + except + else + finally
    # akhir: return (senarai_berjaya, senarai_gagal, ringkasan_sebab_gagal)
    

hasil = proses_onboarding(senarai_pekerja_baharu)

print(hasil)