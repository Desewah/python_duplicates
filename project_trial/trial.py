import csv
# writes a user's input to csv

with open("files_trial/google_stock_data.csv", "w+") as file:
    my_file = csv.writer(file)
    my_file.writerow(["Id", "Activity", "Description", "Level"])

