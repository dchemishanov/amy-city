from unittest import mock, TestCase

from ..engine.engine import Engine


class EngineTest(TestCase):
    def setUp(self):
        self.engine = Engine([{}, {}])

    def test_is_candidate__success(self):
        result = self.engine._is_candidate({"name": "London"}, "lon")
        self.assertEqual(result, True)

    def test_is_candidate__fail(self):
        result = self.engine._is_candidate({"name": "London"}, "Paris")
        self.assertEqual(result, False)

    def test_score__with_beginning(self):
        result = self.engine._score({"name": "London"}, "Lon", 0.0, 0.0)
        self.assertEqual(result, 1.0)

    def test_score__with_inner_string(self):
        result = self.engine._score({"name": "London"}, "don", 0.0, 0.0)
        self.assertEqual(result, 0.25)

    def test_get_full_city_name(self):
        result = self.engine._get_full_city_name({"name": "Berlin"})
        self.assertEqual(result, "Berlin")

    def test_match(self):
        pass
