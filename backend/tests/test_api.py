import requests


base = "http://localhost:8080/datasets"
test_data = [{"test": "data"}]
test_id = 0


class TestAPI:
    """Tests all of the API functionality
    The order in which the tests run also make it so it
    cleans up after itself
    """

    def test_create_dataset(self):
        create_response = requests.post(base, json=test_data)

        global test_id
        test_id = create_response.json()["id"]

        assert create_response.status_code == 200
        assert type(test_id) == int

    def test_list_all(self):
        list_response = requests.get(base)

        test_dataset = next(
            (item for item in list_response.json() if item["id"] == test_id), None
        )

        assert list_response.status_code == 200
        assert test_dataset["id"] == test_id

    def test_list_one(self):
        list_one_response = requests.get(f"{base}/{test_id}")

        assert list_one_response.status_code == 200
        assert list_one_response.json() == test_data

    def test_export(self):
        export_response = requests.get(f"{base}/{test_id}/excel")

        assert export_response.status_code == 200

    def test_delete_one(self):
        delete_response = requests.delete(f"{base}/{test_id}")

        assert delete_response.status_code == 200
        assert delete_response.json()["id"] == test_id
