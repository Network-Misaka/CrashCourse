def build_profile(first, last, **user_info):
    # 创建一个字典 其中包含我们直到有关用户的一切
    # **代表字典 *代表元组
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics', god='Zhang Chen')
print(user_profile)
