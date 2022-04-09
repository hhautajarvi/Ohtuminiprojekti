import secrets
from flask import session
from repositories.user_repository import user_repository as default_user_repository


class UserInputError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def create_user(self, name, username, password, password_confirmation):
        self.validate(name, username, password, password_confirmation)
        if not self._user_repository.get_user(username):
            if self._user_repository.add_user(username, password, name):
                return True
        else:
            raise UserInputError("Käyttäjätunnus on jo olemassa.")

    def validate(self, name, username, password, password_confirmation):
        if not name or not username or not password or not password_confirmation:
            raise UserInputError("Kaikkia kenttiä ei ole täytetty.")
        if password != password_confirmation:
            raise UserInputError(
                "Salasana ja salasanan vahvistus eivät täsmää.")

    def login(self, username, password):
        if not self._user_repository.check_password(username, password):
            raise UserInputError('Käyttäjätunnus tai salasana eivät täsmää')
        self._set_session(username)

    def _set_session(self, username):
        name_and_id = self._user_repository.get_name_and_id(username)

        session["name"] = name_and_id[0]
        session["user_id"] = name_and_id[1]
        session["scrf_token"] = secrets.token_hex(16)

    def logout(self):
        del session["user_id"]


user_service = UserService()
