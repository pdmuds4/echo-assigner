from pydantic import BaseModel, ConfigDict, field_validator
from typing import Any
import music21 as m21

class DatabaseMidiID(BaseModel):
    value: int
    model_config = ConfigDict(frozen=True)


class DatabaseMidiPath(BaseModel):
    value: str
    model_config = ConfigDict(frozen=True)


class DatabaseMidiStream(BaseModel):
    value: Any
    model_config = ConfigDict(frozen=True)

    @field_validator('value')
    def check_value(cls, value: m21.stream.Score):
        if type(m21.stream.Score()) != type(value):
            raise TypeError('Input must be a music21.stream.Score object')
        else:
            return value