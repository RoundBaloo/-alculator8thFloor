from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class TableOfContent (  ParagraphBase, IDocumentObject) :
    """
    Represents a table of contents in a document.
    """
    @dispatch
    def __init__(self, doc:IDocument):
        """
        Initializes a new instance of the TableOfContent class with the specified document.
        
        Args:
            doc (IDocument): The document to which the table of contents belongs.
        """
        intPdoc:c_void_p =  doc.Ptr

        GetDllLibDoc().TableOfContent_CreateTableOfContentD.argtypes=[c_void_p]
        GetDllLibDoc().TableOfContent_CreateTableOfContentD.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TableOfContent_CreateTableOfContentD,intPdoc)
        super(TableOfContent, self).__init__(intPtr)

    @dispatch
    def __init__(self, doc:IDocument,switches:str):
        """
        Initializes a new instance of the TableOfContent class with the specified document and switches.
        
        Args:
            doc (IDocument): The document to which the table of contents belongs.
            switches (str): The switches to be used for creating the table of contents.
        """
        switchesPtr = StrToPtr(switches)
        intPdoc:c_void_p =  doc.Ptr

        GetDllLibDoc().TableOfContent_CreateTableOfContentDS.argtypes=[c_void_p,c_char_p]
        GetDllLibDoc().TableOfContent_CreateTableOfContentDS.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TableOfContent_CreateTableOfContentDS,intPdoc,switchesPtr)
        super(TableOfContent, self).__init__(intPtr)

    @property
    def UseAbsolutePos(self)->bool:
        """
        Gets or sets a value indicating whether to use absolute position for the table of contents.
        """
        GetDllLibDoc().TableOfContent_get_UseAbsolutePos.argtypes=[c_void_p]
        GetDllLibDoc().TableOfContent_get_UseAbsolutePos.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().TableOfContent_get_UseAbsolutePos,self.Ptr)
        return ret

    @UseAbsolutePos.setter
    def UseAbsolutePos(self, value:bool):
        """
        Sets a value indicating whether to use absolute position for the table of contents.
        
        Args:
            value (bool): The value indicating whether to use absolute position.
        """
        GetDllLibDoc().TableOfContent_set_UseAbsolutePos.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().TableOfContent_set_UseAbsolutePos,self.Ptr, value)

    @property
    def UseHeadingStyles(self)->bool:
        """
        Gets or sets a value indicating whether to use default heading styles for the table of contents.
        """
        GetDllLibDoc().TableOfContent_get_UseHeadingStyles.argtypes=[c_void_p]
        GetDllLibDoc().TableOfContent_get_UseHeadingStyles.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().TableOfContent_get_UseHeadingStyles,self.Ptr)
        return ret

    @UseHeadingStyles.setter
    def UseHeadingStyles(self, value:bool):
        """
        Sets a value indicating whether to use default heading styles for the table of contents.
        
        Args:
            value (bool): The value indicating whether to use default heading styles.
        """
        GetDllLibDoc().TableOfContent_set_UseHeadingStyles.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().TableOfContent_set_UseHeadingStyles,self.Ptr, value)

    @property
    def UpperHeadingLevel(self)->int:
        """
        Gets or sets the ending heading level of the table of contents. Default value is 3.
        """
        GetDllLibDoc().TableOfContent_get_UpperHeadingLevel.argtypes=[c_void_p]
        GetDllLibDoc().TableOfContent_get_UpperHeadingLevel.restype=c_int
        ret = CallCFunction(GetDllLibDoc().TableOfContent_get_UpperHeadingLevel,self.Ptr)
        return ret

    @UpperHeadingLevel.setter
    def UpperHeadingLevel(self, value:int):
        """
        Sets the ending heading level of the table of contents.
        
        Args:
            value (int): The ending heading level.
        """
        GetDllLibDoc().TableOfContent_set_UpperHeadingLevel.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().TableOfContent_set_UpperHeadingLevel,self.Ptr, value)

    @property
    def LowerHeadingLevel(self)->int:
        """
        Gets or sets the starting heading level of the table of contents. Default value is 1.
        """
        GetDllLibDoc().TableOfContent_get_LowerHeadingLevel.argtypes=[c_void_p]
        GetDllLibDoc().TableOfContent_get_LowerHeadingLevel.restype=c_int
        ret = CallCFunction(GetDllLibDoc().TableOfContent_get_LowerHeadingLevel,self.Ptr)
        return ret

    @LowerHeadingLevel.setter
    def LowerHeadingLevel(self, value:int):
        """
        Sets the starting heading level of the table of contents.
        
        Args:
            value (int): The starting heading level.
        """
        GetDllLibDoc().TableOfContent_set_LowerHeadingLevel.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().TableOfContent_set_LowerHeadingLevel,self.Ptr, value)

    @property
    def UseTableEntryFields(self)->bool:
        """
        Gets or sets a value indicating whether to use table entry fields for the table of contents.
        """
        GetDllLibDoc().TableOfContent_get_UseTableEntryFields.argtypes=[c_void_p]
        GetDllLibDoc().TableOfContent_get_UseTableEntryFields.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().TableOfContent_get_UseTableEntryFields,self.Ptr)
        return ret

    @UseTableEntryFields.setter
    def UseTableEntryFields(self, value:bool):
        """
        Sets a value indicating whether to use table entry fields for the table of contents.
        
        Args:
            value (bool): The value indicating whether to use table entry fields.
        """
        GetDllLibDoc().TableOfContent_set_UseTableEntryFields.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().TableOfContent_set_UseTableEntryFields,self.Ptr, value)

    @property

    def TableID(self)->str:
        """
        Gets or sets the table ID for the table of contents.
        """
        GetDllLibDoc().TableOfContent_get_TableID.argtypes=[c_void_p]
        GetDllLibDoc().TableOfContent_get_TableID.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().TableOfContent_get_TableID,self.Ptr))
        return ret


    @TableID.setter
    def TableID(self, value:str):
        """
        Sets the table ID for the table of contents.
        
        Args:
            value (str): The table ID.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().TableOfContent_set_TableID.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().TableOfContent_set_TableID,self.Ptr, valuePtr)

    @property
    def RightAlignPageNumbers(self)->bool:
        """
        Gets or sets a value indicating whether to show page numbers from the right side in the table of contents.
        """
        GetDllLibDoc().TableOfContent_get_RightAlignPageNumbers.argtypes=[c_void_p]
        GetDllLibDoc().TableOfContent_get_RightAlignPageNumbers.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().TableOfContent_get_RightAlignPageNumbers,self.Ptr)
        return ret

    @RightAlignPageNumbers.setter
    def RightAlignPageNumbers(self, value:bool):
        """
        Sets a value indicating whether to show page numbers from the right side in the table of contents.
        
        Args:
            value (bool): The value indicating whether to right align page numbers.
        """
        GetDllLibDoc().TableOfContent_set_RightAlignPageNumbers.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().TableOfContent_set_RightAlignPageNumbers,self.Ptr, value)

    @property
    def IncludePageNumbers(self)->bool:
        """
        Gets or sets a value indicating whether to include page numbers in the table of contents.
        """
        GetDllLibDoc().TableOfContent_get_IncludePageNumbers.argtypes=[c_void_p]
        GetDllLibDoc().TableOfContent_get_IncludePageNumbers.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().TableOfContent_get_IncludePageNumbers,self.Ptr)
        return ret

    @IncludePageNumbers.setter
    def IncludePageNumbers(self, value:bool):
        """
        Sets a value indicating whether to include page numbers in the table of contents.
        
        Args:
            value (bool): The value indicating whether to include page numbers.
        """
        GetDllLibDoc().TableOfContent_set_IncludePageNumbers.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().TableOfContent_set_IncludePageNumbers,self.Ptr, value)

    @property
    def UseHyperlinks(self)->bool:
        """
        Gets or sets a value indicating whether to use hyperlinks.Default value is true.

        Return:
            bool: if it uses hyperlinks, set to true.

        """
        GetDllLibDoc().TableOfContent_get_UseHyperlinks.argtypes=[c_void_p]
        GetDllLibDoc().TableOfContent_get_UseHyperlinks.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().TableOfContent_get_UseHyperlinks,self.Ptr)
        return ret

    @UseHyperlinks.setter
    def UseHyperlinks(self, value:bool):
        GetDllLibDoc().TableOfContent_set_UseHyperlinks.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().TableOfContent_set_UseHyperlinks,self.Ptr, value)

    @property
    def UseOutlineLevels(self)->bool:
        """
        Gets or sets a value indicating whether use outline levels.Default value is false.

        Return:
            bool: if it uses outline levels, set to true.

        """
        GetDllLibDoc().TableOfContent_get_UseOutlineLevels.argtypes=[c_void_p]
        GetDllLibDoc().TableOfContent_get_UseOutlineLevels.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().TableOfContent_get_UseOutlineLevels,self.Ptr)
        return ret

    @UseOutlineLevels.setter
    def UseOutlineLevels(self, value:bool):
        GetDllLibDoc().TableOfContent_set_UseOutlineLevels.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().TableOfContent_set_UseOutlineLevels,self.Ptr, value)

    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
        Gets the type of the document object.

        Return:
            DocumentObjectType: The type of the document object.

        """
        GetDllLibDoc().TableOfContent_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().TableOfContent_get_DocumentObjectType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().TableOfContent_get_DocumentObjectType,self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped


    def SetTOCLevelStyle(self ,levelNumber:int,styleName:str):
        """
        Sets the style for TOC level.

        Args:
            levelNumber (int): The level number.
            styleName (str): Name of the style.

        """
        styleNamePtr = StrToPtr(styleName)
        GetDllLibDoc().TableOfContent_SetTOCLevelStyle.argtypes=[c_void_p ,c_int,c_char_p]
        CallCFunction(GetDllLibDoc().TableOfContent_SetTOCLevelStyle,self.Ptr, levelNumber,styleNamePtr)


    def GetTOCLevelStyle(self ,levelNumber:int)->str:
        """
        Gets the style name for TOC level.

        Args:
            levelNumber (int): The level number.

        Returns:
            str: The level style.
        """
        
        GetDllLibDoc().TableOfContent_GetTOCLevelStyle.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().TableOfContent_GetTOCLevelStyle.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().TableOfContent_GetTOCLevelStyle,self.Ptr, levelNumber))
        return ret


