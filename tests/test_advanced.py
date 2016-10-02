# -*- coding: utf-8 -*-

from .context import kotahi

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_game(self):
        kotahi.board()


if __name__ == '__main__':
    unittest.main()
