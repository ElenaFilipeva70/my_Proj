from typing import Any, Dict, List

import pandas as pd


def get_read_csv(path_file_csv: str) -> List[Dict[str, Any]]:
    """Функция чтения CSV-файла"""
    try:
        df_csv = pd.read_csv(path_file_csv, delimiter=";")
    except Exception as e:
        print(type(e).__name__)
        return []
    dict_read_csv = df_csv.to_dict(orient="records")
    return dict_read_csv


def get_read_excel(path_file_excel: str) -> List[Dict[str, Any]]:
    """Функция чтения EXCEL-файла"""
    try:
        df_xls = pd.read_excel(path_file_excel)
        # print(df_xls.shape)
        # print(df_xls.head())
    except Exception as e:
        print(type(e).__name__)
        return []
    dict_read_excel = df_xls.to_dict(orient="records")
    return dict_read_excel


# base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# path_file_csv = os.path.join(base_dir, "data", "transactions.csv")
# path_file_excel = os.path.join(base_dir, "data", "transactions_excel.xlsx")
# read_csv_transaction = get_read_csv(path_file_csv)
# read_excel_transaction = get_read_excel(path_file_excel)
