def read_lines(filename: str) -> list[str]:
    """Reads all lines from a file"""
    with open(filename) as f:
        return [x.strip() for x in f.readlines()]
