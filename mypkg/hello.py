__all__ = [
    'hello'
]

def hello(s: str) -> str:
    """Print hello...

    >>> hello('Amy')
    'Hello, Amy!!'
    """
    return f'Hello, {s}!!'