import os

filenames = {'LING 1', 'CYBER 454', 'HCDD 412'}
try:
    for name in filenames:
        os.mkdir(name)
        print(f"Directory '{name}' created successfully.")
except FileExistsError:
    print("One of the directories already exsists")
