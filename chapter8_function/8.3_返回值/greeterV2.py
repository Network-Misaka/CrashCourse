def get_formatted_name(first_name, last_name):
    # 返回整洁的姓名
    full_name = first_name + " " + last_name
    return full_name.title()


# 这是一个无限循环

while True:
    # print('\n Please tell me your name:')
    print("(enter 'q' at anytime to quit)")
    f_name = input('First name:')
    if f_name == 'q' :
        break
    l_name = input('Last name:')
    if l_name == 'q' :
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print('\n Hello, ' + formatted_name + '!')