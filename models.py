import re
from fastapi import Query

from pydantic import BaseModel, validator


RE_INT_AND_MATH = re.compile(r'([-+]?[0-9]*\.?[0-9]+[\/\+\-\*])+([-+]?[0-9]*\.?[0-9]+)')

class CalcGetRequest(BaseModel):
    expression: str = Query(None, max_length=50)
    @validator('expression')
    def onlySimpleMathAndNumbers(cls, v):
        if RE_INT_AND_MATH.match(v):
            return v
        else:
            raise ValueError('only simple math and numbers requiert')


class CalcResponce(BaseModel):
    uid: str = None
    result: str = None
    operation: str = None