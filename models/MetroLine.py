from dataclasses import dataclass 
from enum import Enum


MetroLineTypes = Enum(
    "Underground",
    "MCC",
    "MCD"
)




@dataclass
class MetroLine(object):
    name:str
    color:str
    type:MetroLineTypes.value


