# -*- coding: utf-8 -*-

from .context import kotahi

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_game(self):
        assert True


if __name__ == '__main__':
    unittest.main()
