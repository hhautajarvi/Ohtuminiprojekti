import unittest
from entities.tip import Tip

class TestTip(unittest.TestCase):
    def setUp(self):
        self.tip = Tip(1, "otsikko", "kirjoittaja", "https://www.youtube.com/", "kuvaus", 1, 1)

    def test_constructor_works(self):
        self.assertEqual(1, self.tip.id)
        self.assertEqual("otsikko", self.tip.title)
        self.assertEqual("kirjoittaja", self.tip.author)
        self.assertEqual("https://www.youtube.com/", self.tip.url)
        self.assertEqual("kuvaus", self.tip.description)
        self.assertEqual(1, self.tip.visible)
        self.assertEqual(1, self.tip.user_id)
