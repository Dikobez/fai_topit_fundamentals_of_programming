# 2.1
print('2.1')
import copy

original = [
    ["Python", 5],
    ["Algorithms", 4],
]

alias = original
shallow = original.copy()
deep = copy.deepcopy(original)


def print_state(step_name):
    print(f"\n{'=' * 20} {step_name} {'=' * 20}")

    print("\n[ Структуры данных ]")
    print(f"original: {original}")
    print(f"alias:    {alias}")
    print(f"shallow:  {shallow}")
    print(f"deep:     {deep}")

    print("\n[ Идентификаторы (id) внешних списков ]")
    print(f"original: {id(original)}")
    print(f"alias:    {id(alias)}")
    print(f"shallow:  {id(shallow)}")
    print(f"deep:     {id(deep)}")

    print("\n[ Идентификаторы первых вложенных списков ]")
    print(f"original[0]: {id(original[0])}")
    print(f"alias[0]:    {id(alias[0])}")
    print(f"shallow[0]:  {id(shallow[0])}")
    print(f"deep[0]:     {id(deep[0])}")

    print("\n[ Идентификаторы объектов, содержащих первую оценку ]")
    print(f"original[0]: {id(original[0])}")
    print(f"alias[0]:    {id(alias[0])}")
    print(f"shallow[0]:  {id(shallow[0])}")
    print(f"deep[0]:     {id(deep[0])}")

    print("\n(Сама оценка - целое число)")
    print(f"original[0][1]: {id(original[0][1])}")
    print(f"alias[0][1]:    {id(alias[0][1])}")
    print(f"shallow[0][1]:  {id(shallow[0][1])}")
    print(f"deep[0][1]:     {id(deep[0][1])}")


original.append(["Databases", 5])
print_state('Первое изменение')

original[0][1] = 3
print_state('Второе изменение')

# 2.2
print('\n2.2')
wrong_matrix = [[0] * 3] * 3
wrong_matrix[0][0] = 1

print('wrong_matrix', wrong_matrix)
print('id:', id(wrong_matrix[0]), id(wrong_matrix[1]), id(wrong_matrix[2]))

correct_matrix = [[0] * 3 for _ in range(3)]
correct_matrix[0][0] = 1
print('correct_matrix', correct_matrix)
print('id:', id(correct_matrix[0]), id(correct_matrix[1]), id(correct_matrix[2]))
