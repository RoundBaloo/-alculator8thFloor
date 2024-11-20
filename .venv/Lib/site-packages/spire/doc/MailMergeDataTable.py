from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class MailMergeDataTable (SpireObject) :
    """
    Represents a mail merge data table.
    """
    @property

    def GroupName(self)->str:
        """
        Gets the group name of the mail merge data table.

        Returns:
            str: The group name.
        """
        GetDllLibDoc().MailMergeDataTable_get_GroupName.argtypes=[c_void_p]
        GetDllLibDoc().MailMergeDataTable_get_GroupName.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().MailMergeDataTable_get_GroupName,self.Ptr))
        return ret


    @property

    def SourceData(self)->'IEnumerator':
        """
        Gets the source data of the mail merge data table.

        Returns:
            IEnumerator: The source data.
        """
        GetDllLibDoc().MailMergeDataTable_get_SourceData.argtypes=[c_void_p]
        GetDllLibDoc().MailMergeDataTable_get_SourceData.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().MailMergeDataTable_get_SourceData,self.Ptr)
        ret = None if intPtr==None else IEnumerator(intPtr)
        return ret


