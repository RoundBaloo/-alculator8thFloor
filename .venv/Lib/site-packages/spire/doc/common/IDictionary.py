from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
if __package__ == "spire.pdf.common":
    from spire.pdf.common import *
elif __package__ == "spire.xls.common":
    from spire.xls.common import *
elif __package__ == "spire.doc.common":
    from spire.doc.common import *
else :
    from spire.presentation.common import *
#from spire.xls import *
from ctypes import *
import abc

K = TypeVar("K", bound=SpireObject)
V = TypeVar("V", bound=SpireObject)
class IDictionary (  ICollection[K]) :
    """

    """

    @abc.abstractmethod
    def get_Item(self ,key:'SpireObject')->'SpireObject':
        """

        """
        pass



    @abc.abstractmethod
    def set_Item(self ,key:'SpireObject',value:'SpireObject'):
        """

        """
        pass


    @property

    @abc.abstractmethod
    def Keys(self)->'ICollection':
        """

        """
        pass


    @property

    @abc.abstractmethod
    def Values(self)->'ICollection':
        """

        """
        pass



    @abc.abstractmethod
    def Contains(self ,key:'SpireObject')->int:
        """

        """
        pass



    @abc.abstractmethod
    def Add(self ,key:'SpireObject',value:'SpireObject'):
        """

        """
        pass


    @abc.abstractmethod
    def Clear(self):
        """

        """
        pass


    @property
    @abc.abstractmethod
    def IsReadOnly(self)->int:
        """

        """
        pass


    @property
    @abc.abstractmethod
    def IsFixedSize(self)->int:
        """

        """
        pass


#
#    @abc.abstractmethod
#    def GetEnumerator(self)->'IDictionaryEnumerator':
#        """
#
#        """
#        pass
#



    @abc.abstractmethod
    def Remove(self ,key:'SpireObject'):
        """

        """
        pass


