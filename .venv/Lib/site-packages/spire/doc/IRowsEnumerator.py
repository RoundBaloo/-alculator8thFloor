from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IRowsEnumerator (abc.ABC) :
    """
    Interface for enumerating rows in a table.
    """
    @abc.abstractmethod
    def Reset(self):
        """
        Reset the enumerator to the beginning.
        """
        pass


    @abc.abstractmethod
    def NextRow(self)->bool:
        """
        Move to the next row.
        Returns:
            bool: True if there is a next row, False otherwise.
        """
        pass



    @abc.abstractmethod
    def GetCellValue(self ,columnName:str)->'SpireObject':
        """
        Get the value of a cell in the current row.
        Args:
            columnName (str): The name of the column.
        Returns:
            SpireObject: The value of the cell.
        """
        pass


    @property

    @abc.abstractmethod
    def ColumnNames(self)->List[str]:
        """
        Get the names of all columns in the table.
        Returns:
            List[str]: The names of the columns.
        """
        pass


    @property
    @abc.abstractmethod
    def RowsCount(self)->int:
        """
        Get the total number of rows in the table.
        Returns:
            int: The number of rows.
        """
        pass


    @property
    @abc.abstractmethod
    def CurrentRowIndex(self)->int:
        """
        Get the index of the current row.
        Returns:
            int: The index of the current row.
        """
        pass


    @property

    @abc.abstractmethod
    def TableName(self)->str:
        """
        Get the name of the table.
        Returns:
            str: The name of the table.
        """
        pass


    @property
    @abc.abstractmethod
    def IsEnd(self)->bool:
        """
        Check if the enumerator has reached the end of the table.
        Returns:
            bool: True if the end is reached, False otherwise.
        """
        pass


    @property
    @abc.abstractmethod
    def IsLast(self)->bool:
        """
        Check if the current row is the last row in the table.
        Returns:
            bool: True if it is the last row, False otherwise.
        """
        pass


