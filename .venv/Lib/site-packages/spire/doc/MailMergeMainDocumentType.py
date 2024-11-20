from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class MailMergeMainDocumentType(Enum):
    """
    Enum class representing the types of mail merge main documents.
    """
    NotAMergeDocument = 0
    FormLetters = 1
    MailingLabels = 2
    Envelopes = 4
    Catalog = 8
    Email = 16
    Fax = 32
    Default = 0
