from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class TextBoxFormat (  WordAttrCollection) :
    """
    Represents the format of a text box.
    """
    @property

    def HorizontalOrigin(self)->'HorizontalOrigin':
        """
        Get/set the horizontal origin of the text box.
        """
        GetDllLibDoc().TextBoxFormat_get_HorizontalOrigin.argtypes=[c_void_p]
        GetDllLibDoc().TextBoxFormat_get_HorizontalOrigin.restype=c_int
        ret = CallCFunction(GetDllLibDoc().TextBoxFormat_get_HorizontalOrigin,self.Ptr)
        objwraped = HorizontalOrigin(ret)
        return objwraped

    @HorizontalOrigin.setter
    def HorizontalOrigin(self, value:'HorizontalOrigin'):
        GetDllLibDoc().TextBoxFormat_set_HorizontalOrigin.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().TextBoxFormat_set_HorizontalOrigin,self.Ptr, value.value)

    @property

    def VerticalOrigin(self)->'VerticalOrigin':
        """
        Get/set the vertical origin of the text box.
        """
        GetDllLibDoc().TextBoxFormat_get_VerticalOrigin.argtypes=[c_void_p]
        GetDllLibDoc().TextBoxFormat_get_VerticalOrigin.restype=c_int
        ret = CallCFunction(GetDllLibDoc().TextBoxFormat_get_VerticalOrigin,self.Ptr)
        objwraped = VerticalOrigin(ret)
        return objwraped

    @VerticalOrigin.setter
    def VerticalOrigin(self, value:'VerticalOrigin'):
        GetDllLibDoc().TextBoxFormat_set_VerticalOrigin.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().TextBoxFormat_set_VerticalOrigin,self.Ptr, value.value)

    @property

    def FillColor(self)->'Color':
        """
        Get/set the fill color of the text box.
        """
        GetDllLibDoc().TextBoxFormat_get_FillColor.argtypes=[c_void_p]
        GetDllLibDoc().TextBoxFormat_get_FillColor.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TextBoxFormat_get_FillColor,self.Ptr)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @FillColor.setter
    def FillColor(self, value:'Color'):
        GetDllLibDoc().TextBoxFormat_set_FillColor.argtypes=[c_void_p, c_void_p]
        CallCFunction(GetDllLibDoc().TextBoxFormat_set_FillColor,self.Ptr, value.Ptr)

    @property

    def FillEfects(self)->'Background':
        """
        Get the fill effects of the text box.
        """
        GetDllLibDoc().TextBoxFormat_get_FillEfects.argtypes=[c_void_p]
        GetDllLibDoc().TextBoxFormat_get_FillEfects.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TextBoxFormat_get_FillEfects,self.Ptr)
        ret = None if intPtr==None else Background(intPtr)
        return ret


    @property

    def LineStyle(self)->'TextBoxLineStyle':
        """
        Get/set the line style of the text box.
        """
        GetDllLibDoc().TextBoxFormat_get_LineStyle.argtypes=[c_void_p]
        GetDllLibDoc().TextBoxFormat_get_LineStyle.restype=c_int
        ret = CallCFunction(GetDllLibDoc().TextBoxFormat_get_LineStyle,self.Ptr)
        objwraped = TextBoxLineStyle(ret)
        return objwraped

    @LineStyle.setter
    def LineStyle(self, value:'TextBoxLineStyle'):
        GetDllLibDoc().TextBoxFormat_set_LineStyle.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().TextBoxFormat_set_LineStyle,self.Ptr, value.value)

    @property
    def Width(self)->float:
        """
        Get/set the width of the text box.
        """
        GetDllLibDoc().TextBoxFormat_get_Width.argtypes=[c_void_p]
        GetDllLibDoc().TextBoxFormat_get_Width.restype=c_float
        ret = CallCFunction(GetDllLibDoc().TextBoxFormat_get_Width,self.Ptr)
        return ret

    @Width.setter
    def Width(self, value:float):
        GetDllLibDoc().TextBoxFormat_set_Width.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().TextBoxFormat_set_Width,self.Ptr, value)

    @property
    def Height(self)->float:
        """
        Get/set the height of the text box.
        """
        GetDllLibDoc().TextBoxFormat_get_Height.argtypes=[c_void_p]
        GetDllLibDoc().TextBoxFormat_get_Height.restype=c_float
        ret = CallCFunction(GetDllLibDoc().TextBoxFormat_get_Height,self.Ptr)
        return ret

    @Height.setter
    def Height(self, value:float):
        GetDllLibDoc().TextBoxFormat_set_Height.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().TextBoxFormat_set_Height,self.Ptr, value)

    @property

    def LineColor(self)->'Color':
        """
        Get/set the line color of the text box.
        """
        GetDllLibDoc().TextBoxFormat_get_LineColor.argtypes=[c_void_p]
        GetDllLibDoc().TextBoxFormat_get_LineColor.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TextBoxFormat_get_LineColor,self.Ptr)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @LineColor.setter
    def LineColor(self, value:'Color'):
        GetDllLibDoc().TextBoxFormat_set_LineColor.argtypes=[c_void_p, c_void_p]
        CallCFunction(GetDllLibDoc().TextBoxFormat_set_LineColor,self.Ptr, value.Ptr)

    @property
    def NoLine(self)->bool:
        """
        Get/set value which defines if
        there is a line around textbox shape.
        """
        GetDllLibDoc().TextBoxFormat_get_NoLine.argtypes=[c_void_p]
        GetDllLibDoc().TextBoxFormat_get_NoLine.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().TextBoxFormat_get_NoLine,self.Ptr)
        return ret

    @NoLine.setter
    def NoLine(self, value:bool):
        GetDllLibDoc().TextBoxFormat_set_NoLine.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().TextBoxFormat_set_NoLine,self.Ptr, value)

    @property
    def HorizontalPosition(self)->float:
        """
        Get/set textbox horizontal position.
        """
        GetDllLibDoc().TextBoxFormat_get_HorizontalPosition.argtypes=[c_void_p]
        GetDllLibDoc().TextBoxFormat_get_HorizontalPosition.restype=c_float
        ret = CallCFunction(GetDllLibDoc().TextBoxFormat_get_HorizontalPosition,self.Ptr)
        return ret

    @HorizontalPosition.setter
    def HorizontalPosition(self, value:float):
        GetDllLibDoc().TextBoxFormat_set_HorizontalPosition.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().TextBoxFormat_set_HorizontalPosition,self.Ptr, value)

    @property
    def IsFitShapeToText(self)->bool:
        """
        Gets or Sets a value.Specifies whether the spape stretches to fit the text in the textbox.
        Default is false.
        """
        GetDllLibDoc().TextBoxFormat_get_IsFitShapeToText.argtypes=[c_void_p]
        GetDllLibDoc().TextBoxFormat_get_IsFitShapeToText.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().TextBoxFormat_get_IsFitShapeToText,self.Ptr)
        return ret

    @IsFitShapeToText.setter
    def IsFitShapeToText(self, value:bool):
        GetDllLibDoc().TextBoxFormat_set_IsFitShapeToText.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().TextBoxFormat_set_IsFitShapeToText,self.Ptr, value)

    @property
    def VerticalPosition(self)->float:
        """
        Get/set textbox vertical position.
        """
        GetDllLibDoc().TextBoxFormat_get_VerticalPosition.argtypes=[c_void_p]
        GetDllLibDoc().TextBoxFormat_get_VerticalPosition.restype=c_float
        ret = CallCFunction(GetDllLibDoc().TextBoxFormat_get_VerticalPosition,self.Ptr)
        return ret

    @VerticalPosition.setter
    def VerticalPosition(self, value:float):
        GetDllLibDoc().TextBoxFormat_set_VerticalPosition.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().TextBoxFormat_set_VerticalPosition,self.Ptr, value)

    @property

    def TextWrappingStyle(self)->'TextWrappingStyle':
        """
        Get/set text Wrapping style.
        """
        GetDllLibDoc().TextBoxFormat_get_TextWrappingStyle.argtypes=[c_void_p]
        GetDllLibDoc().TextBoxFormat_get_TextWrappingStyle.restype=c_int
        ret = CallCFunction(GetDllLibDoc().TextBoxFormat_get_TextWrappingStyle,self.Ptr)
        objwraped = TextWrappingStyle(ret)
        return objwraped

    @TextWrappingStyle.setter
    def TextWrappingStyle(self, value:'TextWrappingStyle'):
        GetDllLibDoc().TextBoxFormat_set_TextWrappingStyle.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().TextBoxFormat_set_TextWrappingStyle,self.Ptr, value.value)

    @property

    def TextWrappingType(self)->'TextWrappingType':
        """
        Get/set wrapping type for textbox.
        """
        GetDllLibDoc().TextBoxFormat_get_TextWrappingType.argtypes=[c_void_p]
        GetDllLibDoc().TextBoxFormat_get_TextWrappingType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().TextBoxFormat_get_TextWrappingType,self.Ptr)
        objwraped = TextWrappingType(ret)
        return objwraped

    @TextWrappingType.setter
    def TextWrappingType(self, value:'TextWrappingType'):
        GetDllLibDoc().TextBoxFormat_set_TextWrappingType.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().TextBoxFormat_set_TextWrappingType,self.Ptr, value.value)

    @property
    def LineWidth(self)->float:
        """
        Get/set textbox line width.
        """
        GetDllLibDoc().TextBoxFormat_get_LineWidth.argtypes=[c_void_p]
        GetDllLibDoc().TextBoxFormat_get_LineWidth.restype=c_float
        ret = CallCFunction(GetDllLibDoc().TextBoxFormat_get_LineWidth,self.Ptr)
        return ret

    @LineWidth.setter
    def LineWidth(self, value:float):
        GetDllLibDoc().TextBoxFormat_set_LineWidth.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().TextBoxFormat_set_LineWidth,self.Ptr, value)

    @property

    def LineDashing(self)->'LineDashing':
        """
        Get/set line dashing for textbox.
        """
        GetDllLibDoc().TextBoxFormat_get_LineDashing.argtypes=[c_void_p]
        GetDllLibDoc().TextBoxFormat_get_LineDashing.restype=c_int
        ret = CallCFunction(GetDllLibDoc().TextBoxFormat_get_LineDashing,self.Ptr)
        objwraped = LineDashing(ret)
        return objwraped

    @LineDashing.setter
    def LineDashing(self, value:'LineDashing'):
        GetDllLibDoc().TextBoxFormat_set_LineDashing.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().TextBoxFormat_set_LineDashing,self.Ptr, value.value)

    @property

    def HorizontalAlignment(self)->'ShapeHorizontalAlignment':
        """
        Get/set textbox horizontal alignment.
        """
        GetDllLibDoc().TextBoxFormat_get_HorizontalAlignment.argtypes=[c_void_p]
        GetDllLibDoc().TextBoxFormat_get_HorizontalAlignment.restype=c_int
        ret = CallCFunction(GetDllLibDoc().TextBoxFormat_get_HorizontalAlignment,self.Ptr)
        objwraped = ShapeHorizontalAlignment(ret)
        return objwraped

    @HorizontalAlignment.setter
    def HorizontalAlignment(self, value:'ShapeHorizontalAlignment'):
        GetDllLibDoc().TextBoxFormat_set_HorizontalAlignment.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().TextBoxFormat_set_HorizontalAlignment,self.Ptr, value.value)

    @property

    def VerticalAlignment(self)->'ShapeVerticalAlignment':
        """
        Get/set textbox vertical alignment.
        """
        GetDllLibDoc().TextBoxFormat_get_VerticalAlignment.argtypes=[c_void_p]
        GetDllLibDoc().TextBoxFormat_get_VerticalAlignment.restype=c_int
        ret = CallCFunction(GetDllLibDoc().TextBoxFormat_get_VerticalAlignment,self.Ptr)
        objwraped = ShapeVerticalAlignment(ret)
        return objwraped

    @VerticalAlignment.setter
    def VerticalAlignment(self, value:'ShapeVerticalAlignment'):
        GetDllLibDoc().TextBoxFormat_set_VerticalAlignment.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().TextBoxFormat_set_VerticalAlignment,self.Ptr, value.value)

    @property

    def LayoutFlowAlt(self)->'TextDirection':
        """
        Gets or sets the text direction of the textbox.
        """
        GetDllLibDoc().TextBoxFormat_get_LayoutFlowAlt.argtypes=[c_void_p]
        GetDllLibDoc().TextBoxFormat_get_LayoutFlowAlt.restype=c_int
        ret = CallCFunction(GetDllLibDoc().TextBoxFormat_get_LayoutFlowAlt,self.Ptr)
        objwraped = TextDirection(ret)
        return objwraped

    @LayoutFlowAlt.setter
    def LayoutFlowAlt(self, value:'TextDirection'):
        GetDllLibDoc().TextBoxFormat_set_LayoutFlowAlt.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().TextBoxFormat_set_LayoutFlowAlt,self.Ptr, value.value)

    @property

    def TextAnchor(self)->'ShapeVerticalAlignment':
        """
        Gets or sets the vertical anchoring of text. Default is top.
        """
        GetDllLibDoc().TextBoxFormat_get_TextAnchor.argtypes=[c_void_p]
        GetDllLibDoc().TextBoxFormat_get_TextAnchor.restype=c_int
        ret = CallCFunction(GetDllLibDoc().TextBoxFormat_get_TextAnchor,self.Ptr)
        objwraped = ShapeVerticalAlignment(ret)
        return objwraped

    @TextAnchor.setter
    def TextAnchor(self, value:'ShapeVerticalAlignment'):
        GetDllLibDoc().TextBoxFormat_set_TextAnchor.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().TextBoxFormat_set_TextAnchor,self.Ptr, value.value)

    @property

    def InternalMargin(self)->'InternalMargin':
        """
        Gets the internal margin.

        Returns:
            InternalMargin: The internal margin.
        """
        GetDllLibDoc().TextBoxFormat_get_InternalMargin.argtypes=[c_void_p]
        GetDllLibDoc().TextBoxFormat_get_InternalMargin.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TextBoxFormat_get_InternalMargin,self.Ptr)
        ret = None if intPtr==None else InternalMargin(intPtr)
        return ret



    def Clone(self)->'TextBoxFormat':
        """
        Clone textbox format.

        Returns:
            TextBoxFormat: The result TextBoxFormat.
        """
        GetDllLibDoc().TextBoxFormat_Clone.argtypes=[c_void_p]
        GetDllLibDoc().TextBoxFormat_Clone.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TextBoxFormat_Clone,self.Ptr)
        ret = None if intPtr==None else TextBoxFormat(intPtr)
        return ret


