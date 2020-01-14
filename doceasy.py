"""Helper functions and classes for using docopt and schema"""
import sys
import csv
from typing import IO, Optional

from docopt import docopt
from schema import SchemaError, Use, And, Schema


PositiveInt = And(Use(int), lambda n: n >= 1,
                  error="Value should be an integer and at least 1")


def positive_int(value: str):
    """Extracts a positive integer from a string.

    Raises ValueError if the string does not contain a positive integer.
    """
    integer = int(value)
    if integer < 1:
        raise ValueError(f"invalid literal for a positive integer: '{value}'")
    return integer


class File:
    """Validator that creates file objects for command line files or '-'.
    """
    def __init__(self, mode: str = 'r', default: Optional[str] = None):
        assert 'b' not in mode
        self.mode = mode
        self.default = default

    def validate(self, filename: Optional[str]) -> IO:
        """Validate the filename and return the associated file object."""
        filename = filename or self.default

        if filename == '-':
            if any(m in self.mode for m in ['w', 'a', 'x']):
                return sys.stdout
            return sys.stdin

        if filename is None:
            raise SchemaError("Invalid object to create a file: '{filename}'")

        try:
            return open(filename, mode=self.mode)
        except Exception as err:
            raise SchemaError(str(err)) from err


class CsvFile(File):
    """Validate and create a csv input/output file.

    If dict_args is not None, a DictReader/-Writer will be created.
    """
    def __init__(self, *args, dict_args: dict = None, **kwargs):
        super().__init__(*args, **kwargs)
        self.dict_args = dict_args

    def validate(self, filename: Optional[str]):
        stream = super().validate(filename)

        if any(m in self.mode for m in ['w', 'a', 'x']):
            if self.dict_args is not None:
                return csv.DictWriter(stream, **self.dict_args)
            return csv.writer(stream)

        if self.dict_args is not None:
            return csv.DictReader(stream, **self.dict_args)
        return csv.reader(stream)


def _validate(arguments: dict, schema: Schema) -> dict:
    try:
        return schema.validate(arguments)
    except SchemaError as err:
        sys.exit(f"Invalid argument: {err}")


def _rename_arguments(arguments: dict):
    return {
        key.lower().strip('-').replace('-', '_'): value
        for key, value in arguments.items()
    }


def doceasy(docstring: str, schema: Optional[Schema] = None,
            rename: bool = True, **kwargs) -> dict:
    """Parse the command line arguments."""
    arguments = docopt(docstring, **kwargs)

    if schema is not None:
        arguments = _validate(arguments, schema)

    if rename:
        arguments = _rename_arguments(arguments)

    return arguments
