try:
    from rich import print as rprint
    from rich import print_json as rprint_json
except ImportError:
    def rprint(s): print(s)
    def rprint_json(s): print(s)