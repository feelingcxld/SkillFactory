import numpy as np

def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = list()
    np.random.seed(5) # фиксируем сид для воспроизведения результатов
    random_array = np.random.randint(1, 101, size=(1000)) # загадываем список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")

def game_core_v3(number:int=1) -> int:
    """Функция, самостоятельно угадывающая случайно заданное число

    Args:
        number (int, optional): Случайно заданное число. Defaults to 1.

    Returns:
        int: Количество затраченных попыток на угадывание
    """
    count = 0
    left_border = 1
    right_border = 101
    predict_number = np.random.randint(1, 101)
    
    while number != predict_number:
        count += 1
        
        if number < predict_number:
            right_border = predict_number
            predict_number = np.random.randint(left_border, right_border)
            
        elif number > predict_number:
            left_border = predict_number
            predict_number = np.random.randint(left_border, right_border)
            
    return count

print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)