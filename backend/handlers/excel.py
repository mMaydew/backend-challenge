from os.path import exists

from pandas import DataFrame

from handlers.datasets import DatasetHandlers


def get_bytes(path: str) -> bytes:
    """Reads Excel file into memory.

    Args:
        path (str): Path to Excel file

    Returns:
        bytes: Excel file as bytes
    """
    with open(path, "rb") as excel_file:
        return excel_file.read()


def dict_to_excel(id: int):
    """Gets the dataset for the given ID and converts it to an Excel file.

    Args:
        id (int): ID of the requested dataset

    Returns:
        id (int): ID of the requested dataset
        None: If the dataset doesn't exist
    """
    output_file = f"exports/dataset{id}.xlsx"

    if exists(output_file):
        return id

    dataset_init = DatasetHandlers()
    dataset = dataset_init.get(id)
    if not dataset:
        return dataset

    DataFrame(dataset[0]).to_excel(output_file)

    return id
