import sys
import tracemalloc


def measure(name, creation_func, num_elements):
    tracemalloc.start()
    obj = creation_func()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return {
        "scenario": name,
        "num_elements": num_elements,
        "outer_size_bytes": sys.getsizeof(obj),
        "current_mem_kb": current / 1024,
        "peak_mem_kb": peak / 1024
    }


def report():
    res = []

    # 5.1
    res.append(measure("Пустой список", list, 0))
    res.append(measure("Список (10 элементов)", lambda: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))
    res.append(measure("Кортеж (10 элементов)", lambda: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 10))
    res.append(measure("Строка (10 символов)", lambda: "0123456789", 10))
    res.append(measure("Целое число", lambda: 42, 1))
    res.append(measure("None", lambda: None, 1))

    # 5.3
    res.append(measure("list(range(100_000))", lambda: list(range(100_000)), 100_000))
    res.append(measure("range(100_000)", lambda: range(100_000), 100_000))

    return res


results = report()
print("=" * 30 + " 5.4 Практическая задача " + "=" * 30)
print(f"{'Объект':<25} | {'Элементов':<10} | {'Размер (Б)':<10} | {'Тек. (КБ)':<10} | {'Пик (КБ)':<10}")
print("-" * 85)

for res in results:
    print(f"{res['scenario']:<25} | "
          f"{res['num_elements']:<10} | "
          f"{res['outer_size_bytes']:<10} | "
          f"{res['current_mem_kb']:<10.2f} | "
          f"{res['peak_mem_kb']:<10.2f}")

print("=" * 85)

peak_list = next(r['peak_mem_kb'] for r in results if r['scenario'] == "list(range(100_000))")
peak_range = next(r['peak_mem_kb'] for r in results if r['scenario'] == "range(100_000)")

ratio = peak_list / peak_range
print(f"\nОтношение пиковой памяти (list / range): {ratio:.1f}")



