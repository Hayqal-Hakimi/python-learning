students = ['Amir', 'Bella', 'Chong', 'Deepa', 'Elena']
scores = [85, 42, 90, 38, 76]
jum_scores = len(scores)
lulus = 0
gagal = 0
final_mark = []
min_pass = int(input('sila masukkan angka lulus murid : '))

purata = sum(scores) / jum_scores

for murid,markah in zip(students, scores) :
    print(f'{murid}: {markah}')

for markah in scores :
    if markah >= min_pass :
        lulus += 1

for markah in scores :
    if markah < min_pass :
        gagal += 1 

print(f'\nJumlah pelajar lulus: {lulus}')
print(f'\nJumlah pelajar gagal: {gagal}')
print(f'\nPurata markah murid {purata}')

for percent in scores :
    percent = (percent / 140) * 100
    final_mark.append(round(percent))


inginCari = True

while inginCari :
    carian = str(input("cari nama pelajar (type keluar jika ingin keluar) : ")).capitalize()

    if carian == 'Keluar' :
        print('Terima Kasih')
        break

    for murid,markah,markah_akhir in zip(students, scores, final_mark) : 
        if carian == murid :
            print(f'{murid} : {markah}\nMarkah Akhir {markah_akhir}%')
            break
    else: 
        print(f'maaf {carian} tiada dalam senarai')
    