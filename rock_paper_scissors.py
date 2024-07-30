import random

rock = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

user_choice = int(input("Что выберешь? Введи 0 для камня, 1 для бумаги или 2 для ножниц: "))

if user_choice < 0 or user_choice > 2:
    print("Ты ввел некорректное число. Ты проиграл!")
else:
    computer_choice = random.randint(0, 2)
    print(f"Ты выбрал:\n{game_images[user_choice]}")
    print(f"Компьютер выбрал:\n{game_images[computer_choice]}")
    if user_choice == computer_choice:
        print("Ничья!")
    elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
        print("Ты выиграл!")
    else:
        print("Ты проиграл!")