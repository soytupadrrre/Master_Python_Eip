import pymongo
from app import PokemonRepository
from configparser import ConfigParser
from app.models.pokemon import create_pokemon

config = ConfigParser()
config.read("config.ini")
db_data = config["mongodb"]

def init_connection(test=False):
    if test:
        return pymongo.MongoClient(db_data["host"],
                               int(db_data["port"]),
                               username=db_data["test_username"],
                               password=db_data["test_password"])

    return pymongo.MongoClient(db_data["host"], 
                               int(db_data["port"]), 
                               username=db_data["username"], 
                               password=db_data["password"])

def poc_get_all_pokemon(pkm_repo: PokemonRepository):
    print("Getting all pokemons from db...")
    for pokemon in pkm_repo.find_by({}):
        print(f"Document ID {pokemon.id}, Pokemon Name: {pokemon.name}, Pokedex ID: {pokemon.pokedex_id}")
    print("Done.\n")

def poc_get_pokemon_by(pkm_repo: PokemonRepository):
    fields = ["name", "pokedex_id"]
    field = ""
    while field not in fields:
        field = input(f"Choose a field ({', '.join(fields)}): ")
        if field not in fields:
            print("Invalid input, try again.")
    value = input("Enter value: ")
    query = {field: value}
    print(f"Getting pokemon by {field} {value} from db...")
    for pokemon in pkm_repo.find_by(query):
        print(f"Document ID {pokemon.id}, Pokemon Name: {pokemon.name}, Pokedex ID: {pokemon.pokedex_id}")
    print("Done.\n")

def poc_search_and_save_pokemon(pkm_repo: PokemonRepository):
    value = input("Enter pokedex ID or name: ")
    try:
        value = int(value)
    except ValueError:
        pass
    print(f"Searching for pokemon {value}...")
    pokemon = create_pokemon(value)
    if pokemon:
        print(f"Pokemon found: {pokemon.name}")
        print("Saving to db...")
        pkm_repo.save(pokemon)
        print("Done.\n")
    else:
        print("Pokemon not found.\n")

def poc_delete_pokemon(pkm_repo: PokemonRepository):
    fields = ["name", "pokedex_id"]
    field = ""
    while field not in fields:
        field = input(f"Choose a field ({', '.join(fields)}): ")
        if field not in fields:
            print("Invalid input, try again.")
    value = input("Enter value: ")
    try:
        value = int(value)
    except ValueError:
        pass
    query = {field: value}
    print(f"Getting pokemon by {field} {value} from db...")
    for pokemon in pkm_repo.find_by(query):
        deleted = pkm_repo.delete(pokemon)
        if deleted:
            print(f"Pokemon {pokemon.name} deleted.")
    print("Done.\n")


def db_menu():
    answer = ""
    while answer != "q":
        answer = input("Do you want to use the test database? (y/n/q): ")
        if answer == "y":
            test = True
            db = "test_pokedex"
            break
        elif answer == "n":
            test = False
            db = "pokedex"
            break
        elif answer == "q":
            break
        else:
            print("Invalid input, try again.")

    client = init_connection(test)
    return client[db]

if __name__ == "__main__":
    pkm_repo = PokemonRepository(db_menu())
    action = ""
    while action != "q":
        action = input("""Choose an action (q to quit): 
1. Get all pokemons (from db)
2. Get pokemon by (from db)
3. Search and Save pokemon to db
4. Delete pokemon from db\n""")
        if action == "1":
            poc_get_all_pokemon(pkm_repo)
        elif action == "2":
            poc_get_pokemon_by(pkm_repo)
        elif action == "3":
            poc_search_and_save_pokemon(pkm_repo)
        elif action == "4":
            poc_delete_pokemon(pkm_repo)
        elif action == "q":
            break
        else:
            print("Invalid input, try again.")


