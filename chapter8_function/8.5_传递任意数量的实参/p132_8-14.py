def cars_info(maker, car_type, **extra):
    info = {}
    info['car_maker'] = maker
    info['car_type'] = car_type
    for key, value in extra.items():
        info[key] = value
    return info


new_car = cars_info('一汽大众', '本田', 轮胎='四个', 里程数='0')
print(new_car)