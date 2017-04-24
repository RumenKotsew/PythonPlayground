import re
import hashlib

from datetime import datetime

from exceptions import PasswordNotStrongEnoughException


def strong_password(*decorator_args, **decorator_kwargs):
    def wrapper(func):
        def inner(*function_args, **function_kwargs):
            pass_regex = "^(?=.*[A-Z])(?=.*[0-9])(?=.*[a-z]).{6,12}$"
            pattern = re.compile(pass_regex)
            if pattern.match(function_kwargs['password']):
                return func(*function_args, **function_kwargs)
            else:
                raise PasswordNotStrongEnoughException()
        return inner
    return wrapper


def hash_password(*decorator_args, **decorator_kwargs):
    def wrapper(func):
        def inner(*function_args, **function_kwargs):
            password = function_kwargs['password'].encode('utf-8')
            password = hashlib.md5(password)
            password = password.hexdigest()
            function_kwargs['password'] = password
            return func(*function_args, **function_kwargs)
        return inner
    return wrapper


def bruteforce_check(*decorator_args, **decorator_kwargs):
    def wrapper(func):
        def inner(*function_args, **function_kwargs):
            time = datetime.now()
            
        return inner
    return wrapper





str(datetime.now())