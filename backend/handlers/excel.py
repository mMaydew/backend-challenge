from os.path import exists

from pandas import DataFrame

from handlers.datasets import DatasetHandlers


def get_bytes(path):
    with open(path, "rb") as excel_file:
        return excel_file.read()


def dict_to_excel(id):
    output_file = f"exports/dataset{id}.xlsx"

    if exists(output_file):
        return get_bytes(output_file)

    dataset_init = DatasetHandlers()
    dataset = dataset_init.get(id)[0]

    DataFrame(dataset).to_excel(output_file)

    return get_bytes(output_file)
