from project.toy_store import ToyStore
import unittest

class TestToyStore(unittest.TestCase):
    def setUp(self):
        self.store = ToyStore()

    def test_init(self):
        # Test that the toy_shelf attribute is initialized correctly
        expected_shelf = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        self.assertDictEqual(self.store.toy_shelf, expected_shelf)

    def test_add_toy(self):
        # Test that add_toy raises an exception if the shelf doesn't exist
        with self.assertRaises(Exception) as cm:
            self.store.add_toy("H", "Barbie")
        self.assertEqual(str(cm.exception), "Shelf doesn't exist!")

        # Test that add_toy raises an exception if the shelf is already taken
        self.store.add_toy("A", "Barbie")
        with self.assertRaises(Exception) as cm:
            self.store.add_toy("A", "Teddy Bear")
        self.assertEqual(str(cm.exception), "Shelf is already taken!")

        # Test that add_toy raises an exception if the toy is already in the shelf
        with self.assertRaises(Exception) as cm:
            self.store.add_toy("A", "Barbie")
        self.assertEqual(str(cm.exception), "Toy is already in shelf!")

        # Test that add_toy adds a toy to the shelf successfully
        self.assertEqual(self.store.add_toy("B", "Teddy Bear"), "Toy:Teddy Bear placed successfully!")
        self.assertEqual(self.store.toy_shelf["B"], "Teddy Bear")

    def test_remove_toy(self):
        # Test that remove_toy raises an exception if the shelf doesn't exist
        with self.assertRaises(Exception) as cm:
            self.store.remove_toy("H", "Barbie")
        self.assertEqual(str(cm.exception), "Shelf doesn't exist!")

        # Test that remove_toy raises an exception if the toy is not in the shelf
        with self.assertRaises(Exception) as cm:
            self.store.remove_toy("A", "Teddy Bear")
        self.assertEqual(str(cm.exception), "Toy in that shelf doesn't exists!")

        # Test that remove_toy removes a toy from the shelf successfully
        self.store.add_toy("C", "Rubik's Cube")
        self.assertEqual(self.store.remove_toy("C", "Rubik's Cube"), "Remove toy:Rubik's Cube successfully!")
        self.assertIsNone(self.store.toy_shelf["C"])

