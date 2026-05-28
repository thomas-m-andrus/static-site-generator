import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def setUp(self):
        node_1 = HTMLNode('p','hello world', None, {})
        node_2 = HTMLNode('li', None, [node_1], { "id": 'unique', "something": "random"})
        node_3 = HTMLNode('ul', None, [node_2], None)
        return [node_1, node_2, node_3]

    def test_repr(self):
        _, _, node_3 = self.setUp()
        self.assertEqual(repr(node_3), "tag: ul, value: None, children: [tag: li, value: None, children: [tag: p, value: hello world, children: None, props: {}], props: {'id': 'unique', 'something': 'random'}], props: None")
    
    def test_to_html(self):
        node_1,_,_ = self.setUp()
        with self.assertRaises(NotImplementedError):
            node_1.to_html()
    
    def test_props_to_html(self):
        n1, n2, n3 = self.setUp()
        self.assertEqual(n1.props_to_html(), '')
        self.assertEqual(n2.props_to_html(), " id=\"unique\" something=\"random\"")
        self.assertEqual(n3.props_to_html(), '')
    

if __name__ == "__main__":
    unittest.main()