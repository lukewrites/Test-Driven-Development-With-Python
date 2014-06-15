from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page  # this view hasn't been written


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home(self):
        found = resolve('/')  # internal django function to resolve urls
        self.assertEqual(found.func, home_page)
