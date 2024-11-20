from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ITable (  ICompositeObject, IDocumentObject) :
    """
    Interface for a table object in a document.
    """
    @property

    @abc.abstractmethod
    def Rows(self)->'RowCollection':
        """
        Returns the collection of rows in the table.
        """
        pass


    @property

    @abc.abstractmethod
    def TableFormat(self)->'RowFormat':
        """
        Returns the format of the table.
        """
        pass


    @property

    @abc.abstractmethod
    def LastCell(self)->'TableCell':
        """
        Returns the last cell in the table.
        """
        pass


    @property

    @abc.abstractmethod
    def FirstRow(self)->'TableRow':
        """
        Returns the first row in the table.
        """
        pass


    @property

    @abc.abstractmethod
    def LastRow(self)->'TableRow':
        """
        Returns the last row in the table.
        """
        pass



    @abc.abstractmethod
    def get_Item(self ,row:int,column:int)->'TableCell':
        """
        Returns the cell at the specified row and column.
        """
        pass


    @property
    @abc.abstractmethod
    def Width(self)->float:
        """
        Returns the width of the table.
        """
        pass


    @dispatch

    @abc.abstractmethod
    def AddRow(self)->TableRow:
        """
        Adds a new row to the table.
        """
        pass


    @dispatch

    @abc.abstractmethod
    def AddRow(self ,isCopyFormat:bool)->TableRow:
        """
        Adds a new row to the table, optionally copying the format from the previous row.
        """
        pass


    @dispatch

    @abc.abstractmethod
    def AddRow(self ,isCopyFormat:bool,autoPopulateCells:bool)->TableRow:
        """
        Adds a new row to the table, optionally copying the format from the previous row and auto-populating cells.
        """
        pass


    @dispatch

    @abc.abstractmethod
    def ResetCells(self ,rowsNum:int,columnsNum:int):
        """
        Resets the cells in the table to the specified number of rows and columns.
        """
        pass


    @dispatch

    @abc.abstractmethod
    def ResetCells(self ,rowsNum:int,columnsNum:int,format:RowFormat,cellWidth:float):
        """
        Resets the cells in the table to the specified number of rows and columns, with the specified format and cell width.
        """
        pass



    @abc.abstractmethod
    def ApplyVerticalMerge(self ,columnIndex:int,startRowIndex:int,endRowIndex:int):
        """
        Applies vertical merge to the cells in the specified column, starting from the specified start row index to the specified end row index.
        """
        pass



    @abc.abstractmethod
    def ApplyHorizontalMerge(self ,rowIndex:int,startCellIndex:int,endCellIndex:int):
        """
        Applies horizontal merge to the cells in the specified row, starting from the specified start cell index to the specified end cell index.
        """
        pass


    @property
    @abc.abstractmethod
    def IndentFromLeft(self)->float:
        """
        Returns the indent from the left of the table.
        """
        pass


    @IndentFromLeft.setter
    @abc.abstractmethod
    def IndentFromLeft(self, value:float):
        """
        Sets the indent from the left of the table.
        """
        pass


    @abc.abstractmethod
    def RemoveAbsPosition(self):
        """
        Removes the absolute position of the table.
        """
        pass


