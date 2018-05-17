import csv

def read(file_location):
#   with open(file_location, 'r+', newline='') as csv_file:
    with open(file_location, 'r+') as csv_file:
        reader = csv.reader(csv_file)
        return [row for row in reader]
def write(file_location, rows):
#   with open(file_location, 'w+', newline='') as csv_file:  
    with open(file_location, 'w+') as csv_file:
        writer = csv.writer(csv_file)
        for row in rows:
            writer.writerow(row)

def raw_test():
    columns = int(raw_input("How many columns do you want to write? "))
    input_rows = []
    keep_going = True
    while keep_going:
        input_rows.append([raw_input("column {}: ".format(i + 1)) for i in range(0, columns)])
        ui_keep_going = raw_input("continue? (y/N): ")
        if ui_keep_going != "y":
            keep_going = False

    print(str(input_rows))
    write('raw.csv', input_rows)
    written_value = read('raw.csv')
    print(str(written_value))

raw_test()
