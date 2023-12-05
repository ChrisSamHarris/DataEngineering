import pydantic
import string
from typing import Optional
import json 

class User(pydantic.BaseModel):
    username: str
    password: str
    age: int
    score: float
    email: Optional[str] = None
    phone_number: Optional[str] = None
    
    
    @pydantic.root_validator(pre=True)
    @classmethod
    def validate_phone_or_email(cls, values):
        "@pydantic.root_validator(pre=True) -> Validate prior to initialisation"
        if "email" in values or "phone_number" in values:
            return values
        else:
            raise ValueError("Either an email or a phone number is required to register a user.")
    
    
    @pydantic.validator("username")
    @classmethod
    def username_valid(cls, value):
        """
        Checks for punctuation within the username. Error raised if any occur.
        Every time you create a new instance of your User class (or modify the username
        field of an existing instance), this validator will be called to validate the "username" field.
        """
        print("Username validator called!")
        if any(p in value for p in string.punctuation):
            raise ValueError("Username must not include punctuation.")
        else:
            return value
        
        
    @pydantic.validator("password")
    @classmethod
    def username_valid(cls, value):
        if len(value) < 8: 
            raise ValueError("Password must be atleast 8 characters long")
        if any(p in value for p in string.punctuation):
            if any(d in value for d in string.digits):
                if any(l in value for l in string.ascii_lowercase):
                    if any(u in value for u in string.ascii_uppercase):
                        return value
        raise ValueError("Passowrd needs atleast 1 punctuation symbol, digit, upper and lowercase character.")
    
    
    @pydantic.validator("age", "score")
    @classmethod
    def number_valid(cls, value):
        if value >= 0:
            return value
        else:
            raise ValueError("Numbers can not be negative.")
    
    
user1 = User(username="user1", password="aB!12345",
             age=20, score=1, email="myemail@mail.com")

print(user1)
# print(user1.age)

json_users = [User(**u) for u in json.load(open("DataLD/users.json"))]

print(json_users)