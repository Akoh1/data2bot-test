# -*- coding: utf-8 -*-
import csv
import json

def write_to_csv(fields, mydict):
    with open('output.csv', 'w') as csvfile:  
        # creating a csv dict writer object  
        writer = csv.DictWriter(csvfile, fieldnames=fields)  
            
        # writing headers (field names)  
        writer.writeheader()  
            
        # writing data rows  
        writer.writerows(mydict)
    print("Writing to csv...")

def write_to_json(mydict):
    with open("output.json", "w") as outfile:  
        json.dump(mydict, outfile)
    print("Writing to json....")
