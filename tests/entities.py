from enum import Enum, IntEnum, Flag, IntFlag
from dataclasses import dataclass

from mashumaro import DataClassDictMixin
from mashumaro.types import SerializableType


class MyEnum(Enum):
    a = 'letter a'
    b = 'letter b'


class MyIntEnum(IntEnum):
    a = 1
    b = 2


class MyFlag(Flag):
    a = 1
    b = 2


class MyIntFlag(IntFlag):
    a = 1
    b = 2


@dataclass
class MyDataClass(DataClassDictMixin):
    a: int
    b: int


class MutableString(SerializableType):
    def __init__(self, value: str):
        self.characters = [c for c in value]

    def _serialize(self) -> str:
        return str(self)

    @classmethod
    def _deserialize(cls, value: str) -> 'MutableString':
        return MutableString(value)

    def __str__(self):
        return ''.join(self.characters)

    def __eq__(self, other):
        return self.characters == other.characters
