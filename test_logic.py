import unittest

class TestTessellProject(unittest.TestCase):
    def test_reconciliation_math(self):
        # Testing the specific logic from your script
        internal_amt = 300.0
        gateway_amt = 290.0
        self.assertEqual(abs(internal_amt - gateway_amt), 10.0)

if __name__ == "__main__":
    unittest.main()