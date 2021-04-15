from enum import Enum


class SdsInterpolationMode(Enum):
    """
    SdsInterpolationMode 0-5
    """
    Continuous = 0
    StepwiseContinuousLeading = 1
    StepwiseContinuousTrailing = 2
    Discrete = 3
    ContinuousNullableLeading = 4
    ContinuousNullableTrailing = 5
