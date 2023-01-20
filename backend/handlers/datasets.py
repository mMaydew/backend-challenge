from os import remove, environ
from os.path import exists

from sqlalchemy import create_engine as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import NoResultFound

from db.db_module import Dataset


class DatasetHandlers:
    def __init__(self, **kwargs) -> None:
        db_user = environ.get("DB_USER")
        db_pass = environ.get("DB_PASSWORD")
        db_host = environ.get("DB_HOST")

        self.engine = db(f"postgresql+psycopg2://{db_user}:{db_pass}@{db_host}")
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def list_all(self) -> tuple:
        """Database query to get all id and size pairs

        Returns:
            tuple: All id and size pairs
        """
        return self.session.query(Dataset.id, Dataset.size).all()

    def get(self, id: int) -> tuple:
        """Database query to retrieve one dataset

        Args:
            id (int): Dataset id

        Returns:
            None: If the dataset doesn't exist
            tuple: The dataset
        """
        try:
            dataset = self.session.query(Dataset.dataset).filter(Dataset.id == id).one()
        except NoResultFound:
            return None

        return dataset

    def create(self, data: list, size: int) -> int:
        """Database query to create a dataset entry

        Args:
            data (list): The dataset
            size (int): Size of the dataset

        Returns:
            int: Dataset id
        """
        new_dataset = Dataset(dataset=data, size=size)
        self.session.add(new_dataset)
        self.session.commit()
        return new_dataset.id

    def delete(self, id: int) -> int:
        """Database query to delete a dataset (And the Excel file if it exists)
        Still returns the id even if the dataset doesn't exist.
        Should probably change that, but also doesn't hurt anything.

        Args:
            id (int): Dataset id

        Returns:
            int: Dataset id
        """
        self.session.query(Dataset).filter(Dataset.id == id).delete()
        self.session.commit()
        if exists(f"exports/dataset{id}.xlsx"):
            remove(f"exports/dataset{id}.xlsx")

        return id
