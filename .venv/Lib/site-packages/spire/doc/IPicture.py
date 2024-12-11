from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class IPicture (  IParagraphBase, IDocumentObject) :
    """
    Represents an interface for a picture in a document.
    """
    @property
    @abc.abstractmethod
    def Height(self)->float:
        """
        Gets or sets the height of the picture.
        """
        pass


    @Height.setter
    @abc.abstractmethod
    def Height(self, value:float):
        """
        Sets the height of the picture.

        Args:
            value (float): The height value to set.
        """
        pass


    @property
    @abc.abstractmethod
    def Width(self)->float:
        """
        Gets or sets the width of the picture.
        """
        pass


    @Width.setter
    @abc.abstractmethod
    def Width(self, value:float):
        """
        Sets the width of the picture.

        Args:
            value (float): The width value to set.
        """
        pass


    @property
    @abc.abstractmethod
    def HeightScale(self)->float:
        """
        Gets or sets the height scale of the picture.
        """
        pass


    @HeightScale.setter
    @abc.abstractmethod
    def HeightScale(self, value:float):
        """
        Sets the height scale of the picture.

        Args:
            value (float): The height scale value to set.
        """
        pass


    @property
    @abc.abstractmethod
    def WidthScale(self)->float:
        """
        Gets or sets the width scale of the picture.
        """
        pass


    @WidthScale.setter
    @abc.abstractmethod
    def WidthScale(self, value:float):
        """
        Sets the width scale of the picture.

        Args:
            value (float): The width scale value to set.
        """
        pass


#
#    @abc.abstractmethod
#    def LoadImage(self ,imageBytes:'Byte[]'):
#        """
#
#        """
#        pass
#


#    @property
#
#    @abc.abstractmethod
#    def ImageBytes(self)->List['Byte']:
#        """
#
#        """
#        pass
#



    @abc.abstractmethod
    def AddCaption(self ,name:str,format:'CaptionNumberingFormat',captionPosition:'CaptionPosition')->'IParagraph':
        """
        Adds a caption to the picture.

        Args:
            name (str): The name of the caption.
            format (CaptionNumberingFormat): The numbering format of the caption.
            captionPosition (CaptionPosition): The position of the caption.

        Returns:
            IParagraph: The paragraph containing the caption.
        """
        pass


    @property

    @abc.abstractmethod
    def HorizontalOrigin(self)->'HorizontalOrigin':
        """
        Gets or sets the horizontal origin of the picture.
        """
        pass


    @HorizontalOrigin.setter
    @abc.abstractmethod
    def HorizontalOrigin(self, value:'HorizontalOrigin'):
        """
        Sets the horizontal origin of the picture.

        Args:
            value (HorizontalOrigin): The horizontal origin value to set.
        """
        pass


    @property

    @abc.abstractmethod
    def VerticalOrigin(self)->'VerticalOrigin':
        """
        Gets or sets the vertical origin of the picture.
        """
        pass


    @VerticalOrigin.setter
    @abc.abstractmethod
    def VerticalOrigin(self, value:'VerticalOrigin'):
        """
        Sets the vertical origin of the picture.

        Args:
            value (VerticalOrigin): The vertical origin value to set.
        """
        pass


    @property
    @abc.abstractmethod
    def HorizontalPosition(self)->float:
        """
        Gets or sets the horizontal position of the picture.
        """
        pass


    @HorizontalPosition.setter
    @abc.abstractmethod
    def HorizontalPosition(self, value:float):
        """
        Sets the horizontal position of the picture.

        Args:
            value (float): The horizontal position value to set.
        """
        pass


    @property
    @abc.abstractmethod
    def VerticalPosition(self)->float:
        """
        Gets or sets the vertical position of the picture.
        """
        pass


    @VerticalPosition.setter
    @abc.abstractmethod
    def VerticalPosition(self, value:float):
        """
        Sets the vertical position of the picture.

        Args:
            value (float): The vertical position value to set.
        """
        pass


    @property

    @abc.abstractmethod
    def TextWrappingStyle(self)->'TextWrappingStyle':
        """
        Gets or sets the text wrapping style of the picture.
        """
        pass


    @TextWrappingStyle.setter
    @abc.abstractmethod
    def TextWrappingStyle(self, value:'TextWrappingStyle'):
        """
        Sets the text wrapping style of the picture.

        Args:
            value (TextWrappingStyle): The text wrapping style value to set.
        """
        pass


    @property

    @abc.abstractmethod
    def TextWrappingType(self)->'TextWrappingType':
        """
        Gets or sets the text wrapping type of the picture.
        """
        pass


    @TextWrappingType.setter
    @abc.abstractmethod
    def TextWrappingType(self, value:'TextWrappingType'):
        """
        Sets the text wrapping type of the picture.

        Args:
            value (TextWrappingType): The text wrapping type value to set.
        """
        pass


    @property

    @abc.abstractmethod
    def HorizontalAlignment(self)->'ShapeHorizontalAlignment':
        """
        Gets or sets the horizontal alignment of the picture.
        """
        pass


    @HorizontalAlignment.setter
    @abc.abstractmethod
    def HorizontalAlignment(self, value:'ShapeHorizontalAlignment'):
        """
        Sets the horizontal alignment of the picture.

        Args:
            value (ShapeHorizontalAlignment): The horizontal alignment value to set.
        """
        pass


    @property

    @abc.abstractmethod
    def VerticalAlignment(self)->'ShapeVerticalAlignment':
        """
        Gets or sets the vertical alignment of the picture.
        """
        pass


    @VerticalAlignment.setter
    @abc.abstractmethod
    def VerticalAlignment(self, value:'ShapeVerticalAlignment'):
        """
        Sets the vertical alignment of the picture.

        Args:
            value (ShapeVerticalAlignment): The vertical alignment value to set.
        """
        pass


    @property

    @abc.abstractmethod
    def AlternativeText(self)->str:
        """
        Gets or sets the alternative text of the picture.
        """
        pass


    @AlternativeText.setter
    @abc.abstractmethod
    def AlternativeText(self, value:str):
        """
        Sets the alternative text of the picture.

        Args:
            value (str): The alternative text value to set.
        """
        pass


    @property

    @abc.abstractmethod
    def Title(self)->str:
        """
        Gets or sets the title of the picture.
        """
        pass


    @Title.setter
    @abc.abstractmethod
    def Title(self, value:str):
        """
        Sets the title of the picture.

        Args:
            value (str): The title value to set.
        """
        pass


    @property
    @abc.abstractmethod
    def IsUnderText(self)->bool:
        """
        Gets or sets a value indicating whether the picture is under the text.
        """
        pass


    @IsUnderText.setter
    @abc.abstractmethod
    def IsUnderText(self, value:bool):
        """
        Sets a value indicating whether the picture is under the text.

        Args:
            value (bool): The value indicating whether the picture is under the text.
        """
        pass
