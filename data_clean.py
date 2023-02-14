import csv

# Takes as input a file name and, assuming it is a csv file, cleans the data to be used by the model.

def clean(filename):
    file = open(filename)
    csv_reader = csv.reader(file)
    data = []
    results = []

    for row in csv_reader:
        results.append(float(row.pop(-1)))
        data.append(list(map(float, row)))
    return [data, results]

# Takes as input an array and splits the data into quantity partitions. For train, test, and validation set creation.

def split_data(list, quantity):
    return_list = []
    
    for i in range(0, len(list), quantity):
        return_list.append(list[i:i + quantity])
    return return_list