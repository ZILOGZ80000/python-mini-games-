import os
import time
import random

def draw_scene(cat_pos, breads, score):
    print("\033[H\033[J")  # Очистка экрана
    print(f"🍞 Лови тосты! Счёт: {score}\n")

    # Рисуем игровое поле 10x10
    for y in range(10):
        line = []
        for x in range(10):
            if (x, y) in breads:
                line.append('🍞')
            elif y == 9 and x in cat_pos:
                line.append('🐈⬛')
            else:
                line.append('・')
        print(' '.join(line))

def bread_cat():
    cat_pos = {4, 5}  # Начальная позиция кота (2 клетки)
    breads = set()
    score = 0
    speed = 0.5

    print("Добро пожаловать в КотоХлеб 3000!")
    time.sleep(1)
    print("Управление: A - влево, D - вправо, Q - выход")
    time.sleep(2)

    while True:
        # Генерация нового тоста
        if random.random() < 0.3:
            breads.add((random.randint(0, 9), 0))

        # Отрисовка
        draw_scene(cat_pos, breads, score)

        # Движение тостов
        new_breads = set()
        for (x, y) in breads:
            if y < 9:
                new_breads.add((x, y + 1))
                if y + 1 == 9 and x in cat_pos:
                    score += 10
        breads = new_breads

        # Управление
        try:
            key = input().lower()
            if key == 'a' and min(cat_pos) > 0:
                cat_pos = {x-1 for x in cat_pos}
            elif key == 'd' and max(cat_pos) < 9:
                cat_pos = {x+1 for x in cat_pos}
            elif key == 'q':
                break
        except:
            pass

        # Усложнение игры
        if score > 50:
            speed = max(0.2, speed - 0.02)

        time.sleep(speed)

    print(f"\nИгра окончена! Финальный счёт: {score}")
    print("Кот доволен: " + random.choice(["🐟", "🍗", "🥛"]))

if __name__ == "__main__":
    bread_cat()
    