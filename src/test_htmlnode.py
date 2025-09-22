import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        a = HTMLNode("div", "this is div", [], { "class": "bg-n-000", "width": "20" })
        self.assertEqual(a.props_to_html(), 'class="bg-n-000" width="20"')



if __name__ == "__name__":
    unittest.main()
