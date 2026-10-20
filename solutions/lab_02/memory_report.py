import sys
import tracemalloc


def measure_scenario(name, creation_func, num_elements):
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


def generate_report():
    results = []

    # 5.1
    results.append(measure_scenario("Пустой список", list, 0))
    results.append(measure_scenario("Список (10 элементов)", lambda: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))
    results.append(measure_scenario("Кортеж (10 элементов)", lambda: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 10))
    results.append(measure_scenario("Строка (10 символов)", lambda: "0123456789", 10))
    results.append(measure_scenario("Целое число", lambda: 42, 1))
    results.append(measure_scenario("None", lambda: None, 1))

    # 5.3
    results.append(measure_scenario("list(range(100_000))", lambda: list(range(100_000)), 100_000))
    results.append(measure_scenario("range(100_000)", lambda: range(100_000), 100_000))

    return results


def report(results):
    print("=" * 30 + " 5.4 Практическая задача " + "=" * 30)
    print(f"{'Сценарий':<25} | {'Элементов':<10} | {'Размер (Б)':<10} | {'Тек. (КБ)':<10} | {'Пик (КБ)':<10}")
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


if __name__ == "__main__":
    data = generate_report()
    report(data)
