from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class Body(DocumentContainer, IBody, ICompositeObject):
    """
    Represents the body of a document.
    """

    @property
    def DocumentObjectType(self) -> 'DocumentObjectType':
        """
        Gets the type of the document object.
        :return: The type of the document object.
        """
        GetDllLibDoc().Body_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().Body_get_DocumentObjectType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Body_get_DocumentObjectType,self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property
    def Paragraphs(self) -> 'ParagraphCollection':
        """
        Gets the inner paragraphs.
        :return: The inner paragraphs.
        """
        GetDllLibDoc().Body_get_Paragraphs.argtypes=[c_void_p]
        GetDllLibDoc().Body_get_Paragraphs.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Body_get_Paragraphs,self.Ptr)
        ret = None if intPtr==None else ParagraphCollection(intPtr)
        return ret

    @property
    def Tables(self) -> 'TableCollection':
        """
        Gets the inner tables.
        :return: The inner tables.
        """
        GetDllLibDoc().Body_get_Tables.argtypes=[c_void_p]
        GetDllLibDoc().Body_get_Tables.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Body_get_Tables,self.Ptr)
        from spire.doc import TableCollection
        ret = None if intPtr==None else TableCollection(intPtr)
        return ret


    @property
    def FormFields(self) -> 'FormFieldCollection':
        """
        Gets the form fields.
        :return: The form fields.
        """
        GetDllLibDoc().Body_get_FormFields.argtypes=[c_void_p]
        GetDllLibDoc().Body_get_FormFields.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Body_get_FormFields,self.Ptr)
        from spire.doc import FormFieldCollection
        ret = None if intPtr==None else FormFieldCollection(intPtr)
        return ret

    @property
    def LastParagraph(self) -> 'IParagraph':
        """
        Gets the last paragraph.
        :return: The last paragraph.
        """
        GetDllLibDoc().Body_get_LastParagraph.argtypes=[c_void_p]
        GetDllLibDoc().Body_get_LastParagraph.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Body_get_LastParagraph,self.Ptr)
        #ret = None if intPtr==None else IParagraph(intPtr)
        from spire.doc import Paragraph
        ret = None if intPtr==None else Paragraph(intPtr)
        return ret

    @property
    def FirstParagraph(self) -> 'IParagraph':
        """
        Gets the first paragraph.
        :return: The first paragraph.
        """
        GetDllLibDoc().Body_get_FirstParagraph.argtypes=[c_void_p]
        GetDllLibDoc().Body_get_FirstParagraph.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Body_get_FirstParagraph,self.Ptr)
        #ret = None if intPtr==None else IParagraph(intPtr)
        from spire.doc import Paragraph
        ret = None if intPtr==None else Paragraph(intPtr)
        return ret


    @property
    def ChildObjects(self) -> DocumentObjectCollection:
        """
        Gets the child objects.
        :return: The child objects.
        """
        GetDllLibDoc().Body_get_ChildObjects.argtypes=[c_void_p]
        GetDllLibDoc().Body_get_ChildObjects.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Body_get_ChildObjects,self.Ptr)
        ret = None if intPtr==None else DocumentObjectCollection(intPtr)
        return ret

    def AddParagraph(self) -> 'Paragraph':
        """
        Adds a paragraph at the end of the section.
        :return: The added paragraph.
        """
        GetDllLibDoc().Body_AddParagraph.argtypes=[c_void_p]
        GetDllLibDoc().Body_AddParagraph.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Body_AddParagraph,self.Ptr)
        from spire.doc import Paragraph
        ret = None if intPtr==None else Paragraph(intPtr)
        return ret


    @dispatch

    def AddTable(self)->'Table':
        """
        Adds a table.
        :return: The added table.
        """
        GetDllLibDoc().Body_AddTable.argtypes=[c_void_p]
        GetDllLibDoc().Body_AddTable.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Body_AddTable,self.Ptr)
        from spire.doc import Table
        ret = None if intPtr==None else Table(intPtr)
        return ret


    @dispatch

    def AddTable(self ,showBorder:bool)->'Table':
        """
        Adds a table.
        :param showBorder: Indicates whether to show the border.
        :return: The added table.
        """
        
        GetDllLibDoc().Body_AddTableS.argtypes=[c_void_p ,c_bool]
        GetDllLibDoc().Body_AddTableS.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Body_AddTableS,self.Ptr, showBorder)
        from spire.doc import Table
        ret = None if intPtr==None else Table(intPtr)
        return ret


    @dispatch
    def InsertXHTML(self, html: str):
        """
        Inserts HTML at the end of the text body.
        :param html: The HTML to insert.
        """
        htmlPtr = StrToPtr(html)
        GetDllLibDoc().Body_InsertXHTML.argtypes=[c_void_p ,c_char_p]
        CallCFunction(GetDllLibDoc().Body_InsertXHTML,self.Ptr, htmlPtr)

    @dispatch
    def InsertXHTML(self, html: str, paragraphIndex: int):
        """
        Inserts HTML. Inserting begins from the paragraph specified by paragraphIndex.
        :param html: The HTML to insert.
        :param paragraphIndex: The index of the paragraph to begin inserting from.
        """
        htmlPtr = StrToPtr(html)
        GetDllLibDoc().Body_InsertXHTMLHP.argtypes=[c_void_p ,c_char_p,c_int]
        CallCFunction(GetDllLibDoc().Body_InsertXHTMLHP,self.Ptr, htmlPtr,paragraphIndex)

    @dispatch
    def InsertXHTML(self, html: str, paragraphIndex: int, paragraphItemIndex: int):
        """
        Inserts HTML. Inserting begins from the paragraph specified by paragraphIndex and the paragraph item specified by paragraphItemIndex.
        :param html: The HTML to insert.
        :param paragraphIndex: The index of the paragraph to begin inserting from.
        :param paragraphItemIndex: The index of the paragraph item to begin inserting from.
        """
        htmlPtr = StrToPtr(html)
        GetDllLibDoc().Body_InsertXHTMLHPP.argtypes=[c_void_p ,c_char_p,c_int,c_int]
        CallCFunction(GetDllLibDoc().Body_InsertXHTMLHPP,self.Ptr, htmlPtr,paragraphIndex,paragraphItemIndex)

    @dispatch
    def IsValidXHTML(self, html: str, type: XHTMLValidationType) -> bool:
        """
        Validates the XHTML.
        :param html: The HTML to validate.
        :param type: The validation type.
        :return: True if the XHTML is valid, False otherwise.
        """
        htmlPtr = StrToPtr(html)
        enumtype:c_int = type.value

        GetDllLibDoc().Body_IsValidXHTML.argtypes=[c_void_p ,c_char_p,c_int]
        GetDllLibDoc().Body_IsValidXHTML.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().Body_IsValidXHTML,self.Ptr, htmlPtr,enumtype)
        return ret

#    @dispatch
#
#    def IsValidXHTML(self ,html:str,type:XHTMLValidationType,exceptionMessage:'String&')->bool:
#        """
#
#        """
#        enumtype:c_int = type.value
#        intPtrexceptionMessage:c_void_p = exceptionMessage.Ptr
#
#        GetDllLibDoc().Body_IsValidXHTMLHTE.argtypes=[c_void_p ,c_wchar_p,c_int,c_void_p]
#        GetDllLibDoc().Body_IsValidXHTMLHTE.restype=c_bool
#        ret = GetDllLibDoc().Body_IsValidXHTMLHTE(self.Ptr, html,enumtype,intPtrexceptionMessage)
#        return ret


    def EnsureMinimum(self):
        """
        If the text body has no paragraphs, creates and appends one paragraph.
        """
        GetDllLibDoc().Body_EnsureMinimum.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().Body_EnsureMinimum,self.Ptr)

