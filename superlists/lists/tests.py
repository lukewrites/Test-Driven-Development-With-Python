from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from lists.views import home_page  # this view hasn't been written


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home(self):
        found = resolve('/')  # internal django function to resolve urls
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        # we use b'...' because response.context is in bytes, not a string.
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
