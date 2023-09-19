import subprocess

# Путь к вашему Python-скрипту
path = "9/b.py"

# Список аргументов, которые вы хотите передать скрипту
args = ["5", "4"]

# Выполнение скрипта с передачей аргументов
try:
    result = subprocess.run(["python", path] + args, capture_output=True, text=True, check=True)
    # В результате будет содержимое stdout скрипта
    print(result.stdout, end='')
except subprocess.CalledProcessError as e:
    # Обработка ошибки, если скрипт завершился с ошибкой
    print("Ошибка выполнения скрипта:", e)
