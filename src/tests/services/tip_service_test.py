import unittest
from services.tip_service import TipService
from repositories.tip_repository import TipRepository
from database import database_connection
from initialize_database import initialize_database

LOREM_LIPSUM = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean " \
               "commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis " \
               "dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, " \
               "pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec p"


class TestTipService(unittest.TestCase):
    def setUp(self):
        initialize_database()
        self.tip_repository = TipRepository(database_connection)
        self.tip_service = TipService()

    def test_add_new_tip_successful(self):
        self.tip_service.add_new_tip(
            "testiotsikko", "testikirjoittaja", "testiurl", "kuvaus", 1)
        tip_list = self.tip_repository.get_tips()
        title = tip_list[0].title
        self.assertEqual("testiotsikko", title)

    def test_add_new_tip_title_too_long(self):
        with self.assertRaises(Exception):
            self.tip_service.add_new_tip("testiotsikko111111111111111111111111111111111111111",
                                         "testikirjoittaja", "testiurl", "kuvaus", 1)

    def test_add_new_tip_title_too_short(self):
        with self.assertRaises(Exception):
            self.tip_service.add_new_tip(
                "t", "testikirjoittaja", "testiurl", "kuvaus", 1)

    def test_add_new_tip_description_too_long(self):
        description = LOREM_LIPSUM
        with self.assertRaises(Exception):
            self.tip_service.add_new_tip(
                "testiotsikko", "testikirjoittaja", "testiurl", description, 1)

    def test_add_new_tip_author_too_long(self):
        author = LOREM_LIPSUM
        with self.assertRaises(Exception):
            self.tip_service.add_new_tip(
                "testiotsikko", author, "testiurl", "kuvaus", 1)

    def test_get_visible_tips_only_returns_visible_tips(self):
        self.tip_service.add_new_tip(
            "testiotsikko", "testikirjoittaja", "testiurl", "kuvaus", 1)
        self.tip_service.add_new_tip(
            "testiotsikko", "testikirjoittaja", "testiurl", "kuvaus", 1)
        self.tip_service.delete_tip(1)
        tips = self.tip_service.get_visible_tips()
        self.assertEqual(len(tips), 1)

    def test_searching_tips_returns_correct_number_of_tips(self):
        self.tip_service.add_new_tip(
            "hästämälöö urmulee", "A.W. Yrjänä", "", "", 1)
        self.tip_service.add_new_tip(
            "hästämälöö urmuleeuujee", "A.W. Yrjänä", "", "", 1)
        self.tip_service.add_new_tip(
            "hästämälöö urmuleeheiheiheii", "A.W. Yrjänä", "", "", 1)
        tip_list = self.tip_service.get_visible_tips()
        search_list1 = self.tip_service.get_searched_tips("hästämälöö urmulee")
        search_list2 = self.tip_service.get_searched_tips(
            "hästämälöö urmuleeuujee")
        self.assertEqual(len(tip_list), 3)
        self.assertEqual(len(search_list1), 3)
        self.assertEqual(len(search_list2), 1)

    def test_add_isbn_tip_successful(self):
        self.tip_service.add_isbn_tip("9780446310789", "kuvaus", 1)
        tip_list = self.tip_repository.get_tips()
        self.assertEqual("To Kill A Mockingbird", tip_list[0].title)
        self.assertEqual("Harper Lee", tip_list[0].author)
        self.assertEqual("kuvaus", tip_list[0].description)

    def test_add_isbn_tip_no_isbn_numbe(self):
        with self.assertRaises(Exception):
            self.tip_service.add_isbn_tip("", "kuvaus", 1)

    def test_add_isbn_tip_isbn_not_valid(self):
        with self.assertRaises(Exception):
            self.tip_service.add_isbn_tip("111", "kuvaus", 1)

    def test_add_isbn_tip_isbn_not_found(self):
        with self.assertRaises(Exception):
            self.tip_service.add_isbn_tip("9789511253044", "kuvaus", 1)

    def test_add_isbn_tip_description_too_long(self):
        with self.assertRaises(Exception):
            self.tip_service.add_isbn_tip("9780446310789", LOREM_LIPSUM, 1)
