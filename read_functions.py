import pandas as pd


"""
filepath : ruta de los archivos
df_data : donde se guardan los datos de los archivos
"""


def read_pses_excel(filepath, index_col=None, sheet: str | int | None = 0, header='infer'):
    try:
        df_data = pd.read_excel(filepath, parse_dates=[['Date', 'Time']], index_col=index_col, header=header, sheet_name=sheet)
        df_data.rename(columns={'Date_Time': 'Timestamp'}, inplace=True)
        df_data.set_index('Timestamp', inplace=True)
        df_data.rename(columns=lambda col : col.split('/')[0], inplace=True)
        return df_data
    except FileNotFoundError as e:
        print(e)


def read_pses_csv(filepath, index_col=None, header='infer'):
    try:
        df_data = pd.read_csv(filepath, parse_dates=[['Date', 'Time']], index_col=index_col, header=header)
        df_data.rename(columns={'Date_Time': 'Timestamp'}, inplace=True)
        df_data.set_index('Timestamp', inplace=True)
        df_data.rename(columns=lambda col : col.split('/')[0], inplace=True)
        return df_data
    except FileNotFoundError as e:
        print(e)


def read_uniformance(filepath, index_col=None, header='infer', sheet_name=None):
    try:
        df_data = pd.read_excel(filepath, index_col=index_col, header=header, sheet_name=sheet_name)
        df_data.rename(columns=lambda x : x.split('-')[0].strip(), inplace=True)
        return df_data
    except FileNotFoundError as e:
        print(e)


def read_epks_excel(filepath, sheet: str | int | None = 0):
    try:
        df_data = pd.read_excel(filepath, index_col=0, sheet_name=sheet, parse_dates=[['Date', 'Time']], thousands=',')
        df_data.index.name = 'Timestamp'
        df_data = df_data.iloc[::-1]    # invierte el orden del timestamp para que sea incremental
        return df_data
    except FileNotFoundError as e:
        print(e)


def read_epks_csv(filepath):
    try:
        df_data = pd.read_csv(filepath, engine='python', index_col=0, parse_dates=[["Date","Time"]], thousands=',')
        df_data.index.name = 'Timestamp'
        df_data = df_data.iloc[::-1]    # invierte el orden del timestamp para que sea incremental
        return df_data
    except FileNotFoundError as e:
        print(e)


def read_pisystems_excel(filepath, sheet: str | int | None = 0):
    """
    Lee archivos de pi systems en excel
    Recive el path del archivo
    y el numero de  hoja que se quiere leer
    tambien se le puede dar el dia en formato "Jan01"

    """
    try:
        df_data = pd.read_excel(filepath, index_col=2, header=1, parse_dates=True, sheet_name = sheet)
        df_data = df_data.drop(df_data.columns[[0, 1, 3]], axis=1)
        return df_data
    except FileNotFoundError as e:
        print(e)


def read_pisystems_csv(filepath):
    """
        Lee archivos de pi systems en formato csv
        Recive el path del archivo

        """
    try:
        df_data = pd.read_csv(filepath, index_col=2, header=1, parse_dates=True)
        df_data = df_data.drop(df_data.columns[[0, 1, 3]], axis=1)
        return df_data
    except FileNotFoundError as e:
        print(e)


def read_phd_excel(filepath,  sheet : str | int | None = 0):
    try:
        df_data = pd.read_excel(filepath, index_col=1, header=2, sheet_name=sheet, parse_dates=True)
        df_data.iloc[0].name
        df_data = df_data.drop(df_data.iloc[0].name)
        df_data = df_data.drop(df_data.columns[0], axis=1)
        df_data.index.names = ['Timestamp']
        return df_data
    except FileNotFoundError as e:
        print(e)


def read_phd_csv(filepath):
    try:
        df_data = pd.read_csv(filepath, index_col=1, header=2, parse_dates=True)
        df_data.iloc[0].name
        df_data = df_data.drop(df_data.iloc[0].name)
        df_data = df_data.drop(df_data.columns[0], axis=1)
        df_data.index.names = ['Timestamp']
        return df_data
    except FileNotFoundError as e:
        print(e)
