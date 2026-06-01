import unittest
from utils.block_to_block_type import BlockType, block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_paragraph(self):
        positive_cases = [
            "something is happening",
            """
this is the coolest thing in the world 1.

but I also like other stuff too # blessed

- this is going to be the best thing ever

# Heading 1
"""
        ]

        for case in positive_cases:
            self.assertEqual(block_to_block_type(case), BlockType.PARAGRAPH)
        
    
    def test_heading(self):
        positive_cases = [
            "# heading 1",
            "## heading 2",
            "### heading 3",
            "#### heading 4",
            "##### heading 5",
            "###### heading 6"
        ]

        for case in positive_cases:
            self.assertEqual(block_to_block_type(case), BlockType.HEADING)
        
        negative_cases = [
            "######## wrong",
            "#bad"
        ]

        for case in negative_cases:
            self.assertNotEqual(block_to_block_type(case), BlockType.HEADING)
    
    def test_code(self):
        positive_cases = [
            """```
                const myFunction = (a, b) => a+b
            ```""",
            "``` const myFunction = (a, b) => a+b```"
        ]

        for case in positive_cases:
            self.assertEqual(block_to_block_type(case), BlockType.CODE)
        
        negative_cases = [
            """```
                const myFunction = (a, b) => a+b
            """,
            """```
                const myFunction = (a, b) => a+b
            `""",
            """```
                const myFunction = (a, b) => a+b
            ``""",
            """
                const myFunction = (a, b) => a+b
            ```""",
            """`
                const myFunction = (a, b) => a+b
            ```""",
            """``
                const myFunction = (a, b) => a+b
            ```"""
        ]

        for case in negative_cases:
            self.assertNotEqual(block_to_block_type(case), BlockType.CODE)

    def test_quote(self):
        positive_cases = [
"""> This is a quote
>so is this
> and this too"""
        ]

        for case in positive_cases:
            self.assertEqual(block_to_block_type(case), BlockType.QUOTE)
        
        negative_cases = [
""">  This is a quote
>so is this
> and this too
"""
        ]

        for case in negative_cases:
            self.assertNotEqual(block_to_block_type(case), BlockType.QUOTE)
    
    def test_unordered_list(self):
        positive_cases = [
"""- one
- two
- 3
- four"""
        ]

        for case in positive_cases:
            self.assertEqual(block_to_block_type(case), BlockType.UNORDERED_LIST)
        
        negative_cases = [
"""-  one
- two
- 3
- four"""
        ]

        for case in negative_cases:
            self.assertNotEqual(block_to_block_type(case), BlockType.UNORDERED_LIST)
    
    def test_ordered_list(self):
        positive_cases = [
            "1. one",
"""1. one
2. two
3. three
4. four
5. five
6. six
7. seven
8. eight
9. nine
10. ten"""
        ]

        for case in positive_cases:
            self.assertEqual(block_to_block_type(case), BlockType.ORDERED_LIST)
        
        negative_cases = [
"""2. one
3. two
4. three""",
"""1. one
2. two
3. three
5. four""",
"""1. one
2. two
3. three
5. four 4.
5. five
6. six
7. seven
8. eight
9. nine
10. ten"""
        ]

        for case in negative_cases:
            self.assertNotEqual(block_to_block_type(case), BlockType.ORDERED_LIST)
    
    



if __name__ == "__main__":
    unittest.main()