import os
import pathlib

dir_atual = pathlib.Path(__file__).parent.absolute()
files = os.listdir(dir_atual)
text_to_remove = input('Texto a ser removido: ')

for file in files:
  old_file = os.path.join(dir_atual, file)
  new_file = os.path.join(dir_atual, file.replace(text_to_remove, '').strip())

  os.rename(old_file, new_file)