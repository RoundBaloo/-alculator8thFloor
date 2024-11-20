from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class TextWatermark (  WatermarkBase) :
    """
    Represents a text watermark.
    """
    @dispatch
    def __init__(self):
        """
        Initializes a new instance of the TextWatermark class.
        """
        GetDllLibDoc().TextWatermark_CreateTextWatermark.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TextWatermark_CreateTextWatermark,);
        super(TextWatermark, self).__init__(intPtr)

    @dispatch
    def __init__(self, text:str):
        """
        Initializes a new instance of the TextWatermark class with the specified text.
        
        Args:
            text (str): The watermark text.
        """
        textPtr = StrToPtr(text)
        GetDllLibDoc().TextWatermark_CreateTextWatermarkT.argtypes=[c_char_p]
        GetDllLibDoc().TextWatermark_CreateTextWatermarkT.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TextWatermark_CreateTextWatermarkT,textPtr)
        super(TextWatermark, self).__init__(intPtr)
    
    @dispatch
    def __init__(self, text:str, fontName:str, fontSize:int, layout:WatermarkLayout):
        """
        Initializes a new instance of the TextWatermark class with the specified text, font name, font size, and layout.
        
        Args:
            text (str): The watermark text.
            fontName (str): The font name.
            fontSize (int): The font size.
            layout (WatermarkLayout): The watermark layout.
        """
        textPtr = StrToPtr(text)
        fontNamePtr = StrToPtr(fontName)
        iTypelayout:c_int = layout.value

        GetDllLibDoc().TextWatermark_CreateTextWatermarkTFFL.argtypes=[c_char_p,c_char_p,c_int,c_int]
        GetDllLibDoc().TextWatermark_CreateTextWatermarkTFFL.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TextWatermark_CreateTextWatermarkTFFL,textPtr, fontNamePtr, fontSize, iTypelayout)
        super(TextWatermark, self).__init__(intPtr)

    @property

    def Text(self)->str:
        """
        Gets or sets the watermark text.
        
        Returns:
            str: The watermark text.
        """
        GetDllLibDoc().TextWatermark_get_Text.argtypes=[c_void_p]
        GetDllLibDoc().TextWatermark_get_Text.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().TextWatermark_get_Text,self.Ptr))
        return ret


    @Text.setter
    def Text(self, value:str):
        """
        Sets the watermark text.
        
        Args:
            value (str): The watermark text.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().TextWatermark_set_Text.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().TextWatermark_set_Text,self.Ptr, valuePtr)

    @property

    def FontName(self)->str:
        """
        Gets or sets the watermark text's font name.
        
        Returns:
            str: The font name.
        """
        GetDllLibDoc().TextWatermark_get_FontName.argtypes=[c_void_p]
        GetDllLibDoc().TextWatermark_get_FontName.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().TextWatermark_get_FontName,self.Ptr))
        return ret


    @FontName.setter
    def FontName(self, value:str):
        """
        Sets the watermark text's font name.
        
        Args:
            value (str): The font name.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().TextWatermark_set_FontName.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().TextWatermark_set_FontName,self.Ptr, valuePtr)

    @property
    def FontSize(self)->float:
        """
        Gets or sets the text watermark size.
        
        Returns:
            float: The font size.
        """
        GetDllLibDoc().TextWatermark_get_FontSize.argtypes=[c_void_p]
        GetDllLibDoc().TextWatermark_get_FontSize.restype=c_float
        ret = CallCFunction(GetDllLibDoc().TextWatermark_get_FontSize,self.Ptr)
        return ret

    @FontSize.setter
    def FontSize(self, value:float):
        """
        Sets the text watermark size.
        
        Args:
            value (float): The font size.
        """
        GetDllLibDoc().TextWatermark_set_FontSize.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().TextWatermark_set_FontSize,self.Ptr, value)

    @property

    def Color(self)->'Color':
        """
        Gets or sets the text watermark color.
        
        Returns:
            Color: The watermark color.
        """
        GetDllLibDoc().TextWatermark_get_Color.argtypes=[c_void_p]
        GetDllLibDoc().TextWatermark_get_Color.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TextWatermark_get_Color,self.Ptr)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @Color.setter
    def Color(self, value:'Color'):
        """
        Sets the text watermark color.
        
        Args:
            value (Color): The watermark color.
        """
        GetDllLibDoc().TextWatermark_set_Color.argtypes=[c_void_p, c_void_p]
        CallCFunction(GetDllLibDoc().TextWatermark_set_Color,self.Ptr, value.Ptr)

    @property
    def Semitransparent(self)->bool:
        """
        Gets or sets the semitransparent property for the text watermark.
        
        Returns:
            bool: True if the text watermark is semitransparent, False otherwise.
        """
        GetDllLibDoc().TextWatermark_get_Semitransparent.argtypes=[c_void_p]
        GetDllLibDoc().TextWatermark_get_Semitransparent.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().TextWatermark_get_Semitransparent,self.Ptr)
        return ret

    @Semitransparent.setter
    def Semitransparent(self, value:bool):
        """
        Sets the semitransparent property for the text watermark.
        
        Args:
            value (bool): True if the text watermark is semitransparent, False otherwise.
        """
        GetDllLibDoc().TextWatermark_set_Semitransparent.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().TextWatermark_set_Semitransparent,self.Ptr, value)

    @property

    def Layout(self)->'WatermarkLayout':
        """
        Gets or sets the layout for the text watermark.
        
        Returns:
            WatermarkLayout: The watermark layout.
        """
        GetDllLibDoc().TextWatermark_get_Layout.argtypes=[c_void_p]
        GetDllLibDoc().TextWatermark_get_Layout.restype=c_int
        ret = CallCFunction(GetDllLibDoc().TextWatermark_get_Layout,self.Ptr)
        objwraped = WatermarkLayout(ret)
        return objwraped

    @Layout.setter
    def Layout(self, value:'WatermarkLayout'):
        """
        Sets the layout for the text watermark.
        
        Args:
            value (WatermarkLayout): The watermark layout.
        """
        GetDllLibDoc().TextWatermark_set_Layout.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().TextWatermark_set_Layout,self.Ptr, value.value)

