import os.path

if os.path.exists("z") and os.path.isdir('z'):
    print("O diretório z existe.")
else:
    print("O diretório z não existe ou não é um diretório.")