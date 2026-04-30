from datetime import datetime, date, time
from typing import Any, List, Optional, Union, Set
from enum import Enum
from pydantic import BaseModel, field_validator


############################################
# Enumerations are defined here
############################################

class Genre(Enum):
    Poetry = "Poetry"
    Cookbooks = "Cookbooks"
    Adventure = "Adventure"
    Philosophy = "Philosophy"
    History = "History"
    Technology = "Technology"
    Thriller = "Thriller"
    Fantasy = "Fantasy"
    Romance = "Romance"
    Horror = "Horror"

############################################
# Classes are defined here
############################################
class PublisherCreate(BaseModel):
    telephone: str
    address: str
    name: str
    book: Optional[List[int]] = None  # 1:N Relationship


class AuthorCreate(BaseModel):
    name: str
    birth: date
    books: Optional[List[int]] = None  # N:M Relationship (optional)


class LibraryCreate(BaseModel):
    telephone: str
    address: str
    web_page: str
    name: str
    books: Optional[List[int]] = None  # N:M Relationship (optional)


class BookCreate(BaseModel):
    pages: int
    genre: Genre
    price: float
    release: date
    title: str
    stock: int
    library: List[int]  # N:M Relationship
    publisher: int  # N:1 Relationship (mandatory)
    authors: List[int]  # N:M Relationship

    @field_validator('pages')
    @classmethod
    def validate_pages_1(cls, v):
        """OCL Constraint: constraint_Book_0_1"""
        if not (v > 10):
            raise ValueError('pages must be > 10')
        return v

