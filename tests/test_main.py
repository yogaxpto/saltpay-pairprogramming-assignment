from unittest import TestCase

import main


class MainTest(TestCase):
    def test_double(self) -> None:
        self.assertEqual(4, main.double(2))
