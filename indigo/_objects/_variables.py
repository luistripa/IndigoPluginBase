import dataclasses
from typing import Dict, Any


__all__ = [
    'Variable',
]


@dataclasses.dataclass
class Variable:
    # See https://wiki.indigodomo.com/doku.php?id=indigo_2021.1_documentation:variable_class

    id: int
    folderId: int
    name: str
    readOnly: bool
    remoteDisplay: bool
    sharedProps: Dict[str, Any]
    value: str

    def getValue(self, type: Any, default: bool = None) -> Any:
        """
        Returns the variable value as the specified type.

        If the variable value cannot be converted to the specified type, the default value will be returned.

        If the default value is not specified, the following default values will be used:
        int type -> 0
        float type -> 0
        bool type -> False

        :param type: The type to convert the variable value to.
        :param default: The default value to return if the variable value cannot be converted to the specified type.
        :return: The variable value as the specified type or the default value if the variable value cannot be converted.
        """
        pass