import unittest
from utils.extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        input = "# A Long Title With Lots Of Text        \n## SubTitle\n\nHere is where my content starts."
        result = extract_title(input)
        self.assertEqual(result, "A Long Title With Lots Of Text")
    
    def test_failure(self):
        input = "\n## SubTitle\n\nHere is where my content starts."
        with self.assertRaises(ValueError) as context:
            extract_title(input)
        self.assertEqual(str(context.exception), "Markdown missing title")

if __name__ == "__main__":
    unittest.main()