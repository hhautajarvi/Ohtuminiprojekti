import unittest
from services.tip_service import TipService
from repositories.tip_repository import TipRepository
from database import database_connection

class TestTipService(unittest.TestCase):
    def setUp(self):
        self.tip_repository = TipRepository(database_connection)
        self.tip_service = TipService()

    def test_add_new_tip_successful(self):
        self.tip_service.add_new_tip("testiotsikko", "testiurl", "kuvaus", 1)
        list = self.tip_repository.get_tips()
        title = list[0].title
        self.assertEqual("testiotsikko",title)

    def test_add_new_tip_title_too_long(self):
        with self.assertRaises(Exception):
            self.tip_service.add_new_tip("testiotsikko111111111111111111111111111111111111111", "testiurl", "kuvaus", 1)

    def test_add_new_tip_title_too_short(self):
        with self.assertRaises(Exception):
            self.tip_service.add_new_tip("t", "testiurl", "kuvaus", 1)

    def test_add_new_tip_description_too_long(self):
        description = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec p"
        with self.assertRaises(Exception):
            self.tip_service.add_new_tip("testiotsikko", "testiurl", description, 1)