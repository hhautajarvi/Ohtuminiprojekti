import unittest
from repositories.tip_repository import TipRepository
from database import database_connection
from initialize_database import initialize_database

class TestTipRepository(unittest.TestCase):
    def setUp(self):
        initialize_database()
        self.tip_repository = TipRepository(database_connection)

    def test_add_tip(self):
        self.tip_repository.add_tip("testiotsikko", "testiurl", "kuvaus", 1)
        list = self.tip_repository.get_tips()
        title = list[0].title
        self.assertEqual("testiotsikko",title)

    def test_get_tips_returns_correct_number_of_tips(self):
        self.tip_repository.add_tip("testiotsikko", "testiurl", "kuvaus", 1)
        self.tip_repository.add_tip("testiotsikko2", "testiurl", "kuvaus", 1)
        self.tip_repository.add_tip("testiotsikko3", "testiurl", "kuvaus", 2, 0)
        list = self.tip_repository.get_tips()
        self.assertEqual(len(list),3)

    def test_tip_is_visible_by_default(self):
        self.tip_repository.add_tip("testiotsikko", "testiurl", "kuvaus", 1)
        list = self.tip_repository.get_tips()
        self.assertEqual(list[0].visible,1)

    def test_hide_tip_changes_tip_visibility(self):
        self.tip_repository.add_tip("testiotsikko", "testiurl", "kuvaus", 1)
        self.tip_repository.hide_tip(1)
        list = self.tip_repository.get_tips()
        self.assertEqual(list[0].visible,0)