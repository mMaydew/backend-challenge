import connexion
from flask import send_file

from handlers.datasets import DatasetHandlers
from handlers import excel


def list_datasets() -> list:
    """List all dataset ids and sizes

    Returns:
        list: A list of all id and size pairs
    """
    dataset_init = DatasetHandlers()
    all_datasets = dataset_init.list_all()

    return [{"id": dataset[0], "size": dataset[1]} for dataset in all_datasets]


def create_dataset(body) -> dict:
    """Create a new dataset.

    Args:
        body (json): Body from the post request

    Returns:
        dict: id of the created dataset
    """
    dataset_init = DatasetHandlers()
    dataset_id = dataset_init.create(body, connexion.request.headers["content-length"])

    return {"id": dataset_id}


def get_dataset(id: int) -> dict:
    """Get one dataset

    Args:
        id (int): id of the dataset

    Returns:
        dataset (array): The requested dataset
        dict: If the dataset doesn't exist
    """
    dataset_init = DatasetHandlers()
    dataset = dataset_init.get(id)

    if not dataset:
        return {"error": "Dataset doesn't exist"}

    return dataset[0]


def delete_dataset(id: int) -> dict:
    """Delete the requested dataset (and Excel file if it exists)

    Args:
        id (int): id of the dataset

    Returns:
        dict: id of the deleted dataset
    """
    dataset_init = DatasetHandlers()
    dataset = dataset_init.delete(id)

    return {"id": id}


def export_dataset(id: int):
    """Export the requested dataset as an Excel file

    Args:
        id (int): id of the dataset

    Returns:
        octet-stream (binary): Excel file of the dataset
        dict: Error if dataset doesn't exist
    """
    file_creation = excel.dict_to_excel(id)
    if not file_creation:
        return {"error": "Dataset doesn't exist"}

    return send_file(f"exports/dataset{id}.xlsx")
