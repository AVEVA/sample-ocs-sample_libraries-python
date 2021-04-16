from enum import Flag


class SdsStreamViewMode(Flag):
    """
    SdsStreamViewMode 0-32
    """
    none = 0
    FieldAdd = 1
    FieldRemove = 2
    FieldRename = 4
    FieldMove = 8
    FieldConversion = 16
    InvalidFieldConversion = 32
