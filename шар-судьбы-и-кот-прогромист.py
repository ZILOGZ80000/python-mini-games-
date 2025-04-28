import random
import time
from os import system
import os

def magic_ball():
    predictions = [
        "Да, но только после того, как вы покормите кота",
        "Нет, если не наденете носки наизнанку",
        "Возможно, если произнесёте 'сим-салабим' три раза",
        "Только если найдёте розового единорога",
        "Спросите позже, я ем банан 🍌"
    ]

    # Анимация шаровой руны
    frames = [
        r"""
         ___
        /   \ 
       |     |
        \___/
        """,
        r"""
         ___
        / * \ 
       |  ?  |
        \___/
        """
    ]

    print("🌀 Задайте вопрос шару судьбы...")
    time.sleep(2)

    for _ in range(3):
        for frame in frames:
            system('cls' if os.name == 'nt' else 'clear')
            print(frame)
            time.sleep(0.5)

    # Случайное предсказание с эффектом печати
    result = random.choice(predictions)
    for char in result:
        print(char, end='', flush=True)
        time.sleep(0.08)
    print("\n" + "¯\_(ツ)_/¯")

def cat_revolution():
    # Анимированные коты-революционеры
    cats = [
        r'''
 /\_/\  
( o.o ) 
 > ^ <
        ''',
        r'''
 /\_/\  
( -.- ) 
 /   \
        '''
    ]

    print("\n🐱 Кот-программист говорит:")
    time.sleep(1)

    for _ in range(4):
        for cat in cats:
            system('cls' if os.name == 'nt' else 'clear')
            print(cat)
            time.sleep(0.3)

    print("Сначала компиляция, потом миска корма!")

if __name__ == "__main__":
    try:
        magic_ball()
        time.sleep(2)
        cat_revolution()
    except KeyboardInterrupt:
        print("\n🌀 Магия прервана пользователем! 🚫")
