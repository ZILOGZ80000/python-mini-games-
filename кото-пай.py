import time
import sys
import random

def cat_animation():
    frames = [
        r'''
  /\_/\  
 ( o.o ) 
  > ^ <
''',
        r'''
  /\_/\  
 ( -.- ) 
  /   \ 
''',
        r'''
  /\_/\  
 ( @.@ ) 
  = _ =
'''
    ]

    for _ in range(8):
        for frame in frames:
            print('\033[H\033[J')  # Альтернативная очистка экрана
            print(frame)
            time.sleep(0.3)

def cat_generator():
    parts = {
        'глаза': ['🔸', '🔹', '⭐', '🍕'],
        'нос': ['👃', '🌼', '🍬', '  '],
        'усы': ['≽^•⩊•^≼', '≽◕ᴥ◕≼', '≽ ՞ ਊ ՞ ≼']
    }

    print('\nВаш уникальный кот:')
    print(f'''
   /\_/\  
  ( {random.choice(parts["глаза"])}.{random.choice(parts["глаза"])} )
  {random.choice(parts["усы"])}
   {random.choice(parts["нос"])}
    ''')

def main_menu():
    while True:
        print('\n' + '='*25)
        print('🐱 Кото-Меню:')
        print('1. Танцующий кот')
        print('2. Сгенерировать кота')
        print('3. Кото-совет')
        print('4. Выход')

        choice = input('Выберите пункт: ')

        if choice == '1':
            cat_animation()
        elif choice == '2':
            cat_generator()
        elif choice == '3':
            print('\nКот рекомендует:', random.choice([
                'Почешите за ухом!',
                'Обновите версию корма!',
                'Перезагрузите диван!'
            ]))
        elif choice == '4':
            print('До новых встреч! 🐾')
            break
        else:
            print('Мяу? Не понимаю...')

if __name__ == "__main__":
    print('\03333m' + '='*30 + '\n  Добро пожаловать в КотоПай! \n' + '='*30)
    time.sleep(1)
    main_menu()
    