from __future__ import annotations

from typing import TYPE_CHECKING

import indigo


if TYPE_CHECKING:
    import indigo._types as _types


class Folder:
    id: int
    name: str
    remoteDisplay: bool

    def replaceOnServer(self) -> None:
        """Updates the folder on the server with the current values."""
        ...

    def refreshFromServer(self) -> None:
        """Refreshes the folder from the server. This is useful if you have changed the folder on the server and want to update the local copy."""
        ...


class FolderList(indigo.List):
    
    def getId(name: str) -> int:
        """Returns the id of the folder with the specified name.
        
        :param name: Name of the folder."""
        ...


class FolderCmds:
    
    def create(name: str) -> 'indigo.Folder':
        """Creates a new folder.
        
        :param name: Name of the new folder."""
        ...

    def delete(id: _types.folderType, deleteAllChildren: bool = False):
        """Deletes the specified folder.
        
        :param id: ID or instance of the folder to delete.
        :param deleteAllChildren: If True, all children of the folder will be deleted as well."""
        ...

    def duplicate(id: _types.folderType, duplicateName: str = None) -> 'indigo.Folder':
        """Duplicates the specified folder.
        
        :param id: ID or instance of the folder to duplicate.
        :param duplicateName: Name of the duplicate folder."""
        ...

    def displayInRemoteUI(id: _types.folderType, *, value: bool):
        """Sets whether the specified folder will be displayed in the remote UI.
        
        :param id: ID or instance of the folder to modify.
        :param display: If True, the folder will be displayed in the remote UI."""
        ...
