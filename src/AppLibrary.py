from app import app
from repositories.tip_repository import tip_repository
from services.tip_service import tip_service

class AppLibrary:
    def __init__(self):
        def __init__(self):
            self._tip_repository = tip_repository
            self._tip_service = tip_service
            self._app = app 