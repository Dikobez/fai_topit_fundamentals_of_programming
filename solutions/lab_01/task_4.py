student = "Анна Смирнова"
course = "Основы программирования на Python"
completed = 7
total = 10

# 1, 2
print("\n1,2.")
name = student[:4]
surname = student[5:]
print(name[0], name[-1])

# 3
print("\n3.")
print(student.upper())
print(student.lower())

# 4
print("\n4.")
print(f'{name[0]}.{surname[0]}.')

# 5
print("\n5.")
print(course[::-1])

# 6
print("\n6.")
percent = (completed / total) * 100
res_percent = "%s - %s: %d/%d (%.1f%%)" % (student, course, completed, total, percent)
print('%:', res_percent)

res_format = "{} — {}: {}/{} ({:.1f}%)".format(student, course, completed, total, percent)
print("format:", res_format)

res_fstring = f"{student} — {course}: {completed}/{total} ({percent:.1f}%)"
print("f-строка:", res_fstring)

# 7
print("\n7.")
symbol = "Я"
print(symbol, ord(symbol), chr(ord(symbol)), symbol.encode("utf-8"), len(symbol.encode("utf-8")), sep='\n')

# 8 
# student[0] = "О" # Ошибка: TypeError: 'str' object does not support item assignment
