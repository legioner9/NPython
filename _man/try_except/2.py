def b(value):
    print("-> b")
    print(value + 1)  # ошибка тут


def a(value):
    print("-> a")
    b(value)

try:
    a("10")
except Exception as e:
    print(e.with_traceback)
else:
    print("ok")
finally:
    print("from finally")