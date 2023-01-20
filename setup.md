# Setup

## API setup:
In the root dir `backend-challenge`:
`docker-compose up -d --build`

## CLI setup:
In `/cli`:
`pip install -r requirements.txt`

## API docs:
(After docker containers are running)
http://localhost:8080/datasets/ui

# Testing:
In `/backend/tests`:
`pytest` (If pytest isn't installed, simply run `pip install pytest`)

# CLI:
Navigate to the `/cli` dir:
`python sesam_cli.py --help`
- List all: `... get`
- List one: `... get <ID>`
- Create: `... create <path to dataset>`
- Delete: `... delete <ID>`
- Export: `... export <ID>`
