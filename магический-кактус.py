import os 
import random
import time
from os import system

def magic_ball():
    predictions = [
        "Да, но сначала обновите Windows 95",
        "Нет, если не станцевать ламбаду",
        "Спросите у кота, он в курсе 🐈",
        "Да, если по"
    ]

    # Исправленная анимация с учётом импорта
    frames = [
        r"""
         ___
        /👾\ 
       | ?  |
        \___/
        """,
        r"""
         ___
        /🌀\ 
       | !  |
        \___/
        """
    ]

    print("🌀 Задайте вопрос магическому кактусу...")
    time.sleep(1)

    for _ in range(3):
        for frame in frames:
            system('cls' if os.name == 'nt' else 'clear')  # Теперь os доступен
            print(frame)
            time.sleep(0.3)

    # Весёлый эффект печати
    result = random.choice(predictions)
    print("\n" + "▌" * 20)
    for char in result:
        print(char, end='', flush=True)
        time.sleep(0.1)
    print("\n" + "¯\_(🌵)_/¯")

def pizza_time():
    # Анимация готовки пиццы
    stages = [
        r"""
         🍅
        🧀🍕
         🔥
        """,
        r"""
         🍅🍅
        🧀🧀🍕
         🔥🔥
        """
    ]

    print("\nПриготовление пиццы...")
    time.sleep(1)

    for _ in range(4):
        for stage in stages:
            system('cls' if os.name == 'nt' else 'clear')
            print(stage)
            time.sleep(0.4)

    print("Пицца готова! 🍕🎉")

if __name__ == "__main__":
    try:
        magic_ball()
        time.sleep(1)
        pizza_time()
    except:
        print("\nВсё сломалось, но пицца осталась! 🍕")
