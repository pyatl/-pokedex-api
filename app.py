from fastapi import (
    FastAPI,
    status,
)
from pydantic import (
    BaseModel,
    ValidationError,
)

from models import (
    Pokemon,
    PokemonType,
)

class PokemonSchema(BaseModel):
    pokemon_type: int
    national_index: int
    name: str


app = FastAPI()


@app.get("/")
async def index():
    return {"message": "welcome to my awesome pokedex"}

@app.post(
    "/pokemon",
    response_model=PokemonSchema,
    status_code=status.HTTP_201_CREATED
)
async def pokemon(pokemon: PokemonSchema):
    
    try:
        new_pokemon = Pokemon(
            pokemon_type=PokemonType(pokemon.pokemon_type),
            national_index=pokemon.national_index,
            name=pokemon.name
        )

    except ValidationError as e:
        print(e)


    response_pokemon = PokemonSchema(
        pokemon_type=new_pokemon.pokemon_type,
        national_index=new_pokemon.national_index,
        name=new_pokemon.name
    )

    return response_pokemon