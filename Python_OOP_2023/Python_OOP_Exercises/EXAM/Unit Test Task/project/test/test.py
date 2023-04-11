from project.tennis_player import TennisPlayer


import unittest

class TestTennisPlayer(unittest.TestCase):

    def test_init(self):
        player = TennisPlayer("Roger Federer", 39, 9820.0)
        self.assertEqual(player.name, "Roger Federer")
        self.assertEqual(player.age, 39)
        self.assertEqual(player.points, 9820.0)
        self.assertEqual(player.wins, [])

    def test_init_with_invalid_name(self):
        with self.assertRaises(ValueError) as context:
            TennisPlayer("AB", 20, 1000.0)
        self.assertEqual(str(context.exception), "Name should be more than 2 symbols!")

    def test_init_with_invalid_age(self):
        with self.assertRaises(ValueError) as context:
            TennisPlayer("Novak Djokovic", 17, 10500.0)
        self.assertEqual(str(context.exception), "Players must be at least 18 years of age!")

    def test_name_property(self):
        player = TennisPlayer("Rafael Nadal", 35, 9865.0)
        player.name = "Rafa Nadal"
        self.assertEqual(player.name, "Rafa Nadal")
        with self.assertRaises(ValueError) as context:
            player.name = "A"
        self.assertEqual(str(context.exception), "Name should be more than 2 symbols!")

    def test_age_property(self):
        player = TennisPlayer("Andy Murray", 34, 1865.0)
        player.age = 35
        self.assertEqual(player.age, 35)
        with self.assertRaises(ValueError) as context:
            player.age = 17
        self.assertEqual(str(context.exception), "Players must be at least 18 years of age!")

    def test_add_new_win(self):
        player = TennisPlayer("Serena Williams", 40, 7865.0)
        self.assertEqual(player.add_new_win("Australian Open"), None)
        self.assertEqual(player.add_new_win("Wimbledon"), None)
        self.assertEqual(player.add_new_win("Wimbledon"), "Wimbledon has been already added to the list of wins!")

    def test_lt_operator(self):
        player1 = TennisPlayer("Rafael Nadal", 35, 9865.0)
        player2 = TennisPlayer("Novak Djokovic", 34, 10770.0)
        self.assertEqual(player1 < player2, "Novak Djokovic is a top seeded player and he/she is better than Rafael Nadal")

    def test_str_method(self):
        player = TennisPlayer("Serena Williams", 40, 7865.0)
        player.add_new_win("Australian Open")
        player.add_new_win("Wimbledon")
        self.assertEqual(str(player), "Tennis Player: Serena Williams\nAge: 40\nPoints: 7865.0\nTournaments won: Australian Open, Wimbledon")

if __name__ == '__main__':
    unittest.main()
