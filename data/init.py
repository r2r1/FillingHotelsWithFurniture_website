
import json
import pandas as pd
import numpy as np
# считываем Excel-таблицу
df = pd.read_excel("data/data.xlsx")
# преобразовываем таблицу в словарь
dict_table = df.to_dict("records")
# записываем словарь в файл
with open("Pages/data.json", "w") as file:
    file.write(json.dumps(dict_table))
  
for i in dict_table:
    print(i)