try:
    from rich import print as rprint
    from rich import print_json as rprint_json
except ImportError:
    def rprint(s) -> None:
        print(s)
    def rprint_json(s) ->None:
        print(s)

'''
MYPY:

```
error: All conditional function variants must have identical signatures
```

- rprint() should have *same* signature as rich.print
- rprint_json() ...
'''