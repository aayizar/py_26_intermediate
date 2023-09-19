import os

""" Создание папки если его нет

import os

folder_name = '9/example2'

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print('Folder created')
else:
    print('Folder alredy exist')
"""


''' Ошибки при работе с модулем
folder_name = '10'

try: 
    os.mkdir(folder_name)
except OSError as error:
    print('error:', error)'''


""" Переименовать файл
try:
    last_name = '10'
    new_name = '9'
    os.rename(last_name, new_name)
except OSError as error:
    print(error)"""


""" Удалить директорию
path = "9/example2"
os.rmdir(path)

os.remove('9/b.py')
"""


''' Смена папки и показ всех файлов внутри
os.chdir('9/')
dir_name = 'example'
result = os.listdir(dir_name)

for element in result:
    print(element)'''
    
    
""" Показать на экран текущую папку
print(os.getcwd())
os.chdir('9')
print(os.getcwd())"""

''' Функция join
folder = '9'
file = 'a.py'

path = os.path.join(folder, file)
print("path", path)
# print(open(path, encoding='utf8').read(), end='')
'''


''' Проверка файла или директории
# path = '9/example'
path = '9/a.py'

if os.path.isfile(path):
    print("Is file")
elif os.path.isdir(path):
    print("Is directory")
else:
    print("Path doesn't exist")
'''


''' Абсолютный путь
path = '9/a.py'

abs_path = os.path.abspath(path)
print(abs_path)
'''


''' Получение папки и файла из пути
abs_path = 'C:\Windows\Boot\DVD\PCAT\etfsboot.com'
file_name = os.path.basename(abs_path)
folder_name = os.path.dirname(abs_path)
# print(file_name, folder_name)

folder, file = os.path.split(abs_path)
print(folder, "|||", file)
'''


''' Показать на экран все файлы
def print_all_from_directory(path):
    content = os.listdir(path)
    for element in content:
        abs_path = os.path.join(path, element)
        if os.path.isfile(abs_path):
            print(f'Файл: {abs_path}')
        elif os.path.isdir(abs_path):
            print(f'Папка: {abs_path}')
            print_all_from_directory(abs_path)
        
path = "C:\Windows\Boot"
print_all_from_directory(path)
'''


print("Hello from a.py")