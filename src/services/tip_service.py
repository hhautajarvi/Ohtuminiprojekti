from src.repositories.tip_repository import tip_repository as default_tip_repository
from src.entities.tip import Tip

class TipService:
    def __init__(self, tip_repository=default_tip_repository):
        self._tip_repository = tip_repository

    def add_new_tip(self, title, url, description, user_id):
        if len(title) < 3 or len(title) > 50:
            raise Exception("Anna otsikko 3-50 merkin pituisena")
        if len(description) > 300:
            raise Exception("Anna enintään 300 merkin pituinen kuvaus")
        self._tip_repository.add_tip(title, url, description, user_id)
        new_tip = Tip(title, url, description, user_id)

tip_service = TipService()