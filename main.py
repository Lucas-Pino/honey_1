import pandas as pd

import import_functions as impf
_FILEPATH = "./data/test_file.xlsx"
_FILEPATH2 = "./data/Datos PHD.xlsx"

_EPKSFILE = "./data/Datos EPKS raw.xlsx"
_EPKSFILE2 = "./data/Datos EPKS raw.csv"
_PISYSFILE = "./data/Datos PI System Raw.xlsx"
_PHDFILE = "./data/Datos PHD raw.xlsx"

_CSVFILE = "./data/Datos PHD.csv"


def main():

    # data = impf.import_epks(_EPKSFILE)
    # print(data)

    # data2 = impf.import_epks(_EPKSFILE2)
    # print(data2)

    # data = impf.rf.read_pi_systems_excel(_PISYSFILE,sheet="Dic22")

    data = impf.rf.read_phd_excel(_PHDFILE)

    data = impf.import_custom(_PHDFILE,header=2,index=1)


    print(data)



if __name__ == '__main__':
    main()

