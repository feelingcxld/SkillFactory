import numpy as np

def score_game(random_predict):
    count_ls = list()
    np.random.seed(5)
    random_array = np.random.randint(1, 101, size=(1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")

def game_core_v3(number=1):
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