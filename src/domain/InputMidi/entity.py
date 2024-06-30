from pydantic import BaseModel
from .value_object import *


class InputMidiEntity(BaseModel):
    id: InputMidiID
    path: InputMidiPath
    stream: InputMidiStream = None
    time_signature: InputMidiTimeSignature = None
    bpm_map: InputMidiBpmMap = None

    def __init__(self, id: int, path: str):
        super().__init__(id=InputMidiID(value=id), path=InputMidiPath(value=path))
        self.stream = InputMidiStream(value=m21.converter.parse(self.path.value))
        
        # [!]拍の変更がある場合はエラーを出す
        self.time_signature = [
            InputMidiTimeSignature(value=ts) 
            for ts in self.stream.value.getTimeSignatures()
        ][0]

        # [!]空のMIDIにこのMapを適応できる関数を作る
        self.bpm_map = InputMidiBpmMap(value=[
            InputMidiBpmSection(
                start_offset=so,
                end_offset= eo,
                value=v
            ) for so, eo, v in self.stream.value.metronomeMarkBoundaries()
        ])


