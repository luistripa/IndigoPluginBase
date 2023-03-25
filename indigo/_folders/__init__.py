from typing import Union

import indigo


class Folder:
    id: int
    name: str
    remoteDisplay: bool

    def replaceOnServer(self) -> None:
        """Updates the folder on the server with the current values."""
        pass

    def refreshFromServer(self) -> None:
        """Refreshes the folder from the server. This is useful if you have changed the folder on the server and want to update the local copy."""
        pass


class FolderList(indigo.List):
    
    def getId(name: str) -> int:
        """Returns the id of the folder with the specified name.
        
        :param name: Name of the folder."""
        pass


class FolderCmds:
    
    def create(name: str) -> 'indigo.Folder':
        """Creates a new folder.
        
        :param name: Name of the new folder."""
        pass

    def delete(id: Union[int, 'indigo.Folder'], deleteAllChildren: bool = False):
        """Deletes the specified folder.
        
        :param id: Id or instance of the folder to delete.
        :param deleteAllChildren: If True, all children of the folder will be deleted as well."""
        pass

    def duplicate(id: Union[int, 'indigo.Folder'], duplicateName: str = None) -> 'indigo.Folder':
        """Duplicates the specified folder.
        
        :param id: Id or instance of the folder to duplicate.
        :param duplicateName: Name of the duplicate folder."""
        pass

    def displayInRemoteUI(id: Union[int, 'indigo.Folder'], value: bool=False):
        """Sets whether the specified folder will be displayed in the remote UI.
        
        :param id: Id or instance of the folder to modify.
        :param display: If True, the folder will be displayed in the remote UI."""
        pass
