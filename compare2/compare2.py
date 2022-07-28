from pathlib import Path # core python module
import pandas as pd
import xlwings as xw

# define filepath
df1 = Path.cwd() / "file" / "May_Report.xlsx"
df2 = Path.cwd() / "file" / "June_Report.xlsx"

#load the dataframes
df_initial = pd.read_excel(df1)
df_final = pd.read_excel(df2)

#testing the code
print(df_initial)

# to highlight the difference
with xw.App(visible=False) as app:
    initial_wb = app.books.open(df1)
    initial_ws = initial_wb.sheets(1)

    updated_wb = app.books.open(df2)
    updated_ws = updated_wb.sheets(1)

    for cell in updated_ws.used_range:
        old_value = initial_ws.range((cell.row, cell.column)).value
        if cell.value != old_value:
            # WARNING: Platform specific (!)
            cell.api.AddComment(f"Value from {initial_wb.name}: {old_value}")
            cell.color = (255, 71, 76)  # light red

    updated_wb.save(Path.cwd() / "file" / "Difference_Highlighted.xlsx")
