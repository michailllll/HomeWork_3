# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:
    # A, E, I, O, U, L, N, S, T, R – 1 очко; 
    # D, G – 2 очка; 
    # B, C, M, P – 3 очка; 
    # F, H, V, W, Y – 4 очка; 
    # K – 5 очков; 
    # J , X – 8 очков; 
    # Q, Z – 10 очков. 
#  А русские буквы оцениваются так: 
    # А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
    # Д, К, Л, М, П, У – 2 очка; 
    # Б, Г, Ё, Ь, Я – 3 очка; 
    # Й, Ы – 4 очка; 
    # Ж, З, Х, Ц, Ч – 5 очков; 
    # Ш, Э, Ю – 8 очков; 
    # Ф, Щ, Ъ – 10 очков. Н
# апишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы. 

list_find = list(input("Введите искомое слово   "))
list_1_eng =['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R']
list_2_eng = ['D', 'G']
list_3_eng = ['B', 'C', 'M', 'P']
list_4_eng = ['F', 'H', 'V', 'W', 'Y']
list_5_eng = ['K']
list_8_eng =['J', 'X']
list_10_eng = ['Q', 'Z']

list_1_rus = ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
list_2_rus = ['Д', 'К', 'Л','М', 'П', 'У']
list_3_rus = ['Б', 'Г', 'Ё', 'Ь', 'Я']
list_4_rus = ['Й', 'Ы']
list_5_rus = ['Ж', 'З', 'Х', 'Ц', 'Ч']
list_8_rus = ['Ш', 'Э', 'Ю']
list_10_rus = ['Ф', 'Щ', 'Ъ']

count = 0
for i in range(len(list_find)):

    if list_find[i] in list_1_eng:
            count += 1
    if list_find[i] in list_2_eng:
            count += 2
    if list_find[i] in list_3_eng:
            count += 3
    if list_find[i] in list_4_eng:
            count += 4
    if list_find[i] in list_5_eng:
            count += 5
    if list_find[i] in list_8_eng:
            count += 8
    if list_find[i] in list_10_eng:
            count += 10
    if count == 0:
       break
    

for i in range(len(list_find)):
    if count > 0:
        break

    if list_find[i] in list_1_rus:
            count += 1
    if list_find[i] in list_2_rus:
            count += 2
    if list_find[i] in list_3_rus:
            count += 3
    if list_find[i] in list_4_rus:
            count += 4
    if list_find[i] in list_5_rus:
            count += 5
    if list_find[i] in list_8_rus:
            count += 8
    if list_find[i] in list_10_rus:
            count += 10


print(count)

