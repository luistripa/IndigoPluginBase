from __future__ import annotations

from typing import Any, Union, Type

import indigo
import dataclasses


class VariableList(indigo.List):

    folders: indigo.FolderList
    folder: indigo.FolderCmds

    def __iter__(self, filter: str = "") -> indigo.List["indigo.Variable"]: ...


@dataclasses.dataclass
class Variable:
    # See https://wiki.indigodomo.com/doku.php?id=indigo_2021.1_documentation:variable_class

    id: int
    folderId: int
    name: str
    readOnly: bool
    remoteDisplay: bool
    sharedProps: indigo.Dict[str, Any]
    value: str

    def getValue(self, type: Type[Union[int, float, bool]], default: Any = None) -> Union[int, float, bool]:
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
        ...
