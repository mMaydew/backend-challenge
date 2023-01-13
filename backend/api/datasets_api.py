import connexion

from handlers.datasets import DatasetHandlers
from handlers import excel


def list_datasets():
    dataset_init = DatasetHandlers()
    all_datasets = dataset_init.list_all()

    return [{"id": dataset[0], "size": dataset[1]} for dataset in all_datasets]


def create_dataset(body):
    dataset_init = DatasetHandlers()
    dataset_id = dataset_init.create(body, connexion.request.headers["content-length"])

    return {"id": dataset_id}


def get_dataset(id):
    dataset_init = DatasetHandlers()
    dataset = dataset_init.get(id)[0]

    return dataset


def delete_dataset(id):
    dataset_init = DatasetHandlers()
    dataset = dataset_init.delete(id)

    return {"id": id}


def export_dataset(id):
    return excel.dict_to_excel(id)
