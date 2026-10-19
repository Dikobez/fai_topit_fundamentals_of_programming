import gc

# 4.1
print('4.1 -------------------')
first = []
second = []

first.append(second)
second.append(first)

print("first ссылается на second:", first[0] is second)
print("second ссылается на first:", second[0] is first)

print("\n--- Состояние GC ---")
print("Автоматический сборщик включен:", gc.isenabled())
print("Пороги поколений:", gc.get_threshold())
print("Статистика поколений:")
for i, stat in enumerate(gc.get_stats()):
    print(f"  Поколение {i}: {stat}")

id_first = id(first)
id_second = id(second)
print(f"\nID объекта first:  {id_first}")
print(f"ID объекта second: {id_second}")

del first, second
print("\nИмена first и second удалены.")

collected = gc.collect()
print(f"Ручной вызов gc.collect() собрал объектов: {collected}")


# 4.2
print("\n4.2 --- Отключение GC ---")
gc.disable()
print("Автоматический GC отключен. Статус:", gc.isenabled())

cycles = []
for i in range(3):
    a = [i]
    b = [i]
    a.append(b)
    b.append(a)
    cycles.append(a)

del cycles
del a, b

collected_manual = gc.collect()
print(f"Собрано объектов при ручном вызове: {collected_manual}")

gc.enable()
print("Автоматический GC снова включен:", gc.isenabled())


# 4.3
print("\n4.3 --- Практическая задача: Граф ---")

gc.collect()

node_a = {"name": "A"}
node_b = {"name": "B"}
node_c = {"name": "C"}
node_d = {"name": "D"}

# цикл A -> B -> C -> A
node_a["next"] = node_b
node_b["next"] = node_c
node_c["next"] = node_a

# независимый узел
node_d["next"] = None

print("Связи в графе:")
print(f"  {node_a['name']} -> {node_a['next']['name']}")
print(f"  {node_b['name']} -> {node_b['next']['name']}")
print(f"  {node_c['name']} -> {node_c['next']['name']}")
print(f"  {node_d['name']} -> {node_d['next']}")

del node_a, node_b, node_c

collected_graph = gc.collect()
print(f"\nПосле удаления внешних ссылок на A, B, C сборщик мусора уничтожил: {collected_graph} объектов.")

print(f"Независимый узел {node_d['name']} доступен.")
