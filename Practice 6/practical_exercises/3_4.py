val_str = "100"
val_float = 12.34

print("Тип val_str:", type(val_str))
print("Является ли val_float числом float?:", isinstance(val_float, float))

converted_int = int(val_str)
converted_str = str(val_float)

print("После int():", converted_int, type(converted_int))
print("После str():", converted_str, type(converted_str))