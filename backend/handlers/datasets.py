from os import remove

import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

from db.db_module import Dataset


class DatasetHandlers:
    def __init__(self, **kwargs):
        self.engine = db.create_engine(
            "postgresql+psycopg2://sesam:sesam_task@localhost"
        )
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def list_all(self):
        return self.session.query(Dataset.id, Dataset.size).all()

    def get(self, id):
        return self.session.query(Dataset.dataset).filter(Dataset.id == id).one()

    def create(self, data, size):
        new_dataset = Dataset(dataset=data, size=size)
        self.session.add(new_dataset)
        self.session.commit()
        return new_dataset.id

    def delete(self, id):
        self.session.query(Dataset).filter(Dataset.id == id).delete()
        self.session.commit()
        remove(f"exports/dataset{id}.xlsx")
        return id
