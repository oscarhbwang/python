import pandas as pd
from openpyxl.workbook import workbook

df = pd.read_csv('', header = None)
df.columns = ['First','Last','Address','City','State','Area Code']

print(df.columns)
