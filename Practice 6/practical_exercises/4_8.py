import os

path_to_delete = "copied_sample.txt"

if os.path.exists(path_to_delete):
    print(f"Файл '{path_to_delete}' найден.")
    
    if os.access(path_to_delete, os.W_OK):
        os.remove(path_to_delete)
        print(f"Файл '{path_to_delete}' успешно удален.")
    else:
        print(f"Ошибка: Нет прав на запись/удаление файла '{path_to_delete}'.")
else:
    print(f"Ошибка: Файл '{path_to_delete}' не существует.")