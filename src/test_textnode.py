import unittest
from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_un_eq(self):
        node = TextNode("This is a text node, one different", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_different_text_type(self):
        node = TextNode("This is a text node", TextType.CODE)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_cases(self):
        text = "TEST_TEXT"
        url = "www.fake.come"
        pureTextCases = [
            [TextType.BOLD, '<b>TEST_TEXT</b>'],
            [TextType.ITALIC, '<i>TEST_TEXT</i>'],
            [TextType.CODE, '<code>TEST_TEXT</code>']
        ]
        for case in pureTextCases:
            type, expected= case
            node = TextNode(text, type)
            html_node = text_node_to_html_node(node)
            self.assertEqual(html_node.to_html(), expected)
        linkedCases = [
            [TextType.LINK, "tag: a, value: TEST_TEXT, props: {'href': 'www.fake.come'}"],
            [TextType.IMAGE, "tag: img, value: , props: {'src': 'www.fake.come', 'alt': 'TEST_TEXT'}"]
        ]

        for [type, expected] in linkedCases:
            node = TextNode(text, type, url)
            html_node = text_node_to_html_node(node)
            self.assertEqual(repr(html_node), expected)

        with self.assertRaises(Exception):
            node = TextNode(text, "RANDOM")
            html_node = text_node_to_html_node(node)


if __name__ == "__main__":
    unittest.main()