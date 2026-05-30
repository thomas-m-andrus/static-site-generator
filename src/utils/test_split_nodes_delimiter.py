import unittest
from utils.split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ])
    
    def test_not_text(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        node_2 = TextNode("something `something`", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node_2,node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            node_2,
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ])
    
    def test_no_pattern(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [TextNode("This is text with a `code block` word", TextType.TEXT, None)])
    
    def test_bad_pattern(self):
        node = TextNode("This is text with a `code block word", TextType.TEXT)
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(str(context.exception), "Incorrect markdown syntax: 'This is text with a `code block word'")
    
    def test_start_and_end(self):
        node = TextNode("**start** and **middle** and **end**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("start",TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("middle",TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("end",TextType.BOLD),
        ])



if __name__ == "__main__":
    unittest.main()