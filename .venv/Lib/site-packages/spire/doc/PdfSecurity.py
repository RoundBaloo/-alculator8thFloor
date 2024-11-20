from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class PdfSecurity (SpireObject) :
    """
        Represents the security settings of the PDF document.
    """
    @property

    def OwnerPassword(self)->str:
        """
        Gets the owner password.
        """
        GetDllLibDoc().PdfSecurity_get_OwnerPassword.argtypes=[c_void_p]
        GetDllLibDoc().PdfSecurity_get_OwnerPassword.restype=c_wchar_p
        ret = CallCFunction(GetDllLibDoc().PdfSecurity_get_OwnerPassword,self.Ptr)
        return ret


    @property

    def UserPassword(self)->str:
        """
        Gets the user password.
        """
        GetDllLibDoc().PdfSecurity_get_UserPassword.argtypes=[c_void_p]
        GetDllLibDoc().PdfSecurity_get_UserPassword.restype=c_wchar_p
        ret = CallCFunction(GetDllLibDoc().PdfSecurity_get_UserPassword,self.Ptr)
        return ret


    @dispatch

    def Encrypt(self ,openPassword:str):
        """
         To Encrypt the PDF document with open password.
         Note:If set empty string value to open password, it indicates that the PDF document can be operated without providing corresponding password. 
         Note: the document owner password should not be exist.

        Args:
            openPassword (str): The open password.
        """
        openPasswordPtr = StrToPtr(openPassword)
        GetDllLibDoc().PdfSecurity_Encrypt.argtypes=[c_void_p ,c_char_p]
        CallCFunction(GetDllLibDoc().PdfSecurity_Encrypt,self.Ptr, openPasswordPtr)

    @dispatch

    def Encrypt(self ,permissionPassword:str,permissions:PdfPermissionsFlags):
        """
         To Encrypt the PDF document with permission password and permissions.
         Note:The Permission password can't be empty string.

        Args:
            permissionPassword (str): The permission password.
            permissions (PdfPermissionsFlags): A set of flags specifying which operations are permitted when the document is opened with user access.
        """
        permissionPasswordPtr = StrToPtr(permissionPassword)
        enumpermissions:c_int = permissions.value

        GetDllLibDoc().PdfSecurity_EncryptPP.argtypes=[c_void_p ,c_char_p,c_int]
        CallCFunction(GetDllLibDoc().PdfSecurity_EncryptPP,self.Ptr, permissionPasswordPtr,enumpermissions)

    @dispatch

    def Encrypt(self ,openPassword:str,permissionPassword:str,permissions:PdfPermissionsFlags,keySize:PdfEncryptionKeySize):
        """
         To Encrypt the PDF document and set the encryption key size and permissions.
         Note:If set empty string value to open password or permission password, it indicates that the PDF document can be operated without providing corresponding password. 

        Args:
            openPassword (str): The open password.
            permissionPassword (str): The permission password.
            permissions (PdfPermissionsFlags): A set of flags specifying which operations are permitted when the document is opened with user access.
            keySize (PdfEncryptionKeySize): The bit length of the encryption key.
        """
        openPasswordPtr = StrToPtr(openPassword)
        permissionPasswordPtr = StrToPtr(permissionPassword)
        enumpermissions:c_int = permissions.value
        enumkeySize:c_int = keySize.value

        GetDllLibDoc().PdfSecurity_EncryptOPPK.argtypes=[c_void_p ,c_char_p,c_char_p,c_int,c_int]
        CallCFunction(GetDllLibDoc().PdfSecurity_EncryptOPPK,self.Ptr, openPasswordPtr,permissionPasswordPtr,enumpermissions,enumkeySize)

    @property

    def Permissions(self)->'PdfPermissionsFlags':
        """
        Gets the document's permission flags
        """
        GetDllLibDoc().PdfSecurity_get_Permissions.argtypes=[c_void_p]
        GetDllLibDoc().PdfSecurity_get_Permissions.restype=c_int
        ret = CallCFunction(GetDllLibDoc().PdfSecurity_get_Permissions,self.Ptr)
        objwraped = PdfPermissionsFlags(ret)
        return objwraped

    @property

    def KeySize(self)->'PdfEncryptionKeySize':
        """
        Gets the size of the key.
        """
        GetDllLibDoc().PdfSecurity_get_KeySize.argtypes=[c_void_p]
        GetDllLibDoc().PdfSecurity_get_KeySize.restype=c_int
        ret = CallCFunction(GetDllLibDoc().PdfSecurity_get_KeySize,self.Ptr)
        objwraped = PdfEncryptionKeySize(ret)
        return objwraped

