import unittest
from unittest.mock import patch
from services.user_service import UserInputError, UserService
from repositories.user_repository import UserRepository
from database import database_connection
from initialize_database import initialize_database


class UserServiceTest(unittest.TestCase):
    def setUp(self):
        initialize_database()
        self.user_repository = UserRepository(database_connection)
        self.user_service = UserService(self.user_repository)

    def test_create_user_valid(self):
        self.user_service.create_user(
            "testinimi", "testikayttajanimi", "salasana", "salasana")
        result = self.user_repository.get_user("testikayttajanimi")

        self.assertEqual(result, True)

    def test_create_user_username_taken(self):
        self.user_service.create_user(
            "testinimi2", "testikayttajanimi2", "salasana", "salasana")
        with self.assertRaises(UserInputError):
            self.user_service.create_user(
                "testinimi2", "testikayttajanimi2", "salasana", "salasana")

    def test_validate_passwords_dont_match(self):
        with self.assertRaises(UserInputError):
            self.user_service.validate(
                "testinimi10", "testikayttajanimi10", "salasanaA", "salasanaB")

    def test_incorrect_password_returns_error(self):
        self.user_service.create_user(
            "testinimi", "testikayttajanimi", "salasana", "salasana")
        with self.assertRaises(UserInputError):
            self.user_service.login("testikayttajanimi", "vaarasalasana")

    @patch.object(UserService, "_set_session")
    def test_correct_password_calls_set_session(self, mock):
        self.user_service.create_user(
            "testinimi", "testikayttajanimi", "salasana", "salasana")
        self.user_service.login("testikayttajanimi", "salasana")
        mock.assert_called()
