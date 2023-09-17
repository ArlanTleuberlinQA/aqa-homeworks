import csv

with open('test_file.csv', 'r', ) as f:
    reading = csv.reader(f)
    upd_data = []
    currency_course = 37.5
    for row in reading:
        updated_rows = [int(int(cell) * currency_course) if cell.isdigit() else cell for cell in row]
        upd_data.append(updated_rows)
with open('salaries_uah.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(upd_data)
