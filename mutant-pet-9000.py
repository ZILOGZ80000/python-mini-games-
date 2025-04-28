import time
import random
import sys

class MutantPet:
    def __init__(self):
        self.parts = {
            'голова': ['🐱', '⛄', '🐲', '🍎'],
            'тело': ['🐟', '🍞', '🌈', '🐉'],
            'ноги': ['🦵', '🚗', '🐾', '🛸']
        }
        self.generate_new()
        self.hunger = 0
        self.mood = random.choice(['😊', '😐', '🤪'])

    def generate_new(self):
        self.name = random.choice(['Бобик', 'Мурзик', 'Цунами', 'Хлебоед',"абобус"])
        self.appearance = {
            'head': random.choice(self.parts['голова']),
            'body': random.choice(self.parts['тело']),
            'legs': random.choice(self.parts['ноги'])
        }

    def draw(self):
        print(f"\n=== {self.name} ===")
        print(f"  {self.appearance['head']}")
        print(f" {self.appearance['body']*3}")
        print(f"{self.appearance['legs']*2}  {self.appearance['legs']*2}")
        print(f"\nНастроение: {self.mood}  Голод: {'⭐' * self.hunger}")

    def feed(self):
        foods = ['🍕', '🍣', '🍔', '🥦']
        print("\nВыберите еду:")
        for i, food in enumerate(foods, 1):
            print(f"{i}. {food}")

        choice = input("> ")
        if choice in ['1', '2', '3', '4']:
            self.hunger = max(0, self.hunger - 2)
            print(f"\n{self.appearance['head']}: М-р-р-мяу! Спасибо за {foods[int(choice)-1]}")
            self.mood = random.choice(['😍', '😋', '🤤'])
        else:
            print("🚫 Неизвестная еда!")

    def play(self):
        games = {
            '1': '🔍 Искать хвост',
            '2': '🏃 Гонка за лазером',
            '3': '🎣 Рыбалка с усами'
        }

        print("\nВыберите игру:")
        for k, v in games.items():
            print(f"{k}. {v}")

        choice = input("> ")
        if choice == '1':
            self.animate("🌀 Вращение...", 5)
            print("Результат: Нашёл 3 хвоста и потерял голову!")
        elif choice == '2':
            self.animate("💨 Бег...", 3)
            print("Финиш! Заняли место: 🥇" if random.random() > 0.5 else "💥 Столкновение с диваном!")
        elif choice == '3':
            self.animate("🎣 Заброс...", 2)
            print("Поймали: " + random.choice(['🐡', '👢', '💻']))
        else:
            print("🚫 Игра сломалась!")

        self.hunger += 1
        self.mood = random.choice(['🤪', '😎', '🥳'])

    def animate(self, text, seconds):
        for _ in range(seconds*2):
            print(f"\r{text} {'/' * (_%4)}", end='')
            time.sleep(0.5)
        print()

def main():
    pet = MutantPet()
    actions = {
        '1': 'Покормить',
        '2': 'Играть',
        '3': 'Новый питомец',
        '4': 'Выход'
    }

    print("🐾 Добро пожаловать в MutantPet 9000! 🧬")

    while True:
        pet.draw()
        print("\nВыберите действие:")
        for k, v in actions.items():
            print(f"{k}. {v}")

        choice = input("> ")
        if choice == '1':
            pet.feed()
        elif choice == '2':
            pet.play()
        elif choice == '3':
            new_en=input("хочешь завести нового питомца? 1 - да все оспальное - нет ")
            if new_en == "1":
                pet.generate_new()
                print("🔬 Новый питомец создан!")
            else:
                print("фух")
        elif choice == '4':
            print("🐾 До новых экспериментов!")
            break
        else:
            print("🚫 Неизвестная команда!")

        time.sleep(1)

        if pet.hunger >= 5:
            print("\n💢 ВНИМАНИЕ! Питомец голоден и сбежал!")
            pet = MutantPet()

if __name__ == "__main__":
    main()
