# -*- coding: utf-8 -*-

import csv
from read_write import write_to_csv, write_to_json
from model import Output, Warehouse

def main():
    print("Reading from file...")
    out = Output()
    with open("python hands-on - dataset.csv", 'r') as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            ware = Warehouse(dict(row))
            ware.obsolete()
            # print(ware.get_data())
            out.add_data(ware.get_data())
            # print(ware.obselete())
            # print(dict(row))
    # print(out.header())
    # print(out.items())

    fields = out.header()
    mydict = out.items()

    # name of csv file  
    # filename = "output.csv"
        
    # writing to csv file  
    write_to_csv(fields, mydict)

    # converting and writing as json format
    write_to_json(mydict)
    

if __name__ == '__main__':
    main()