from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class SubSetEnumerator (  IEnumerator) :
    """
    Represents an internal enumerator for EntitySubSetCollection.
    """
    @property

    def Current(self)->'SpireObject':
        """
        Gets the current element in the collection.

        Returns:
            The current element in the collection.

        Raises:
            InvalidOperationException: The enumerator is positioned before the first element of the collection or after the last element.
        """
        GetDllLibDoc().SubSetEnumerator_get_Current.argtypes=[c_void_p]
        GetDllLibDoc().SubSetEnumerator_get_Current.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().SubSetEnumerator_get_Current,self.Ptr)
        ret = None if intPtr==None else SpireObject(intPtr)
        return ret


    def MoveNext(self)->bool:
        """
        Advances the enumerator to the next element of the collection.

        Returns:
            True if the enumerator was successfully advanced to the next element; False if the enumerator has passed the end of the collection.

        Raises:
            InvalidOperationException: The collection was modified after the enumerator was created.
        """
        GetDllLibDoc().SubSetEnumerator_MoveNext.argtypes=[c_void_p]
        GetDllLibDoc().SubSetEnumerator_MoveNext.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().SubSetEnumerator_MoveNext,self.Ptr)
        return ret

    def Reset(self):
        """
        Sets the enumerator to its initial position, which is before the first element in the collection.

        Raises:
            InvalidOperationException: The collection was modified after the enumerator was created.
        """
        GetDllLibDoc().SubSetEnumerator_Reset.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().SubSetEnumerator_Reset,self.Ptr)

