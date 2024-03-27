from django.test import TestCase, Client

# Create your tests here.

class QuranAPITestCase(TestCase):
    def setUp(self) -> None:
        c = Client()
        res = c.get("https://quran.kemenag.go.id")
        print(res.status_code)
        return super().setUp()