from pathlib import Path


def get_script_path(script_filename: str) -> Path:
    """`Path` object of `script_filename`

    https://stackoverflow.com/a/3430395

    EXAMPLE: my_path = get_script_path(__file__); fname = str(my_path / 'hello.txt')
    """
    return Path(script_filename).parent.resolve()
