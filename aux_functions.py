import csv

import pandas as pd


def get_delimiter(filepath, bytes_=4096):
    try:
        """
        Obtiene el separador del archivo CSV
        """
        sniffer = csv.Sniffer()
        data = open(filepath, "r").read(bytes_)
        delimiter = sniffer.sniff(data).delimiter
        return delimiter
    except FileNotFoundError as e:
        print(e)

def get_extension(filename):
    file = filename
    file = file[len(file) - 5:len(file)]

    if ".csv" in file:
        extension = "csv"
    elif ".xlsx" in file:
        extension = "xlsx"
    extension
    return extension

def excel_to_csv(filepath):
    folder = ""
    try:
        data = pd.read_excel(filepath)
        path_name = folder + filepath[:-4] + "csv"
        data.to_csv(path_name,sep=",")
        return path_name
    except FileNotFoundError:
        print("not an excel file")


#def import_epks():
