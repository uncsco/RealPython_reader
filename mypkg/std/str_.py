from string import whitespace as WHITESPACE


def str_remove_whitespace(s: str) -> str:
    """Remove *whitespace* from string `s`

    >>> str_remove_whitespace(' abc d ef  ')
    'abcdef'
    """
    # // `string.whitespace` https://stackoverflow.com/questions/16474848/python-compare-strings-ignore-special-characters
    return ''.join(c for c in s if c not in WHITESPACE)


def get_filename_ext(fname: str) -> str:
    """Get `fname`'s extension

    >>> get_filename_ext('hello_world.txt')
    'txt'
    """
    return fname.rsplit('.', 1)[1].lower()
