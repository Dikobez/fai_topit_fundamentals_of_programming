import sys
import weakref

# 3.1
print('=== 3.1 ===')
data = [1, 2, 3]
print("После создания:", sys.getrefcount(data))

alias = data
print("После создания alias:", sys.getrefcount(data))

container = [data]
print("После помещения в контейнер:", sys.getrefcount(data))

del alias
print("После del alias:", sys.getrefcount(data))

container.clear()
print("После очистки контейнера:", sys.getrefcount(data))

# 3.2
print('\n=== 3.2 ===')


class Record:
    pass


record = Record()
weak_record = weakref.ref(record)

print('record:', weak_record())
del record
print('после del record:', weak_record())

# practise
print("\n=== Практическая задача ===")


class DataRecord:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"DataRecord({self.name})"


registry = weakref.WeakValueDictionary()

obj1 = DataRecord("A")
obj2 = DataRecord("B")
obj3 = DataRecord("C")

registry["key1"] = obj1
registry["key2"] = obj2
registry["key3"] = obj3

print("Изначально в реестре:", list(registry.values()))

del obj3
print("После удаления obj3 в реестре:", list(registry.values()))

del obj2
print("После удаления obj2 в реестре:", list(registry.values()))
