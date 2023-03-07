

__all__ = [
    'Dict',
    'List',
]


class List(list):
    """Indigo-specific list class."""
    def to_list(self) -> list:
        # TODO: Change this to support simulation
        return list()


class Dict(dict):
    """Indigo-specific dict class."""
    def to_dict(self) -> dict:
        # TODO: Change this to support simulation
        return dict()
