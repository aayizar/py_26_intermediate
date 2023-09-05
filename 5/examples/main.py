import os

path = '5\\examples\\'


"""
1 task
"""
# content = 'Hello from my python examples!!!'
# with open(f'{path}first_task.txt', 'w') as f:
#     f.write(content)
    

"""
2 task
"""
# os.mkdir(f"{path}my_directory")
# file_path = os.path.join(f"{path}my_directory", "new_file.txt")

# with open(file_path, 'w')as f:
#     f.write(content)


"""
3 task
"""
# files = os.listdir('5\\')
# print(files)


"""
4 task
"""
if os.path.exists(f".git"):
    print("exist")
else:
    print("not exist")