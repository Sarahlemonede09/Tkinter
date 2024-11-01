from tkinter.filedialog import askopenfilename
import pandas as pd

caminho_arquivo= askopenfilename(title='Selecione o arquivo em exel para abrir.')

df = pd.read_excel(caminho_arquivo)
print(df)