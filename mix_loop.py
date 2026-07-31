students = ['Amir', 'Bella', 'Chong', 'Deepa', 'Elena']
scores = [85, 42, 90, 38, 76]
lulus = 0

for murid,markah in zip(students, scores) :
    print(f'{murid}: {markah}')

for markah in scores :
    if markah >= 50 :
        lulus += 1

print(f'\nJumlah pelajar lulus: {lulus}')

inginCari = True

while inginCari :
    carian = str(input("cari nama pelajar (type keluar jika ingin keluar) : ")).capitalize()

    if carian == 'Keluar' :
        print('Terima Kasih')
        break

    for murid,markah in zip(students, scores) : 
        if carian == murid :
            print(f'{murid} : {markah}')
            break
    else: 
        print(f'maaf {carian} tiada dalam senarai')
    