from typing import Callable


def read_lines(filename: str, strip: bool = True) -> list[str]:
    """Reads all lines from a file"""
    with open(filename) as f:
        return [x.strip() if strip else x for x in f.readlines()]


def parse_lines(filename: str, line_parser: Callable[[str], any]) -> list[any]:
    """Reads and parses lines from a file"""
    with open(filename) as f:
        return [line_parser(x.strip()) for x in f.readlines()]
