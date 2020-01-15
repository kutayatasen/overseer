import openpyxl
import psycopg2

host = "local"
user = "postgres"
password = "default"
db_name = "database"
query =  input("Please write your SQL query")
file_location = input("Where to save excel file")

psql_connection = psycopg2.connect(host=host, user=user, password=password, database=db_name)
cursor = psql_connection.cursor()
cursor.execute(query)
data = cursor.fetchall()
cursor.close()
wb = openpyxl.Workbook()
sheet = wb.active

for rowno, row in enumerate(data, start = 1):
    for colno, cell_value in enumerate(row, start = 1):
        sheet.cell(row = rowno, column = colno).value = cell_value

wb.save(file_location)

print("File successfully saved..")