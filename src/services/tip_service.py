from repositories.tip_repository import tip_repository as default_tip_repository

class TipService:
    def __init__(self, tip_repository=default_tip_repository):
        self._tip_repository = tip_repository

    def add_new_tip(self, title, url, description, user_id):
        if len(title) < 3 or len(title) > 50:
            raise Exception("Anna otsikko 3-50 merkin pituisena")
        if len(description) > 300:
            raise Exception("Anna enintään 300 merkin pituinen kuvaus")
        self._tip_repository.add_tip(title, url, description, user_id)

    def get_visible_tips(self):
        tips = self._tip_repository.get_tips()
        visible_tips = [tip for tip in tips if tip.visible==1]
        return visible_tips

    def delete_tip(self, id):
        return self._tip_repository.hide_tip(id)

tip_service = TipService()