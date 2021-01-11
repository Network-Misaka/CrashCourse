def print_models(unprinted_design, completed_models):
    # 模拟打印每个设计后，直到没有未打印的设计为止
    # 打印每个设计后，都将其移到列表completed_models

    while unprinted_design:
        current_design = unprinted_design.pop()

        # 模拟根据设计制作3D打印模型的过程
        completed_models.append(current_design)


def show_completed_models(completed_models):
    # 显示打印好的所有模型
    print('\nThe following models have been printed:')
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)