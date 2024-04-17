import click
import logging
from os import path
from parse import parse_timesheet

@click.command()
@click.option('-i', '--input_filepath', required=True, help='input filepath')
@click.option('-d', '--debug', is_flag=True, help="debug mode")
def transform(input_filepath, debug):
    logging.basicConfig(level=10 if debug else 20)

    if not path.exists(input_filepath):
        click.echo(f'{input_filepath} does not exist')
        return

    try:
        input_file = open(f"{input_filepath}", "r")

        click.echo("PARSED TIMESHEET OUTPUT:")
        output = parse_timesheet(input_file)
        click.echo(output)

        input_file.close()

    except IOError:
        click.echo(f"Could not open {input_filepath}")

if __name__ == '__main__':
    transform()