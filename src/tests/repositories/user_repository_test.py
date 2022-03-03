import unittest
from repositories.user_repository import UserRepository
from database import database_connection

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.user_repository = UserRepository(database_connection)

    def test_add_user(self):
        self.user_repository.add_user("kayttajanimi", "salasana", "nimi")

        self.assertEqual(True, self.user_repository.get_user("kayttajanimi"))

    def test_get_user_find_user(self):
        self.user_repository.add_user("kayttajanimi2", "salasana", "nimi")
        result = self.user_repository.get_user("kayttajanimi2")

        self.assertEqual(result, True)

    def test_get_user_nonexistent_user(self):
        self.user_repository.add_user("kayttajanimi2", "salasana", "nimi")
        result = self.user_repository.get_user("kayttajanimi3")

        self.assertEqual(result, False)