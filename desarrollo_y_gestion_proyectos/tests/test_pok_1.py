import unittest
from app.pokemon import Pokemon
from datetime import datetime
from bson import ObjectId

class TestPokemon(unittest.TestCase):
    def setUp(self) -> None:
        self.date_now = datetime.now()
        self.new_pokemon = Pokemon(pokedex_id=1,
                                   name="Bulbasaur",
                                   height=7,
                                   weight=69,
                                   atk=49,
                                   def_=49,
                                   atk_sp=65,
                                   def_sp=65,
                                   vel=45,
                                   hp=45,
                                   type_1="Grass",
                                   type_2="Poison",
                                   generation=1,
                                   genra="Leaf",
                                   is_legendary=False,
                                   is_mythical=False,
                                   is_default=True,
                                   shape="Quadruped",
                                   color="Green",
                                   evolution_chain=["Bulbasaur", "Ivysaur", "Venusaur"],
                                   sprite="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png",
                                   moves=["Tackle", "Vine Whip", "Razor Leaf", "Solar Beam"],
                                   capture_date=self.date_now)
        self.db_pokemon = self.new_pokemon.copy()
        self.db_pokemon.id = ObjectId()

    def test_new_pokemon(self):
        """
        Test de la clase Pokemon simulando un pokemon nuevo
        """
        self.assertIsNone(self.new_pokemon.id)
        self.assertEqual(self.new_pokemon.pokedex_id, 1)
        self.assertEqual(self.new_pokemon.name, "Bulbasaur")
        self.assertEqual(self.new_pokemon.height, 7)
        self.assertEqual(self.new_pokemon.weight, 69)
        self.assertEqual(self.new_pokemon.atk, 49)
        self.assertEqual(self.new_pokemon.def_, 49)
        self.assertEqual(self.new_pokemon.atk_sp, 65)
        self.assertEqual(self.new_pokemon.def_sp, 65)
        self.assertEqual(self.new_pokemon.vel, 45)
        self.assertEqual(self.new_pokemon.hp, 45)
        self.assertEqual(self.new_pokemon.type_1, "Grass")
        self.assertEqual(self.new_pokemon.type_2, "Poison")
        self.assertEqual(self.new_pokemon.generation, 1)
        self.assertEqual(self.new_pokemon.genra, "Leaf")
        self.assertEqual(self.new_pokemon.is_legendary, False)
        self.assertEqual(self.new_pokemon.is_mythical, False)
        self.assertEqual(self.new_pokemon.is_default, True)
        self.assertEqual(self.new_pokemon.shape, "Quadruped")
        self.assertEqual(self.new_pokemon.color, "Green")
        self.assertEqual(self.new_pokemon.evolution_chain, ["Bulbasaur", "Ivysaur", "Venusaur"])
        self.assertEqual(self.new_pokemon.sprite, "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png")
        self.assertEqual(self.new_pokemon.moves, ["Tackle", "Vine Whip", "Razor Leaf", "Solar Beam"])
        self.assertEqual(self.new_pokemon.capture_date, self.date_now)

    def test_db_pokemon(self):
        """
        Test de la clase Pokemon simulando un pokemon obtenido de la base de datos
        """
        self.assertIsInstance(self.db_pokemon.id, ObjectId)
        self.assertNotEqual(self.db_pokemon.id, self.new_pokemon.id)
        self.assertEqual(self.db_pokemon.pokedex_id, self.new_pokemon.pokedex_id)
        self.assertEqual(self.db_pokemon.name, self.new_pokemon.name)
        self.assertEqual(self.db_pokemon.height, self.new_pokemon.height)
        self.assertEqual(self.db_pokemon.weight, self.new_pokemon.weight)
        self.assertEqual(self.db_pokemon.atk, self.new_pokemon.atk)
        self.assertEqual(self.db_pokemon.def_, self.new_pokemon.def_)
        self.assertEqual(self.db_pokemon.atk_sp, self.new_pokemon.atk_sp)
        self.assertEqual(self.db_pokemon.def_sp, self.new_pokemon.def_sp)
        self.assertEqual(self.db_pokemon.vel, self.new_pokemon.vel)
        self.assertEqual(self.db_pokemon.hp, self.new_pokemon.hp)
        self.assertEqual(self.db_pokemon.type_1, self.new_pokemon.type_1)
        self.assertEqual(self.db_pokemon.type_2, self.new_pokemon.type_2)
        self.assertEqual(self.db_pokemon.generation, self.new_pokemon.generation)
        self.assertEqual(self.db_pokemon.genra, self.new_pokemon.genra)
        self.assertEqual(self.db_pokemon.is_legendary, self.new_pokemon.is_legendary)
        self.assertEqual(self.db_pokemon.is_mythical, self.new_pokemon.is_mythical)
        self.assertEqual(self.db_pokemon.is_default, self.new_pokemon.is_default)
        self.assertEqual(self.db_pokemon.shape, self.new_pokemon.shape)
        self.assertEqual(self.db_pokemon.color, self.new_pokemon.color)
        self.assertEqual(self.db_pokemon.evolution_chain, self.new_pokemon.evolution_chain)
        self.assertEqual(self.db_pokemon.sprite, self.new_pokemon.sprite)
        self.assertEqual(self.db_pokemon.moves, self.new_pokemon.moves)
        self.assertEqual(self.db_pokemon.capture_date, self.new_pokemon.capture_date)
