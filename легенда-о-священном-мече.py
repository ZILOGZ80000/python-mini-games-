import random

class Player:
    def __init__(self, name, cls):
        self.name = name
        self.cls = cls
        self.health = 100
        self.mana = 50
        self.strength = 10
        self.agility = 10
        self.intellect = 10
        self.level = 1
        self.xp = 0

    def attack(self, enemy):
        damage = random.randint(0, self.strength*2) * self.level
        enemy.health -= damage
        print(f"{self.name} наносит {damage} урона мечом!")
        return damage

    def cast_spell(self, enemy):
        if self.mana < 10:
            print("Не хватает маны!")
            return
        self.mana -= 10
        damage = random.randint(0, self.intellect*3) * self.level
        enemy.health -= damage
        print(f"{self.name} атакует огнём! Урон: {damage}")
        return damage

class Enemy:
    def __init__(self, name):
        self.name = name
        self.health = random.randint(50, 150)
        self.strength = random.randint(5, 20)

def game_loop():
    print("Добро пожаловать в Легенду о Священном Мече!")
    name = input("Введите имя персонажа: ")
    cls = input("Выберите класс (воин/маг/вор): ").lower()

    player = Player(name, cls)
    if cls == "воин":
        player.strength = 15
    elif cls == "маг":
        player.intellect = 15
    elif cls == "вор":
        player.agility = 15

    while True:
        print("\n🌟 Меню:")
        print("1. Пойти в лес (бой)")
        print("2. Отдохнуть (восстановить HP/MP)")
        print("3. Посетить трактир (покупка)")
        print("4. Выход")

        choice = input("Выбор: ")

        if choice == "1":
            enemy = Enemy("Темный рыцарь")
            battle(player, enemy)
        elif choice == "2":
            player.health += 20
            player.mana += 10
            print("Вы отдохнули. HP и мана восстановлены.")
        elif choice == "3":
            shop(player)
        elif choice == "4":
            print("Спасти прогресс? (да/нет)")
            save_choice = input().lower()
            if save_choice == "да":
                save_game(player)
            break

def battle(player, enemy):
    print(f"\n🗡️ Битва с {enemy.name}!")
    while enemy.health > 0 and player.health > 0:
        print(f"\nHP: {player.health} | MP: {player.mana}")
        print(f"Враг: {enemy.name} (HP: {enemy.health})")

        action = input("\nДействие (атака/магия/бег): ").lower()

        if action == "атака":
            damage = player.attack(enemy)
            if enemy.health <= 0:
                xp = random.randint(20, 50)
                player.xp += xp
                print(f"\n🎉 Враг побеждён! Получено XP: {xp}")
                if player.xp >= (player.level * 100):
                    level_up(player)
                break
            enemy_damage = enemy.strength * random.uniform(0.7, 1.3)
            player.health -= int(enemy_damage)
            print(f"Враг наносит {int(enemy_damage)} урона!")

        elif action == "магия":
            player.cast_spell(enemy)
            enemy_damage = enemy.strength * random.uniform(0.7, 1.3)
            player.health -= int(enemy_damage)
            print(f"Враг наносит {int(enemy_damage)} урона!")

        elif action == "бег":
            if random.random() < 0.5:
                print("Успешный бег!")
                break
            else:
                print("Не удалось сбежать! Враг атакует!")
                player.health -= enemy.strength * 2
                continue

    if player.health <= 0:
        print("\n💀 Игра окончена: герой пал в битве!")
        return

def level_up(player):
    player.level += 1
    player.xp -= player.level * 100
    print(f"\n🔥 Левел ап! Теперь уровень {player.level}!")
    print("Распределите очки атрибутов:")
    points = 3  # Больше очков за каждые 5 уровней

    while points > 0:
        print(f"\nОчки: {points}")
        print("1. Сила (+2)")
        print("2. Ловкость (+2)")
        print("3. Интеллект (+2)")
        choice = input("Выбор: ")
        if choice in ["1", "2", "3"]:
            if choice == "1":
                player.strength += 2
            elif choice == "2":
                player.agility += 2
            elif choice == "3":
                player.intellect += 2
            points -= 1
        else:
            print("Неверный выбор!")

# Запуск игры
game_loop()
