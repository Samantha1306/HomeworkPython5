# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

#! Играют 2 человека
# from random import randint as rd
# player1 = input("Введите имя игрока 1: ")
# player2 = input("Введите имя игрока 2: ")
# candies = 2021

# flag = rd(0,2)
# if flag:
#     print(f"Первым ходит игрок: {player1}.")
# else:
#     print(f"Первым ходит игрок: {player2}.")

# count1 = 0 
# count2 = 0

# def candies_number(player):
#     x = int(input(f"Введите количество конфет от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"Ошибка! Введите количество конфет от 1 до 28: "))
#     return x

# def candies_on_the_table(player, x, candies):
#     print(f"Игрок {player} взял/а {x} конфет/у/ы. На столе осталось {candies} конфет.")

# while candies > 28:
#     if flag:
#         x = candies_number(player1)
#         count1 += x
#         candies -= x
#         flag = False
#         candies_on_the_table(player1, x, candies)
#     else:
#         x = candies_number(player2)
#         count2 += x
#         candies -= x
#         flag = True
#         candies_on_the_table(player2, x, candies)

# if flag:
#     print(f"Выиграл игрок: {player1}.")
# else:
#     print(f"Выиграл игрок: {player2}.")


#! Играют человек и бот

# from random import randint as rd
# player1 = input("Введите имя игрока 1: ")
# player2 = 'Компьютер'
# candies = 200

# flag = rd(0,2)
# if flag:
#     print(f"Первым ходит игрок: {player1}.")
# else:
#     print(f"Первым ходит: {player2}.")

# count1 = 0 
# count2 = 0

# def candies_number(player):
#     x = int(input(f"Введите количество конфет от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"Ошибка! Введите количество конфет от 1 до 28: "))
#     return x

# def candies_on_the_table(player, x, candies):
#     print(f"{player} взял/а {x} конфет/у/ы. На столе осталось {candies} конфет.")
    
# while candies > 28:
#     if flag:
#         x = candies_number(player1)
#         count1 += x
#         candies -= x
#         flag = False
#         candies_on_the_table(player1, x, candies)
#     else:
#         x = rd(1,29)
#         count2 += x
#         candies -= x
#         flag = True
#         candies_on_the_table(player2, x, candies)

# if flag:
#     print(f"Выиграл игрок: {player1}.")
# else:
#     print(f"Выиграл {player2}.")

#! Играют человек и умный бот

from random import randint as rd
player1 = input("Введите имя игрока 1: ")
player2 = 'Компьютер'
candies = 200

flag = rd(0,2)
if flag:
    print(f"Первым ходит игрок: {player1}.")
else:
    print(f"Первым ходит: {player2}.")

count1 = 0 
count2 = 0

def candies_number(player):
    x = int(input(f"Введите количество конфет от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"Ошибка! Введите количество конфет от 1 до 28: "))
    return x

def candies_on_the_table(player, x, candies):
    print(f"{player} взял/а {x} конфет/у/ы. На столе осталось {candies} конфет.")

def smart_choice(candies):
    x = rd(1,29)
    while candies-x <= 28 and candies > 29:
        x = rd(1,29)
    return x   
while candies > 28:
    if flag:
        x = candies_number(player1)
        count1 += x
        candies -= x
        flag = False
        candies_on_the_table(player1, x, candies)
    else:
        x = smart_choice(candies)
        count2 += x
        candies -= x
        flag = True
        candies_on_the_table(player2, x, candies)

if flag:
    print(f"Выиграл игрок: {player1}.")
else:
    print(f"Выиграл {player2}.")
