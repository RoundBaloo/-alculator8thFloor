from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class HttpContentType(Enum):
    """
    Enum class representing the type of HTTP content to be sent to the browser.

    """
    InBrowser = 0
    Attachment = 1
