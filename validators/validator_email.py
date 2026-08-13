from pydantic import BaseModel
from validators import constants
from typing import Literal
class CheckEmail:
    class Request(BaseModel):
        email:str
    class Response(BaseModel):
        status:Literal[constants.Status.success, constants.Status.failed]
        is_valid:bool|None=None
        message:str=""

    @staticmethod
    def _isValidLetterInLocal(l:str)->bool:
        if ord("a") <= ord(l) <= ord("z"): return True
        if ord("A") <= ord(l) <= ord("Z"): return True
        if l.isnumeric(): return True
        if l in "._%+-": return True
        return False
    @staticmethod
    def _isValidLetterInDomain(l:str)->bool:
        if ord("a") <= ord(l) <= ord("z"): return True
        if ord("A") <= ord(l) <= ord("Z"): return True
        if l.isnumeric(): return True
        if l in ".-": return True
        return False
    
    @staticmethod
    def _isValidLocal(local:str)->bool:
        if any(not CheckEmail._isValidLetterInLocal(l) for l in local):
            return False
        if ".." in local: return False
        if "." in [local[0], local[-1]]: return False
        return True

    @staticmethod
    def _isValidDomain(domain:str)->bool:
        if any(not CheckEmail._isValidLetterInDomain(l) for l in domain):
            return False
        if ".." in domain: return False
        if "." in [domain[0], domain[-1]]: return False
        if '-' in [domain[0], domain[-1]]: return False
        if "." not in domain: return False
        first_dot_index = domain.index(".")
        after_dot = domain[first_dot_index + 1:]
        if sum([l.isalpha() for l in after_dot]) < 2:
            return False
        return True
         
    

    @staticmethod
    async def check_email(req:Request)->Response:
        try:
            if req.email.count("@") != 1:
                return CheckEmail.Response(
                    status=constants.Status.success,
                    is_valid = False,
                    message = "Count of '@' is invalid"
                )
            dog_index = req.email.index("@")
            local = req.email[:dog_index]
            domain = req.email[dog_index+1:]
            if not CheckEmail._isValidLocal(local):
                return CheckEmail.Response(
                                status=constants.Status.success,
                                is_valid = False,
                                message="Local part of email is invalid"
                            )
            if not CheckEmail._isValidDomain(domain):
                return CheckEmail.Response(
                                status=constants.Status.success,
                                is_valid = False,
                                message="Domain part of email is invalid"
                            )
            return CheckEmail.Response(
                status=constants.Status.success,
                is_valid = True,
                messsage = "Email is valid!"
            )
        except Exception as e:
            print(e)
            return CheckEmail.Response(
                status = constants.Status.failed,
                is_valid = None,
                message = str(e)
            )


        
