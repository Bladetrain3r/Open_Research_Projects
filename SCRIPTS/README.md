# Scripts Directory

This directory contains code for data collection, analysis, and simulations.

## Current Scripts

- **data_collection.py**: Scripts for collecting research data
- **analysis.py**: Data analysis and statistical procedures
- **simulation.py**: Simulation and modeling scripts

## Guidelines

### Writing Scripts

1. **Documentation**: Add docstrings to all functions and classes
2. **Modularity**: Keep functions focused and reusable
3. **Error Handling**: Include appropriate error handling
4. **Testing**: Write tests for all scripts (see TESTS/)

### Code Style

- Follow PEP 8 for Python code
- Use meaningful variable names
- Add comments for complex logic
- Keep code DRY (Don't Repeat Yourself)

### Dependencies

If your script requires external packages:
1. Document dependencies in requirements.txt
2. Use virtual environments for development
3. Pin version numbers for reproducibility

## Running Scripts

Example usage:

```bash
# Data collection
python SCRIPTS/data_collection.py

# Analysis
python SCRIPTS/analysis.py

# Simulation
python SCRIPTS/simulation.py
```

## Adding New Scripts

When adding new analysis or simulation scripts:
1. Place them in this directory
2. Follow existing naming conventions
3. Add corresponding tests in TESTS/
4. Update this README with script descriptions
