import pandas as pd

import read_functions as rf
import aux_functions  as af


def import_pses(filepath, sheet : str | int | None = 0,header = 'infer'):
    try:
        file_extension = af.get_extension(filepath)

        if file_extension == "csv":
            return rf.read_pses_csv(filepath,header=header)

        elif file_extension == "xlsx":
            return rf.read_pses_excel(filepath, sheet=sheet,header=header)

    except FileNotFoundError as e:
        print(e)


def import_epks(filepath, sheet : str | int | None = 0):

    try:
        file_extension = af.get_extension(filepath)

        if file_extension == "csv":
            return rf.read_epks_csv(filepath)

        elif file_extension == "xlsx":
            return rf.read_epks_excel(filepath,sheet=sheet)

    except FileNotFoundError as e:
        print(e)


def import_pisystems(filepath, sheet: str | int | None = 0):
    try:
        file_extension = af.get_extension(filepath)

        if file_extension == "csv":
            return rf.read_pisystems_csv(filepath)

        elif file_extension == "xlsx":
            return rf.read_pisystems_excel(filepath, sheet=sheet)

    except FileNotFoundError as e:
        print(e)


def import_phd(filepath, sheet: str | int | None = 0):
    try:
        file_extension = af.get_extension(filepath)

        if file_extension == "csv":
            return rf.read_phd_csv(filepath)

        elif file_extension == "xlsx":
            return rf.read_phd_excel(filepath, sheet=sheet)

    except FileNotFoundError as e:
        print(e)


def import_perfect(filepath, sheet : str | int | None = 0):
    """
    importa un archivo csv o excel perfecto

    Primera columna : Timeframe
    Primera fila : Headers
    """

    try:
        file_extension = af.get_extension(filepath)

        if file_extension == "csv":
            return pd.read_csv(filepath, index_col=0, parse_dates=True)

        elif file_extension == "xlsx":
            return pd.read_excel(filepath, index_col=0,sheet_name=sheet, parse_dates=True)
    except FileNotFoundError as e:
        print(e)


def import_custom(filepath,
                  header: int | None = 0,
                  index: int | None = 0,
                  sheet: str | int | None = 0,
                  ):
    try:
        file_extension = af.get_extension(filepath)

        if file_extension == "csv":

            df_data = pd.read_csv(filepath, header=header, index_col=index, parse_dates=True)
            df_data = df_data.iloc[:, index+1:]
            return df_data

        elif file_extension == "xlsx":

            df_data = pd.read_excel(filepath,header=header, index_col=index, sheet_name=sheet, parse_dates=True)
            df_data = df_data.iloc[:, index + 1:]
            return df_data

    except FileNotFoundError as e:
        print(e)