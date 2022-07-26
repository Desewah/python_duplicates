import pandas as pd
import numpy as np
dfmay = pd.read_excel("file/May_Report.xlsx")
dfjune = pd.read_excel("file/June_Report.xlsx")
print(dfmay)
# shows that dfmay != dfjune
print(dfmay == dfjune)

comparevalues = dfmay.values == dfjune.values

print(comparevalues)

rows,cols = np.where(comparevalues==False)
# shows the change using arrows which will be saved in anew file hence returning a single file
for item in zip(rows,cols):
    dfmay.iloc[item[0],item[1]] = ' {} --> {} '.format(dfmay.iloc[item[0], item[1]], dfjune.iloc[item[0],item[1]])


dfmay.to_excel('file/output.xlsx', index=False,header=True)
