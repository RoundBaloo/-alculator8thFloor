from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class BackgroundGradient(VMLFill):
    """
    Represents a background gradient.
    """

    @property
    def Color1(self) -> 'Color':
        """
        Gets the first color for the gradient.
        """
        GetDllLibDoc().BackgroundGradient_get_Color1.argtypes=[c_void_p]
        GetDllLibDoc().BackgroundGradient_get_Color1.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().BackgroundGradient_get_Color1,self.Ptr)
        ret = None if intPtr==None else Color(intPtr)
        return ret

    @Color1.setter
    def Color1(self, value:'Color'):
        """
        Sets the first color for the gradient.
        """
        GetDllLibDoc().BackgroundGradient_set_Color1.argtypes=[c_void_p, c_void_p]
        CallCFunction(GetDllLibDoc().BackgroundGradient_set_Color1,self.Ptr, value.Ptr)

    @property
    def Color2(self) -> 'Color':
        """
        Gets the second color for the gradient (used when TwoColors set to true).
        """
        GetDllLibDoc().BackgroundGradient_get_Color2.argtypes=[c_void_p]
        GetDllLibDoc().BackgroundGradient_get_Color2.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().BackgroundGradient_get_Color2,self.Ptr)
        ret = None if intPtr==None else Color(intPtr)
        return ret

    @Color2.setter
    def Color2(self, value:'Color'):
        """
        Sets the second color for the gradient (used when TwoColors set to true).
        """
        GetDllLibDoc().BackgroundGradient_set_Color2.argtypes=[c_void_p, c_void_p]
        CallCFunction(GetDllLibDoc().BackgroundGradient_set_Color2,self.Ptr, value.Ptr)

    @property
    def ShadingStyle(self) -> 'GradientShadingStyle':
        """
        Gets the shading style for the gradient.
        """
        GetDllLibDoc().BackgroundGradient_get_ShadingStyle.argtypes=[c_void_p]
        GetDllLibDoc().BackgroundGradient_get_ShadingStyle.restype=c_int
        ret = CallCFunction(GetDllLibDoc().BackgroundGradient_get_ShadingStyle,self.Ptr)
        objwraped = GradientShadingStyle(ret)
        return objwraped

    @ShadingStyle.setter
    def ShadingStyle(self, value:'GradientShadingStyle'):
        """
        Sets the shading style for the gradient.
        """
        GetDllLibDoc().BackgroundGradient_set_ShadingStyle.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().BackgroundGradient_set_ShadingStyle,self.Ptr, value.value)

    @property
    def ShadingVariant(self) -> 'GradientShadingVariant':
        """
        Gets the shading variants.
        """
        GetDllLibDoc().BackgroundGradient_get_ShadingVariant.argtypes=[c_void_p]
        GetDllLibDoc().BackgroundGradient_get_ShadingVariant.restype=c_int
        ret = CallCFunction(GetDllLibDoc().BackgroundGradient_get_ShadingVariant,self.Ptr)
        objwraped = GradientShadingVariant(ret)
        return objwraped

    @ShadingVariant.setter
    def ShadingVariant(self, value:'GradientShadingVariant'):
        """
        Sets the shading variants.
        """
        GetDllLibDoc().BackgroundGradient_set_ShadingVariant.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().BackgroundGradient_set_ShadingVariant,self.Ptr, value.value)

