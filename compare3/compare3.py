from pathlib import Path
import pandas as pd
import xlwings as xw

df1 = Path.cwd() / "files" / "initial.xlsx"
df2 = Path.cwd() / "files" / "Final.xlsx"

df_initial = pd.read_excel(df1)
print(df_initial.shape) # check d shape and data

df_final = pd.read_excel(df2)
print(df_final.shape) # notice d diff
print(df_initial.shape == df_final.shape)

# show d diff by merging both dataframes
# We need the index information to highlight the rows in Excel
df_final = df_final.reset_index()
print(df_final.head(2))
# Merge dataframes and add indactor column
df_diff = pd.merge(df_initial, df_final, how="outer", indicator="Exist")
print(df_diff)

# Show only the differnce
df_diff = df_diff.query("Exist != 'both'")
print(df_diff)

# Show only the data we want to highlight
df_highlight = df_diff.query("Exist == 'right_only'")
df_highlight

# Get the row numbers we want to highlight in Excel
highlight_rows = df_highlight['index'].tolist()
print(highlight_rows)



# pandas index starts at 0
# Excel data (w/o header) starts from row 2
first_row_in_excel = 2

highlight_rows = [x + first_row_in_excel for x in highlight_rows]
print(highlight_rows)




