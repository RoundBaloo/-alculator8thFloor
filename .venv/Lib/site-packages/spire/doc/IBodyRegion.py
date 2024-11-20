from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IBodyRegion(IDocumentObject):
    """
    Represents a body region in a document.
    """
#    @dispatch
#
#    @abc.abstractmethod
#    def Replace(self ,pattern:'Regex',replace:str)->int:
#        """
#
#        """
#        pass
#

    @dispatch
    @abc.abstractmethod
    def Replace(self, given: str, replace: str, caseSensitive: bool, wholeWord: bool) -> int:
        """
        Replaces occurrences of a given string with a replacement string in the body region.

        Args:
            given (str): The string to be replaced.
            replace (str): The replacement string.
            caseSensitive (bool): Specifies whether the replacement should be case-sensitive.
            wholeWord (bool): Specifies whether the replacement should be done only for whole words.

        Returns:
            int: The number of replacements made.
        """
        pass


#    @dispatch
#
#    @abc.abstractmethod
#    def Replace(self ,pattern:'Regex',textSelection:TextSelection)->int:
#        """
#
#        """
#        pass
#


