import click
import json
import requests
import pandas as pd
from tabulate import tabulate


base = "http://localhost:8080/datasets"
cli = click.Group(help="Sesam Backend Task CLI")


@cli.command(help="Use without id to list all", name="get")
@click.argument("id", type=int, required=False)
@click.option("-f", "--format", help="Format the dataset", is_flag=True)
@click.option(
    "-t",
    "--table",
    help="Print the dataset in a table (If the dataset is large, send the output to a file)",
    is_flag=True,
)
def get(id: int, format: bool, table: bool):
    if id:
        dataset = requests.get(f"{base}/{id}").json()
        if format:
            dataset = json.dumps(dataset, indent=4)
        elif table:
            df = pd.DataFrame(dataset)
            dataset = tabulate(df.T, headers="keys", tablefmt="rounded_grid")

        click.echo(dataset)
        return

    ids = requests.get(base).json()
    click.echo(ids)


@cli.command(help="Pass the path to a dataset file.", name="create")
@click.argument("path", type=str, required=True)
def create(path: str):
    with open(path) as json_file:
        dataset = json.load(json_file)
    post_request = requests.post(base, json=dataset)
    click.echo(post_request.json())


@cli.command(help="Delete a dataset by passing its id", name="delete")
@click.argument("id", type=int, required=True)
def delete(id: int):
    delete_response = requests.delete(f"{base}/{id}")
    click.echo(delete_response.json())


@cli.command(help="Export a dataset as an Excel file by passing its id", name="export")
@click.argument("id", type=int, required=True)
@click.option(
    "-o",
    "--output",
    help="Output file/path. Or download with the default name in this directory",
    required=False,
)
def export(id: int, output: str):
    export_response = requests.get(f"{base}/{id}/excel")
    filename = export_response.headers["Content-Disposition"].split("=")[1]
    if output:
        filename = output

    with open(filename, "wb") as excel_file:
        excel_file.write(export_response.content)


if __name__ == "__main__":
    cli()
