from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from lists.views import home_page  # this view hasn't been written
from django.template.loader import render_to_string


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home(self):
        found = resolve('/')  # internal django function to resolve urls
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        # this tests our implementation, not constants.
        self.assertEqual(response.content.decode(), expected_html)
