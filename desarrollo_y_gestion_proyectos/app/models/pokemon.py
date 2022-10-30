from datetime import datetime
from typing import List, Union, Optional

from bson import ObjectId
from pydantic import BaseModel
from pydantic_mongo import ObjectIdField, AbstractRepository
import vlm_pypoke

client = vlm_pypoke.PokeClient()


class Pokemon(BaseModel):
    id: ObjectIdField = None
    pokedex_id: int
    name: str
    height: int
    weight: int
    atk: int
    def_: int
    atk_sp: int
    def_sp: int
    vel: int
    hp: int
    type_1: str
    type_2: Optional[str] = None
    generation: int
    genra: str
    is_legendary: bool
    is_mythical: bool
    is_default: bool
    shape: str
    color: str
    evolution_chain: List[str]
    sprite: str
    moves: List[str]
    capture_date: datetime
    
    class Config:
        json_encoders = {ObjectId: str}

class PokemonRepository(AbstractRepository[Pokemon]):
    class Meta:
        collection_name = "pokemons"

def create_pokemon(value: Union[str, int]) -> Optional[Pokemon]:
    if isinstance(value, str):
        value = value.lower()
    try:
        pokemon_data = client.get_pokemon(value)
        pokemon_species_data = client.get_pokemon_species(value)
        pokemon_evolution_chain = client.get_evolution_chain(pokemon_species_data["evolution_chain"]["url"].split("/")[-2])

        pkm_type_2 = None
        if len(pokemon_data["types"]) > 1:
            pkm_type_2 = pokemon_data["types"][1]["type"]["name"]

        for gen in pokemon_species_data["genera"]:
            if gen["language"]["name"] == "en":
                genra = gen["genus"]
                break
        else:
            genra = None

        evolution_chain = []

        if pokemon_species_data["evolves_from_species"] and \
        pokemon_species_data["evolves_from_species"]["name"] not in evolution_chain:
            evolution_chain.append(pokemon_species_data["evolves_from_species"]["name"])
            
        for chain in pokemon_evolution_chain["chain"]["evolves_to"]:
            if chain["species"]["name"] != pokemon_data["name"]:
                evolution_chain.append(chain["species"]["name"])
            for chain2 in chain["evolves_to"]:
                evolution_chain.append(chain2["species"]["name"])
        
        return Pokemon(pokedex_id=pokemon_data['id'],
                       name=pokemon_data['name'],
                       height=pokemon_data['height'],
                       weight=pokemon_data['weight'],
                       atk=pokemon_data["stats"][1]["base_stat"],
                       def_=pokemon_data["stats"][2]["base_stat"],
                       hp=pokemon_data["stats"][0]["base_stat"],
                       atk_sp=pokemon_data["stats"][3]["base_stat"],
                       def_sp=pokemon_data["stats"][4]["base_stat"],
                       vel=pokemon_data["stats"][5]["base_stat"],
                       sprite=pokemon_data["sprites"]["other"]["official-artwork"]["front_default"],
                       type_1=pokemon_data["types"][0]["type"]["name"],
                       type_2=pkm_type_2,
                       generation=pokemon_species_data["generation"]["url"].split("/")[-2],
                       genra=genra,
                       is_legendary=pokemon_species_data["is_legendary"],
                       is_mythical=pokemon_species_data["is_mythical"],
                       is_default=pokemon_data["is_default"],
                       shape=pokemon_species_data["shape"]["name"],
                       color=pokemon_species_data["color"]["name"],
                       evolution_chain=list(dict.fromkeys(evolution_chain)),
                       moves=[m["move"]["name"] for m in pokemon_data["moves"]],
                       capture_date=datetime.now())

    except Exception:
        return None
