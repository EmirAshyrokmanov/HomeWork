immutable_var = 1, 'hello', 2.5, True
print(type(immutable_var))
immutable_var[0] = 4 # Данные из кортежа нельзя изменять,можно только провести сложение и умножение
mutable_var = ([32, 46], 24) + (18, 4)
print(mutable_var)
