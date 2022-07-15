from enum import Enum

from pydantic import (
    BaseModel,
    validator,
    ValidationError,
)


class PokemonType(Enum):
    WATER = 1
    FIRE = 2
    GRASS = 3
    GROUND = 4
    DRAGON = 5
    FLYING = 6
    FAIRY = 7
    GHOST = 8
    NORMAL = 9
    ELECTRIC = 10
    ICE = 11

# TODO
# calculate type weakness

class Pokemon(BaseModel):
    pokemon_type: PokemonType 
    national_index: int
    name: str

    @validator('name')
    def validate_name(cls, value):
        if 'Ian' in value:
            raise ValidationError
        return value



