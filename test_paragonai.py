# test_paragonai.py
"""
Tests for ParagonAI module.
"""

import unittest
from paragonai import ParagonAI

class TestParagonAI(unittest.TestCase):
    """Test cases for ParagonAI class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ParagonAI()
        self.assertIsInstance(instance, ParagonAI)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ParagonAI()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
