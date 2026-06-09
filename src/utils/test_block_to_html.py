import unittest
from utils.block_to_html import create_block_node, markdown_to_html_node

class TestBlockToHtml(unittest.TestCase):
    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_create_block_node(self):
        cases = [
            [
                "This is another paragraph with _italic_ text and `code` here",
                "<p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p>"
            ],
            [
"""- one
- two
- three
- four
- five
- **six**""",
                "<ul><li>one</li><li>two</li><li>three</li><li>four</li><li>five</li><li><b>six</b></li></ul>"
            ],
                        [
"""1. one
2. two
3. three
4. four
5. five
6. **six**""",
                "<ol><li>one</li><li>two</li><li>three</li><li>four</li><li>five</li><li><b>six</b></li></ol>"
            ],
            [
                "# title",
                "<h1>title</h1>"
            ],
            [
                "## title",
                "<h2>title</h2>"
            ],
                        [
                "### title",
                "<h3>title</h3>"
            ],
                        [
                "#### title",
                "<h4>title</h4>"
            ],
                        [
                "##### title",
                "<h5>title</h5>"
            ],
                        [
                "###### title",
                "<h6>title</h6>"
            ],
            [
                "####### title",
                "<p>####### title</p>"
            ],
            [
"""> "I am in fact a Hobbit in all but size."
>
> -- J.R.R. Tolkien>""",
"<blockquote>\"I am in fact a Hobbit in all but size.\" -- J.R.R. Tolkien></blockquote>"
            ]
            
        ]
        for case,expected in cases:
            result = create_block_node(case)
            self.assertEqual(result.to_html(),expected)


if __name__ == "__main__":
    unittest.main()