from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class MailMergeDataSet (SpireObject) :
    """
    Represents a mail merge data set.
    """
#    @property
#
#    def DataSet(self)->'List1':
#        """
#
#        """
#        GetDllLibDoc().MailMergeDataSet_get_DataSet.argtypes=[c_void_p]
#        GetDllLibDoc().MailMergeDataSet_get_DataSet.restype=c_void_p
#        intPtr = GetDllLibDoc().MailMergeDataSet_get_DataSet(self.Ptr)
#        ret = None if intPtr==None else List1(intPtr)
#        return ret
#



    def Add(self ,dataTable:'SpireObject'):
        """
        Adds a data table to the mail merge data set.

        Args:
            dataTable: The data table to add.
        """
        intPtrdataTable:c_void_p = dataTable.Ptr

        GetDllLibDoc().MailMergeDataSet_Add.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().MailMergeDataSet_Add,self.Ptr, intPtrdataTable)

    def Clear(self):
        """
        Clears the mail merge data set.
        """
        GetDllLibDoc().MailMergeDataSet_Clear.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().MailMergeDataSet_Clear,self.Ptr)

