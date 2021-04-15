from enum import Enum


class SdsStreamViewMode(Enum):
    """
    SdsStreamViewMode 0-32
    """
    none = 0,
    FieldAdd = 1,
    FieldRemove = 2,
    FieldRename = 3,
    FieldMove = 8,
    FieldConversion = 16,
    InvalidFieldConversion = 32
