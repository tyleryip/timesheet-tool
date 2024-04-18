# Timesheet Tool

A simple CLI tool to convert annotated time spans into durations.

## Features

The following features have been implemented or are planned for future development:

- [x] Text file timesheet input
- [x] Command prompt timesheet input
- [ ] Total hours

## Installation

To activate the virtual environment, run the following from the root directory: `. .venv/bin/activate`

From the `src` directory, run the following to install dependencies: `pip install -r requirements.txt`

## Usage

You can run the CLI as a normal python file. From the `src` directory, run the following: `python3 main.py`

Instead of pasting your timesheet into the command line, you can also use an input text file: `python3 main.py -i <filename>`

## setuptools

After activating the virtual environment, you can also use setuptools to invoke the CLI directly instead of using Python: `pip install --editable .`

From the `src` directory, simply run `timesheet`.

## References

- [Click](https://click.palletsprojects.com/en/8.1.x/setuptools/#setuptools-integration)
