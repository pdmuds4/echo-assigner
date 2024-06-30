from pydantic import BaseModel, ConfigDict, field_validator
from typing import List, Any
import music21 as m21

class InputMidiID(BaseModel):
    value: int
    model_config = ConfigDict(frozen=True)


class InputMidiPath(BaseModel):
    value: str
    model_config = ConfigDict(frozen=True)


class InputMidiStream(BaseModel):
    value: Any
    model_config = ConfigDict(frozen=True)

    @field_validator('value')
    def check_value(cls, value: m21.stream.Score):
        if type(m21.stream.Score()) != type(value):
            raise TypeError('Input must be a music21.stream.Score object')
        else:
            return value


class InputMidiTimeSignature(BaseModel):
    value: Any
    model_config = ConfigDict(frozen=True)

    @field_validator('value')
    def check_value(cls, value: m21.meter.TimeSignature):
        if type(m21.meter.TimeSignature()) != type(value):
            raise TypeError('Input must be a music21.meter.TimeSignature object')
        elif value.ratioString not in ['4/4']:
            raise ValueError('Time signature must be 4/4')
        else:
            return value


class InputMidiBpmSection(BaseModel):
    start_offset: float
    end_offset: float
    value: Any

    @field_validator('value')
    def check_value(cls, value: m21.tempo.MetronomeMark):
        if type(m21.tempo.MetronomeMark()) != type(value):
            raise TypeError('Input must be a music21.tempo.MetronomeMark object')
        else:
            return value

class InputMidiBpmMap(BaseModel):
    value: List[InputMidiBpmSection]
    model_config = ConfigDict(frozen=True)


class InputMidiKey(BaseModel):
    value: Any
    model_config = ConfigDict(frozen=True)

    @field_validator('value')
    def check_value(cls, value: m21.key.Key):
        if type(m21.key.Key()) != type(value):
            raise TypeError('Input must be a music21.key.Key object')
        else:
            return value