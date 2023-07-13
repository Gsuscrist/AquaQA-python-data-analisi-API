from pydantic import BaseModel
from typing import Text, List


class Data(BaseModel):
    data: List[float]
