# -*- coding: utf-8 -*-

from datetime import datetime

"""
This class Warehouse row as a separate entity, it models the row
as a dictionary with the column header as its key
"""
class Warehouse:
    def __init__(self, dataset):
        self.dataset = dataset

    def obsolete(self):
        """
        Checks for the expiry date using the available metrics and
        adds the key 'obsolete' to the existing dataset of each 
        individual warehouse
        """
        warehouse_date_obj = datetime.strptime(self.dataset['date'], '%Y-%m-%d')
        warehouse_date = datetime.strftime(warehouse_date_obj, '%Y-%m-%d')

        check_date_obj = datetime.strptime('2021-01-01', '%Y-%m-%d')
        check_date = datetime.strftime(check_date_obj, '%Y-%m-%d')

        if warehouse_date < check_date:
            self.dataset['obsolete'] = 'TRUE'
        else:
            self.dataset['obsolete'] = 'FALSE'

    def get_data(self):
        return self.dataset

"""
The class Output models the entire dataset and prepares data
for output
"""
class Output:
    def __init__(self):
        self.ware_data = []

    def add_data(self, warehouse_data):
        self.ware_data.append(warehouse_data)

    def header(self):
        """ Returns the column header values of the new data set
            in the case of outputing to a csv file
         """
        for ix in self.ware_data:
            return list(ix.keys())

    def items(self):
        return self.ware_data