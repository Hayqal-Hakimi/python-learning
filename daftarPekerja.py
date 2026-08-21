import random

senarai_pekerja_baharu = [
    {'nama': 'Ali bin Ahmad', 'email': 'ali@syarikat.com', 'umur': 25, 'jabatan': 'IT'},
    {'nama': 'Aina binti Hassan', 'email': 'aina-tiada-at.com', 'umur': 30, 'jabatan': 'HR'},
    {'nama': 'Kumar', 'email': 'kumar@syarikat.com', 'umur': 'dua puluh', 'jabatan': 'Kewangan'},
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
    if umur <= 18 : 
        raise DataTidakSahError('Umur', 'umur masih belum mencapai minimum syarat')
    

def daftar_ke_sistem(rekod):
    peratus = random.random()
    if not peratus >= 0.5 : 
        raise SambunganGagalError()
    return f"rekod untuk {rekod['nama']} berjaya didaftar"
    

def proses_onboarding(senarai_pekerja):
    for rekod in senarai_pekerja : 
        validate_pekerja(rekod)
        daftar_ke_sistem(rekod)

    # untuk setiap rekod: retry MAKSIMUM 3 kali HANYA untuk SambunganGagalError
    # DataTidakSahError -> terus masuk senarai gagal, JANGAN retry
    # guna while + try + except + else + finally
    # akhir: return (senarai_berjaya, senarai_gagal, ringkasan_sebab_gagal)
    

hasil = proses_onboarding(senarai_pekerja_baharu)