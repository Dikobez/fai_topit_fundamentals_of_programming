import sys
import tracemalloc

print("=" * 50)
print("5.1 Размер отдельных объектов")
print("=" * 50)

empty_list = []
list_10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tuple_10 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
str_10 = "0123456789"
int_obj = 42
none_obj = None

objects = {
    "Пустой список": empty_list,
    "Список из 10 int": list_10,
    "Кортеж из 10 int": tuple_10,
    "Строка из 10 символов": str_10,
    "Целое число": int_obj,
    "Объект None": none_obj
}

for name, obj in objects.items():
    print(f"{name:25} | Размер: {sys.getsizeof(obj):4} байт")

print("\n" + "=" * 50)
print("5.2 Рост списка")
print("=" * 50)

growing_list = []
prev_size = sys.getsizeof(growing_list)
print(f"Длина: {len(growing_list):3} | Размер: {prev_size} байт")

for i in range(100):
    growing_list.append(i)
    current_size = sys.getsizeof(growing_list)

    if current_size != prev_size:
        print(f"Длина: {len(growing_list):3} | Размер: {current_size} байт")
        prev_size = current_size

print("\n" + "=" * 50)
print("5.3 Измерение через tracemalloc")
print("=" * 50)


def measure_memory(description, creation_func):
    tracemalloc.start()

    obj = creation_func()

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Сценарий: {description}")
    print(f"  Текущая память: {current / 1024:.2f} КБ")
    print(f"  Пиковая память: {peak / 1024:.2f} КБ")
    print(f"  Размер объекта: {sys.getsizeof(obj)} байт\n")

    return peak


peak_list = measure_memory(
    "list(range(100_000))",
    lambda: list(range(100_000))
)

peak_range = measure_memory(
    "range(100_000)",
    lambda: range(100_000)
)

print(f"Отношение пиковой памяти (list / range): {peak_list / peak_range:.1f}")
