import unittest
import os

class TestIndexHTML(unittest.TestCase):
    def test_adr_138_text_present(self):
        path = os.path.join(os.path.dirname(__file__), "index.html")
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("ADR-138 governed delivery verified", content)

if __name__ == "__main__":
    unittest.main()
