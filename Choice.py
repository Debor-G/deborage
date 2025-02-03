import random

print("Выбери число 1 или 2")
try:
    user_choice = int(input())  # By Debor
    if user_choice not in [1, 2]:
        print("Нужно ввести 1 или 2!")
    else:
        numbers = [1, 2]
        random_number = random.choice(numbers)

        print(f"Выпало: {random_number}")

        if random_number == user_choice:
            print("Молодец!")
        else:
            print("Не угадал!")

        input("Нажмите Enter, чтобы выйти...")  
except ValueError:
    print("Ошибка! Введите число 1 или 2.")  
    input("Нажмите Enter, чтобы выйти...")  




























#By Debor