"""
Tests for simulation.py

This module contains unit tests for the simulation script.
"""

import unittest
import sys
import os

# Add SCRIPTS directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'SCRIPTS'))

from simulation import setup_simulation, run_simulation, analyze_simulation_results


class TestSimulation(unittest.TestCase):
    """Test cases for simulation functions."""
    
    def test_setup_simulation(self):
        """Test simulation setup."""
        params = {"iterations": 100, "seed": 42}
        config = setup_simulation(params)
        
        self.assertIsInstance(config, dict)
        self.assertEqual(config["iterations"], 100)
        self.assertEqual(config["seed"], 42)
    
    def test_setup_simulation_defaults(self):
        """Test simulation setup with default parameters."""
        config = setup_simulation({})
        
        self.assertEqual(config["iterations"], 1000)
        self.assertEqual(config["seed"], 42)
    
    def test_run_simulation(self):
        """Test simulation execution."""
        config = {"iterations": 5, "seed": 42, "variables": {}}
        results = run_simulation(config)
        
        self.assertIsInstance(results, list)
        self.assertGreater(len(results), 0)
    
    def test_analyze_simulation_results(self):
        """Test simulation results analysis."""
        results = [
            {"iteration": 0, "value": 1.0},
            {"iteration": 1, "value": 2.0},
            {"iteration": 2, "value": 3.0}
        ]
        
        summary = analyze_simulation_results(results)
        
        self.assertIsInstance(summary, dict)
        self.assertEqual(summary["total_iterations"], 3)
        self.assertEqual(summary["final_value"], 3.0)
    
    def test_analyze_empty_results(self):
        """Test analysis with empty results."""
        summary = analyze_simulation_results([])
        
        self.assertEqual(summary["total_iterations"], 0)
        self.assertIsNone(summary["final_value"])


if __name__ == "__main__":
    unittest.main()
