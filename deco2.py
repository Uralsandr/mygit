# Напишем функцию, которая принимает параметры и возвращает декоратор
def get_time_track(precision) :
    def time_track1(func): # практически тот же самый time_track, за исключением точности вывода времени 
        def surrogate (*args, **kwargs):   
            started_at = time.time()
            result = func(*args, **kwargs)
            ended_at = time.time()
            elapsed = round(ended_at - started_at, precision) # отличия в этой строке 
            print(f'Функция работала {  elapsed} секунд(ы)') 
	        return result
        return surrogate
    return time track



time_track_precision_6 = get_time_track(presision =6)
digits = time_track_precision_6(digits) 
result = digits(3141, 5926, 2718, 2818) 
print(result)