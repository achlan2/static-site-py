import unittest
from extract import extract_title

class TestExtract(unittest.TestCase):
    def test_extract_header(self):
        title = extract_title("""
# ELU KOCAK
""")
        self.assertEqual(title, "ELU KOCAK")

