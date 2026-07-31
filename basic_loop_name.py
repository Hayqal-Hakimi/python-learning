# friends = ['Amir', 'Bella', 'Chong', 'Deepa', 'Elena']
# for friend in friends :
#     print(friend)


# word = 'python'

# for letters in word :
#     print(letters.upper())


# colors = ['Merah', 'Biru']
# sizes = ['S', 'M', 'L']

# for color in colors :
#     for size in sizes :
#         print(f"{color} - {size.upper()}")


# correct_password = "malaysia123"
# password = "hayqal"

# while password != correct_password :
#     password = str(input('sila masukkan password : '))
#     if password != correct_password :
#         print('Kata laluan salah, cuba lagi.')
#     else : 
#         print('Akses dibenarkan.')
#         break


# temperatures = [22, 25, 19, 31, 28, 35, 20]

# for suhu in temperatures :
#     if suhu > 30 :
#         break
#     else :
#         print(suhu)


# scores = [85, 42, 90, 38, 76, 55, 95]
# total_lulus = 0

# for jumLulus in scores :
#     if jumLulus < 50 :
#         continue
#     else :
#         total_lulus += 1

# print(total_lulus)


# inventory = ['Beras', 'Gula', 'Garam', 'Minyak', 'Susu']
# carian = 'Susu'

# for item in inventory :
#     if item == carian : 
#         print(f'{item} dijumpai dalam stok.')
#         break
# else :
#         print('item TIDAK dijumpai dalam stok.')


# shopping_list = ['Beras', 'Gula', 'Telur', 'Roti', 'Susu']

# shopping_list.append('Minyak')

# shopping_list.remove('Telur')

# shopping_list

# print(shopping_list)

attendance = ('Hadir', 'Tidak Hadir', 'Hadir', 'Hadir', 'Tidak Hadir', 'Hadir', 'Hadir')

print(f'Jumlah Hadir: {attendance.count('Hadir')}')

print(f'Index pertama Tidak Hadir: {attendance.index('Tidak Hadir')}')
