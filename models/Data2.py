from pydantic import BaseModel
from typing import Text, List


class Data2(BaseModel):
    data01: List[float]
    data02: List[float]