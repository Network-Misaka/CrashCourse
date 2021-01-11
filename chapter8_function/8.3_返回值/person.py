def build_person(first_name, last_name, age=''):
    # 返回一个字典
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


# musician = build_person('zhao', 'si', age=27)
musician = build_person('zhao', 'si')
print(musician)