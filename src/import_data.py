import pandas as pd
from .clean_dataframe import clean_dataframe


def import_airport_data(list_files):
    dtype = {
        "ANMOIS": "str",
        "APT": "str",
        "APT_NOM": "str",
        "APT_ZON": "str"
    }
    temp = []
    for file in list_files:
        df = pd.read_csv(file, sep=';', dtype=dtype)
        temp.append(clean_dataframe(df))
    return pd.concat(temp)


def import_compagnies_data(list_files):
    dtype = {
        "ANMOIS": "str",
        "CIE": "str",
        "CIE_NOM": "str",
        "CIE_NAT": "str",
        "CIE_PAYS": "str"
    }
    temp = []
    for file in list_files:
        df = pd.read_csv(file, sep=';', dtype=dtype)
        temp.append(clean_dataframe(df))
    return pd.concat(temp)


def import_liaisons_data(list_files):
    dtype = {
        "ANMOIS": "str",
        "LSN": "str",
        "LSN_DEP_NOM": "str",
        "LSN_ARR_NOM": "str",
        "LSN_SCT": "str",
        "LSN_FSC": "str"
    }
    temp = []
    for file in list_files:
        df = pd.read_csv(file, sep=';', dtype=dtype)
        temp.append(clean_dataframe(df))
    return pd.concat(temp)