# Data Directory

This directory stores research data used in the project.

## Structure

- **raw/**: Original, unprocessed data
  - Store data exactly as collected
  - Do not modify files in this directory
  - Include metadata about data sources

- **processed/**: Cleaned and preprocessed data
  - Store processed, analysis-ready data
  - Document preprocessing steps
  - Include version information

## Data Management

### Best Practices

1. **Raw Data**: Keep original data immutable
2. **Processed Data**: Document all transformations
3. **File Naming**: Use descriptive, consistent names
4. **Formats**: Prefer open formats (CSV, JSON) over proprietary ones
5. **Documentation**: Include data dictionaries and metadata

### Large Files

For large datasets:
- Consider using Git LFS (Large File Storage)
- Or store externally and document access procedures
- Update .gitignore if files shouldn't be tracked

## Privacy and Ethics

- Ensure data collection follows ethical guidelines
- Remove or anonymize sensitive information
- Respect privacy and confidentiality requirements
- Document data usage permissions
