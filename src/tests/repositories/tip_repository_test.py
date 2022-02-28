import unittest
from repositories.tip_repository import TipRepository
from database import database_connection

class TestTipRepository(unittest.TestCase):
    def setUp(self):
        self.tip_repository = TipRepository(database_connection)

    def test_add_tip(self):
        self.tip_repository.add_tip("testiotsikko", "testiurl", "kuvaus", 1)
        list = self.tip_repository.get_tips()
        title = list[0].title
        self.assertEqual("testiotsikko",title)