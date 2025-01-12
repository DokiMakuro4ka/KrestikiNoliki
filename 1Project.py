def check_win(place, player):
    # Проверка строк
    for row in place:
        if all(cell == player for cell in row):
            return True

    # Проверка столбцов
    for col in range(len(place)):
        if all(row[col] == player for row in place):
            return True

    # Проверка диагоналей
    if all(place[i][i] == player for i in range(len(place))) or \
       all(place[i][len(place) - i - 1] == player for i in range(len(place))):
        return True

    return False

def pole ():
    for i in range(ROWS):
        for j in range(COLS):
            print(place[i][j], end = '\t') 
        print()

def krest (i, j):
    if place[i][j] == 'x' or place[i][j] == 'o':
        print('Попробуйте ещё раз, вы указали поле, которое уже занято')
        i = input('Укажите строчку (1,2,3) ')
        j = input('Укажите стобец (1,2,3) ')
        if i.isdigit() == True and j.isdigit() == True and int(i) >= 1 or int(i) <= 3 and int(j) >= 1 or int(j) <= 3:
            return nol(int(i), int(j))
        while i.isdigit() == True and j.isdigit() == True and int(i) < 1 or int(i) > 3 and int(j) < 1 or int(j) > 3:
            i = input('Укажите строчку (1,2,3) ')
            j = input('Укажите стобец (1,2,3) ')
        
    elif place[i][j] == '':
        place[i][j] = 'x'
        
        print('Вы успешно изменили клетку\n')
        pole()
    else:
        i = input('Укажите строчку (1,2,3) ')
        j = input('Укажите стобец (1,2,3) ')
        if i.isdigit() == True and j.isdigit() == True and int(i) >= 1 or int(i) <= 3 and int(j) >= 1 and int(j) <= 3:
            return nol(int(i), int(j))
        while i.isdigit() == True and j.isdigit() == True and int(i) < 1 or int(i) > 3 and int(j) < 1 or int(j) > 3:
            i = input('Укажите строчку (1,2,3) ')
            j = input('Укажите стобец (1,2,3) ')

def nol (i, j):
    if place[i][j] == 'x' or place[i][j] == 'o':
        print('Попробуйте ещё раз, вы указали поле, которое уже занято')
        i = input('Укажите строчку (1,2,3) ')
        j = input('Укажите стобец (1,2,3) ')
        if i.isdigit() == True and j.isdigit() == True and int(i) >= 1 or int(i) <= 3 and int(j) >= 1 or int(j) <= 3:
            return nol(int(i), int(j))
        while i.isdigit() == True and j.isdigit() == True and int(i) < 1 or int(i) > 3 and int(j) < 1 or int(j) > 3:
            i = input('Укажите строчку (1,2,3) ')
            j = input('Укажите стобец (1,2,3) ') 
    elif place[i][j] == '':
        place[i][j] = 'o'
        
        print('Вы успешно изменили клетку\n')
        pole()
    else:
        print('Повторите попытку')
        i = input('Укажите строчку (1,2,3) ')
        j = input('Укажите стобец (1,2,3) ')
        if i.isdigit() == True and j.isdigit() == True and int(i) >= 1 or int(i) <= 3 and int(j) >= 1 or int(j) <= 3:
            return nol(int(i), int(j))
        while i.isdigit() == True and j.isdigit() == True and int(i) < 1 or int(i) > 3 and int(j) < 1 or int(j) > 3:
            i = input('Укажите строчку (1,2,3) ')
            j = input('Укажите стобец (1,2,3) ')
            
            
ROWS = 4 # кол-во строчек
COLS = 4 # кол-во столбцов

# Создание поля для крестиков ноликов
place = [
    ['', '1', '2', '3'],
    ['1', '', '', ''],
    ['2', '', '', ''],
    ['3', '', '', ''],
]

#Инициализация игры
print('Приветствую в игре, созданной Осокиным Даниилом, это классические крестики-нолики\n')

check = 1
while check == 1:
    ask = input('Чтобы начать играть играть выбери за кого ты будешь играть изначально: 1) Нолик, 2) Крестик, 0)выход ')
    if ask.isdigit() == True:
        if int(ask) == 1:
            while check == 1:
                pole()
                print('Ход нолика')
                i = input('Укажите строчку (1,2,3) ')
                j = input('Укажите стобец (1,2,3) ')
                if i.isdigit() == True and j.isdigit() == True and int(i) >= 1 or int(i) <= 3 and int(j) >= 1 or int(j) <= 3:
                    if check_win(place, 'x'):
                        print("X победил!")
                    elif check_win(place, 'o'):
                        print("O победил!")
                    else:
                        print('Ход крестика')
                    nol(int(i), int(j))
                    
                    i = input('Укажите строчку (1,2,3) ')
                    j = input('Укажите стобец (1,2,3) ')
                    if i.isdigit() == True and j.isdigit() == True:
                        if check_win(place, 'x'):
                            print("X победил!")
                        elif check_win(place, 'o'):
                            print("O победил!")
                        else:
                            print('Ход нолика')
                        krest(int(i), int(j))
                    elif j.isdigit() == True and int(j) >= 1 or int(j) <= 3:
                        print('Вы ввели только столбец с нужным диапозоном')
                    elif i.isdigit() == True and int(i) >= 1 or int(i) <= 3:
                        print('Вы ввели только строчку с нужным диапозоном')
                    else:
                        while i.isdigit() == True and j.isdigit() == True:
                            i = input('Укажите строчку (1,2,3) ')
                            j = input('Укажите стобец (1,2,3) ')
                elif j.isdigit() == True and int(j) >= 1 or int(j) <= 3:
                    print('Вы ввели только столбец с нужным диапозоном')
                elif i.isdigit() == True and int(i) >= 1 or int(i) <= 3:
                    print('Вы ввели только строчку с нужным диапозоном')
                else:
                    while i.isdigit() == True and j.isdigit() == True:
                        i = input('Укажите строчку (1,2,3) ')
                        j = input('Укажите стобец (1,2,3) ')
        elif int(ask) == 2:
            while check == 1:
                print('Ход Крестика')
                i = input('Укажите строчку (1,2,3) ')
                j = input('Укажите стобец (1,2,3) ')
                if i.isdigit() == True and j.isdigit() == True:
                    if check_win(place, 'x'):
                        print("X победил!")
                    elif check_win(place, 'o'):
                        print("O победил!")
                    else:
                        print('Ход крестика')
                    krest(int(i), int(j))
                    print('Ход нолика')
                    i = input('Укажите строчку (1,2,3) ')
                    j = input('Укажите стобец (1,2,3) ')
                    if i.isdigit() == True and j.isdigit() == True:
                        if check_win(place, 'x'):
                            print("X победил!")
                        elif check_win(place, 'o'):
                            print("O победил!")
                        else:
                            print('Ход нолика')
                        nol(int(i), int(j))
                    else:
                        while i.isdigit() == True and j.isdigit() == True:
                            i = input('Укажите строчку (1,2,3) ')
                            j = input('Укажите стобец (1,2,3) ')
                else:
                    while i.isdigit() == True and j.isdigit() == True:
                        i = input('Укажите строчку (1,2,3) ')
                        j = input('Укажите стобец (1,2,3) ')
        elif int(ask) == 0:
            print('Уже покидаете? Печально, связаться со мной можно по тг @NomikLover или по почте brumis01@mail.ru')
            break
        elif int(ask) > 2 or int(ask) < 0:
            print('Вы вышли из диапозона нужного выбора\n')
    else:
        print('Вы ввели не число')