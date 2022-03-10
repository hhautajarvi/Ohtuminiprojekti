from isbnlib import meta, notisbn
from repositories.tip_repository import tip_repository as default_tip_repository

SERVICE = "goob" #Bookservice for isbn-metadata. 'goob' for Google Books service
                #'openl' for OpenLibrary.org and 'wiki' for wikipedia.org

class TipService:
    def __init__(self, tip_repository=default_tip_repository):
        self._tip_repository = tip_repository

    def add_new_tip(self, title, author, url, description, user_id):
        if len(title) < 3 or len(title) > 50:
            raise Exception("Anna otsikko 3-50 merkin pituisena")
        if len(author) > 100:
            raise Exception("Anna kirjoittajan nimi enintään 100 merkin pituisena")
        if len(description) > 300:
            raise Exception("Anna enintään 300 merkin pituinen kuvaus")
        self._tip_repository.add_tip(title, author, url, description, user_id)

    def add_isbn_tip(self, isbn_number, isbn_description, user_id):
        if len(isbn_number) == 0:
            raise Exception("Anna ISBN-numero")
        if notisbn(isbn_number, level='strict'):
            raise Exception("Numero ei ole kelpaava ISBN-numero")
        try:
            book = meta(isbn_number, SERVICE)
            author = ', '.join(book["Authors"])
        except:
            raise Exception("ISBN-numerolla ei löytynyt kirjaa")
        if len(isbn_description) > 300:
            raise Exception("Anna enintään 300 merkin pituinen kuvaus")
        url = ""
        self._tip_repository.add_tip(book["Title"], author, url, isbn_description, user_id)

    def get_visible_tips(self):
        tips = self._tip_repository.get_tips()
        visible_tips = [tip for tip in tips if tip.visible==1]
        return visible_tips

    def delete_tip(self, tip_id):
        return self._tip_repository.hide_tip(tip_id)

tip_service = TipService()
