from pydantic import BaseModel
from typing import Text, List


class Data3(BaseModel):
    data01: List[float]
    data02: List[float]
    number: float