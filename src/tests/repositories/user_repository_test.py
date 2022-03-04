import unittest
from repositories.user_repository import UserRepository
from database import database_connection
from initialize_database import initialize_database

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        initialize_database()
        self.user_repository = UserRepository(database_connection)

    def test_add_user(self):
        self.user_repository.add_user("kayttajanimi", "salasana", "nimi")

        self.assertEqual(True, self.user_repository.get_user("kayttajanimi"))

    def test_get_user_find_user(self):
        self.user_repository.add_user("kayttajanimi2", "salasana", "nimi")
        result = self.user_repository.get_user("kayttajanimi2")

        self.assertEqual(result, True)

    def test_get_user_nonexistent_user(self):
        self.user_repository.add_user("kayttajanimi3", "salasana", "nimi")
        result = self.user_repository.get_user("kayttajanimi4")

        self.assertEqual(result, False)

    def test_correct_password_returns_true(self):
        username = "user"
        password = "salasana"
        self.user_repository.add_user(username, password, "nimi")
        result = self.user_repository.check_password(username, password)
        self.assertTrue(result)

    def test_incorrect_password_returns_false(self):
        username = "user"
        self.user_repository.add_user(username, "salasana", "nimi")
        result = self.user_repository.check_password(username, "salasana123")
        self.assertFalse(result)

    def test_get_name_and_id_returns_correct_result(self):
        username = "user"
        name = "nimi"
        self.user_repository.add_user("anna", "anna", "anna")
        self.user_repository.add_user(username, "salasana", name)
        name_result, id_result = self.user_repository.get_name_and_id(username)
        self.assertEqual(name_result, name)
        self.assertEqual(id_result, 2)
