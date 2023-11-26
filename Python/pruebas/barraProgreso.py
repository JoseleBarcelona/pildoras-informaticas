from tqdm import tqdm
import time
elementos=range(100)
for i in tqdm(elementos, desc='Progresando', unit='i'):
    time.sleep(0.1)
print('\nPrograma cargado correctamente')