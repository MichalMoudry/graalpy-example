"""
A module with request classes.
"""
from typing import Annotated
from pydantic import BaseModel, Field
from pydantic.dataclasses import dataclass


@dataclass(frozen=True)
class AddEventRequest(BaseModel):
    data: Annotated[str, Field(min_length=1, max_length=255)]
