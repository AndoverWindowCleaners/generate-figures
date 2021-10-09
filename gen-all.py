import os

for file in os.listdir('./'):
    if file.endswith('.py') and file != 'gen-all.py':
        print(file)
        os.system('python ' + file)