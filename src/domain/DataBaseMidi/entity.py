from pydantic import BaseModel
from .value_object import *


class DatabaseMidiEntity(BaseModel):
    id: DatabaseMidiID
    path: DatabaseMidiPath
    stream: DatabaseMidiStream = None

    def __init__(self, id: int, path: str):
        super().__init__(id=DatabaseMidiID(value=id), path=DatabaseMidiPath(value=path))
        self.stream = DatabaseMidiStream(value=m21.converter.parse(self.path.value))
        
        # [!]パートが3つ以上ある場合はパラメータとして選択できるようにする
        if len(self.stream.value.parts) > 2:
            raise ValueError("Database MIDI should have only one part")