"""Игра угадай число
Компьютер сам загадывает и сам угадывает число"""

import numpy as np

def random_predict(number: int=1) -> int:
    """Угадываем число за 20 попыток и меньше

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    max_number = 100
    min_number = 1

    while True:
        count+=1
        predict_number = (max_number + min_number) // 2

        if predict_number > number:
            max_number = predict_number - 1 # понижаем верхнюю границу диапазона поиска
            
        elif predict_number < number:
            min_number = predict_number + 1 #повышаем нижнюю границу диапазона поиска
            
        elif number == predict_number:
            break #выход из цикла если угадали
    
    return count

def score_game(random_predict)->int:
    """За какое количество попыток в среднем угадывает за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array= np.random.randint(1,101,size=(1000)) #загадали список 1000 чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score=int(np.mean(count_ls))
    print(f"Ваш алгоритм в среднем угадывает число за: {score} попыток")
    return score
 
 #RUN   
if __name__ == '__main__':
    score_game(random_predict)
    

#print(f"Количество попыток: {random_predict(25)}")
        