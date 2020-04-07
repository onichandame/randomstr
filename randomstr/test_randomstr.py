from unittest import TestCase

from .randomstr import randomstr as subject

class TestRandomStr(TestCase):

    def test_default(self):
        self.assertEqual(len(subject()), 10)
        self.assertRegex(subject(), '[a-zA-Z0-9]')

    def test_length(self):
        self.assertEqual(len(subject(length=100)), 100)

    def test_readable(self):
        self.assertNotRegex(subject(readable=True, length=100), '[0Oil]')

    def test_capitalization(self):
        self.assertNotRegex(subject(capitalization=True, length=100), '[a-z]')

    def test_charset(self):
        # alphanumeric
        self.assertRegex(subject(charset='alphanumeric', length=100), '[A-Za-z0-9]')

        # alphabetic
        self.assertRegex(subject(charset='alphabetic', length=100), '[A-Za-z]')
        self.assertNotRegex(subject(charset='alphabetic', length=100), '[0-9]')

        # numeric
        self.assertRegex(subject(charset='numeric', length=100), '[0-9]')
        self.assertNotRegex(subject(charset='numeric', length=100), '[a-zA-Z]')

        # hex
        self.assertRegex(subject(charset='hex', length=100), '[0-9a-f]')
        self.assertNotRegex(subject(charset='hex', length=100), '[g-zA-Z]')

        # custom
        self.assertRegex(subject(charset='!@#$%$', length=100), '[!@#$%$]')
        self.assertNotRegex(subject(charset='!@#$%$', length=100), '[0-9a-zA-Z]')
