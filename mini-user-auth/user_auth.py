import functools
from typing import Any, Dict, Callable
import logging
from time import perf_counter

#Set logging level to INFO
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)
logger = logging.getLogger("timelog")

class AuthError(Exception):
    """
    Validation error for unauthorized users
    """
    
    def __init__(self, value: Any, message: str) -> None:
        self.value = value
        super().__init__(message)
    
def require_auth(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        auth = False
        name = "Unknown"
        if args[0] and type(args[0])==dict:
            auth = args[0].get("is_auth", 0)
            name = args[0].get("name", "Unknown")
        if not auth:
            raise AuthError(auth, f'Unauthenticated user : {name}')

        value = func(*args, **kwargs)
        return value
    return wrapper

def log_execution_time(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        logger.info(f'Function {func.__name__} has started.')
        start_time = perf_counter()
        value = func(*args, **kwargs)
        end_time = perf_counter()
        logger.info(f'Function {func.__name__} has executed and took a time of {end_time - start_time:.4f}s.')

        return value
    return wrapper

@require_auth
@log_execution_time
def print_user_data(user: Dict) -> None:
    for k,v in user.items():
        print(f'{k} of this user is {v}')

def main():
    users = [{"name": "Shreya", "age": 90, "is_auth": True}, {"name": "hacker", "age": 20, "is_auth": False}, {"name": "unknown", "age": 20}]
    for user in users:
        print_user_data(user)

if __name__ == "__main__":
    main()