import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node2normal = TextNode("This is a text node", TextType.TEXT)
        node3normal = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)
        self.assertEqual(node2normal, node3normal)
        self.assertNotEqual(node, node2normal)


if __name__ == "__name__":
    unittest.main()
