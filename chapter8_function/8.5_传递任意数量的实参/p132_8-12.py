def foods_info(*foods):
    print('This customer want to eat:\t')
    for food in foods:
        print('- ' + food + '\t')


foods_info('sugar', 'salt', 'yogurt')