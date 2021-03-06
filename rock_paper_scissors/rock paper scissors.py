# Реализовать игру «камень 1, ножницы 2, бумага 3». Используемые навыки: цикл while и оператор if.
# Условие выигрыша
'''
Камень побеждает ножницы (“камень затупляет или ломает ножницы”)  1 2
Бумага побеждает камень (“бумага накрывает камень”) 3 1
Ножницы побеждают бумагу (“ножницы разрезают бумагу”) 2 3
'''

import os
import random


# Функция очищения консоли, для более честных условий игры.
def clear():
    print('\n' * 50)


# Функция выбора хода игрока(ов)
def player_step():
    print('Выбирете вариант хода:\nкамень - 1\nножницы - 2\nбумага - 3')
    motion = int(input())
    return motion


# Функция выбора хода ИИ
def ai_step():
    return random.randint(1, 3)


# Функция выбора кол-во игроков
def amount_players():
    amo_players = int(input('Выберите количество игроков: '))
    while amo_players != 1 and amo_players != 2:
        amo_players = int(input('Выберите количество игроков: '))
    return amo_players


# Проверка выигрыша и вывод
def win_or_lose(p_1, p_2):
    flag = (p_1 == 1 and p_2 == 2) or (p_1 == 2 and p_2 == 3) or (p_1 == 3 and p_2 == 1)
    if p_1 == p_2:
        print('Ничья')
    elif flag:
        print('Победа первого игрока')
    else:
        print('Победа второго игрока')


# Основной код программы
def game():
    k = 1
    while k == 1:
        p_s = [0, 0]
        amount = amount_players()
        if amount == 1:
            p_s[0] = player_step()
            p_s[1] = ai_step()
            # print(p_s) - проверка, что выберет ии
        else:
            for i in range(amount):
                p_s[i] = player_step()
                clear()
        win_or_lose(p_s[0], p_s[1])
        k = int(input("Хотите сыграть еще раз?\n Да - 1\n Нет - 2\n"))
        clear()

game()
