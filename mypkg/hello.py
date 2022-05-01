__all__ = [
    'hello'
]

def _filter(s: str) -> str:
    """Return first 6 chars

    - [ ] Can be *redefined*
    """
    return s[0:6]

def hello(s: str, do_filter=False ) -> str:
    """Print hello...

    >>> hello('Amy')
    'Hello, Amy!!'
    >>> hello('Barbara', do_filter=True)
    'Hello, Barbar!!'
    """
    return f'Hello, {_filter(s) if do_filter else s}!!'