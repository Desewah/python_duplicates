# importing pandas package
import pandas as pd

# making dataframe from csv file
df = pd.read_csv("files/employees.csv")

# dropping all duplicate values in the first name column
df.drop_duplicates(subset = ["First Name"], keep = "first", inplace = True)

new_df = df
# saving the df and returns the new file without the duplicates
new_df.to_csv("files/output.csv")