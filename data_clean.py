import csv

def clean(filename):
    file = open(filename)
    csv_reader = csv.reader(file)
    print (type(file))

    data = []
    results = []
    for row in csv_reader:
        results.append(float(row.pop(-1)))
        data.append(list(map(float, row)))
    return [data, results]

def split_data(list, quantity):
    return_list = []
    for i in range(0, len(list), quantity):
        return_list.append(list[i:i + quantity])
    return return_list