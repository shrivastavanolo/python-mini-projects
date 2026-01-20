from pydantic import BaseModel, field_validator, validate_email, SecretStr
from typing import List
import json

class EmailValidationError(Exception):
    """
    Validation error for invalid emails
    """
    def __init__(self, value, message):
        self.value = value
        super().__init__(message)

class PasswordValidationError(Exception):
    """
    Validation error for invalid passwords
    """
    def __init__(self, value, message):
        self.value = value
        super().__init__(message)

class User(BaseModel):
    name: str | None = None
    email: str
    password : SecretStr

    @field_validator("email", mode="after")
    @classmethod
    def validate_email_after(cls, value):
        try:
            validate_email(value)
        except Exception:
            raise EmailValidationError( value, "Invalid email address" )
        
    @field_validator("password", mode="after")
    @classmethod
    def validate_pass_after(cls, value):
        secret = value.get_secret_value()
        if len(secret)<8:
            raise PasswordValidationError( value, "Password should be longer than 8 chars" )
        return value
    
def main():
    with open("./users.json") as file:
        data = json.load(file)
        users : User[List] = [User(**item) for item in data]
        print(users[0].model_dump())

if __name__ == "__main__":
    main()