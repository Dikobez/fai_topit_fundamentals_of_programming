### exp A
print('=== exp A ===')
a = 10
b = a

print(a, b)
print(id(a), id(b))

a += 1

print(a, b)
print(id(a), id(b))

### exp B
print('\n=== exp B ===')
first = [10, 20]
second = first

print(id(a), id(b))
print(first, second)
print(id(first), id(second))

second.append(30)

print(first, second)
print(id(first), id(second))

### Added
print('\n=== extra ===')
second = [10, 20]
print('==', first == second)
print('is', first is second)
second.append(40)
print('Первый после изменения второго:', first)
print(second)
print(id(first), id(second))

### Practise
print('\n                                    Практическая задача')
import copy

config1 = {
    "name": "Учебный проект Альфа",
    "participants": ["Алексей", "Мария"],
    "launch_params": ["--debug", ["--port", "8080", "--env", "dev"]]
}

print("=== ПРОСТОЕ ПРИСВАИВАНИЕ ===")
print("Исходная config1: ", config1)

config2_shared = config1
config2_shared["participants"].append("Иван")
config2_shared["launch_params"][1][1] = "9090"

print("\nПосле изменения config2_shared:")
print("config1:        ", config1)
print("config2_shared: ", config2_shared)

config3_independent = copy.deepcopy(config1)

assert config1 is not config3_independent, "Конфигурации ссылаются на один объект"
assert config1["participants"] is not config3_independent["participants"], "Списки участников общие"
assert config1["launch_params"] is not config3_independent["launch_params"], "Вложенные параметры общие"

config3_independent["name"] = "Учебный проект Бета"
config3_independent["participants"].append("Ольга")
config3_independent["launch_params"][1][1] = "3000"

print("\n=== 2. ПОСЛЕ СОЗДАНИЯ НЕЗАВИСИМОЙ КОПИИ ===")
print("config1:             ", config1)
print("config3_independent: ", config3_independent)

print("\n=== ИТОГ ===")
print(f"1. config1 и config2_shared:")
print(f"   - Оказываются ОБЩИМ объектом (id: {id(config1)} == {id(config2_shared)}).")
print(f"   - Любые изменения в config2_shared автоматически меняют config1.\n")

print(f"2. config1 и config3_independent:")
print(f"   - Оказываются НЕЗАВИСИМЫМИ объектами (id: {id(config1)} != {id(config3_independent)}).")
print(f"   - Вложенные списки также получили разные адреса в памяти:")
print(f"     id вложенного списка config1: {id(config1['launch_params'][1])}")
print(f"     id вложенного списка config3: {id(config3_independent['launch_params'][1])}")
print(f"   - Изменения в config3_independent не влияют на config1.")
