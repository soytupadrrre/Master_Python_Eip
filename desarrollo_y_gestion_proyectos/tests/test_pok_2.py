import unittest
from datetime import datetime
from app.pokemon import Pokemon, create_pokemon


class TestsConnector(unittest.TestCase):
    def setUp(self) -> None:
        self.test_pokemon = Pokemon(
            id = None, 
            pokedex_id = 25, 
            name = 'pikachu', 
            height = 4, 
            weight = 60, 
            atk = 55, 
            def_ = 40, 
            atk_sp = 50, 
            def_sp = 50, 
            vel = 90, 
            hp = 35, 
            type_1 = 'electric', 
            type_2 = None, 
            generation = 1, 
            genra = 'Mouse Pokémon', 
            is_legendary = False, 
            is_mythical = False, 
            is_default = True, 
            shape = 'quadruped', 
            color = 'yellow', 
            evolution_chain = ['pichu', 'raichu'], 
            sprite = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png', 
            moves = ['mega-punch', 
                'pay-day', 'thunder-punch', 'slam', 'double-kick', 'mega-kick', 'headbutt', 'body-slam', 'take-down', 'double-edge', 'tail-whip', 'growl', 'surf', 'submission', 'counter', 'seismic-toss', 'strength', 'thunder-shock', 'thunderbolt', 'thunder-wave', 'thunder', 'dig', 'toxic', 'agility', 'quick-attack', 'rage', 'mimic', 'double-team', 'defense-curl', 'light-screen', 'reflect', 'bide', 'swift', 'skull-bash', 'flash', 'rest', 'substitute', 'thief', 'snore', 'curse', 'reversal', 'protect', 'sweet-kiss', 'mud-slap', 'zap-cannon', 'detect', 'endure', 'charm', 'rollout', 'swagger', 'spark', 'attract', 'sleep-talk', 'return', 'frustration', 'dynamic-punch', 'encore', 'iron-tail', 'hidden-power', 'rain-dance', 'rock-smash', 'uproar', 'facade', 'focus-punch', 'helping-hand', 'brick-break', 'knock-off', 'secret-power', 'signal-beam', 'covet', 'volt-tackle', 'calm-mind', 'shock-wave', 'natural-gift', 'feint', 'fling', 'magnet-rise', 'nasty-plot', 'discharge', 'captivate', 'grass-knot', 'charge-beam', 'electro-ball', 'round', 'echoed-voice', 'volt-switch', 'electroweb', 'wild-charge', 'draining-kiss', 'play-rough', 'play-nice', 'confide', 'electric-terrain', 'nuzzle', 'laser-focus', 'rising-voltage'], 
            capture_date = datetime.now()
        )
        return super().setUp()

    def create_pokemon(self):
        generated = create_pokemon("pikachu")
        self.assertEqual(generated.name, self.test_pokemon.name)
        self.assertEqual(generated.pokedex_id, self.test_pokemon.pokedex_id)
        self.assertEqual(generated.height, self.test_pokemon.height)
        self.assertEqual(generated.weight, self.test_pokemon.weight)
        self.assertEqual(generated.atk, self.test_pokemon.atk)
        self.assertEqual(generated.def_, self.test_pokemon.def_)
        self.assertEqual(generated.atk_sp, self.test_pokemon.atk_sp)
        self.assertEqual(generated.def_sp, self.test_pokemon.def_sp)
        self.assertEqual(generated.vel, self.test_pokemon.vel)
        self.assertEqual(generated.hp, self.test_pokemon.hp)
        self.assertEqual(generated.type_1, self.test_pokemon.type_1)
        self.assertEqual(generated.type_2, self.test_pokemon.type_2)
        self.assertEqual(generated.generation, self.test_pokemon.generation)
        self.assertEqual(generated.genra, self.test_pokemon.genra)
        self.assertEqual(generated.is_legendary, self.test_pokemon.is_legendary)
        self.assertEqual(generated.is_mythical, self.test_pokemon.is_mythical)
        self.assertEqual(generated.is_default, self.test_pokemon.is_default)
        self.assertEqual(generated.shape, self.test_pokemon.shape)
        self.assertEqual(generated.color, self.test_pokemon.color)
        self.assertEqual(generated.evolution_chain, self.test_pokemon.evolution_chain)
        self.assertEqual(generated.sprite, self.test_pokemon.sprite)
        self.assertEqual(generated.moves, self.test_pokemon.moves)
        self.assertIsInstance(generated.capture_date, datetime)