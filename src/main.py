import click
import logging
from os import path
from parse import parse_timesheet

@click.command()
@click.option('-i', '--input_filepath', help='input filepath')
@click.option('-d', '--debug', is_flag=True, help="debug mode")
def transform(input_filepath, debug):
    logging.basicConfig(level=10 if debug else 20)
    lines = []
    
    # If no filepath is provided, prompt the user to paste their input directly into the terminal
    if input_filepath is None:
        click.echo("Please paste your timesheet. CTRL+D or CTRL+Z (Windows) to save your timesheet:")
        click.echo("\n--------------TIMESHEET--------------\n")
        while True:
            try:
                line = input()
            except EOFError:
                break
            lines.append(line)
    else:
        try:
            input_file = open(f"{input_filepath}", "r")
            lines = input_file.readlines()
            input_file.close()

        except IOError:
            click.echo(f"Could not open {input_filepath}")

    click.echo("\n--------PARSED TIMESHEET OUTPUT--------\n")
    output = parse_timesheet(lines)
    click.echo(output)

if __name__ == '__main__':
    transform()