#
# SPDX-FileCopyrightText: Copyright 2022 Arm Limited and/or its affiliates <open-source-office@arm.com>
# SPDX-License-Identifier: MIT
#

"""A module for testing our Flask server by checking if it is returning 200 status code"""
import unittest
from app import App


class Tests(unittest.TestCase):
    """Basic tests for the application"""
    def setUp(self):
        self.app = App.test_client()

    def test_200(self):
        """test_200: a request for / shall return 200 OK"""
        res = self.app.get('/')
        assert res.status == '200 OK'

    def test_404(self):
        """test_404: a request for null shall return 404 NOT FOUND"""
        res = self.app.get('/null')
        assert res.status == '404 NOT FOUND'

if __name__ == "__main__":
    unittest.main()
