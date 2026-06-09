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