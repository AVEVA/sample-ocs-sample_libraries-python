from enum import Enum


class SdsExtrapolationMode(Enum):
    """
    SdsExtrapolationMode 0-3
    """
    All = 0
    None_ = 1
    Forward = 2
    Backward = 3
