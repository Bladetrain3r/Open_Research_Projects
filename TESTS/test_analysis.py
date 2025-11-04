"""
Tests for analysis.py

This module contains unit tests for the data analysis script.
"""

import unittest
import sys
import os

# Add SCRIPTS directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'SCRIPTS'))

from analysis import load_data, analyze_data, save_results


class TestAnalysis(unittest.TestCase):
    """Test cases for analysis functions."""
    
    def test_load_data(self):
        """Test data loading functionality."""
        # Test with empty filename
        result = load_data("test_file.csv")
        self.assertIsInstance(result, list)
    
    def test_analyze_data(self):
        """Test data analysis functionality."""
        # Test with empty data
        data = []
        results = analyze_data(data)
        
        self.assertIsInstance(results, dict)
        self.assertIn("count", results)
        self.assertIn("mean", results)
        self.assertEqual(results["count"], 0)
    
    def test_analyze_data_with_values(self):
        """Test analysis with sample data."""
        data = [1, 2, 3, 4, 5]
        results = analyze_data(data)
        
        self.assertEqual(results["count"], 5)
        self.assertIsInstance(results["mean"], float)
    
    def test_save_results(self):
        """Test results saving functionality."""
        results = {"count": 10, "mean": 5.0}
        
        # Should not raise an exception
        try:
            save_results(results)
        except Exception as e:
            self.fail(f"save_results raised {type(e).__name__}: {e}")


if __name__ == "__main__":
    unittest.main()
