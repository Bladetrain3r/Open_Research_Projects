# Contributing to Open Research Projects

Thank you for your interest in contributing to this research project! This document provides guidelines for contributing.

## Getting Started

1. **Fork the Repository**: Create your own fork of the project
2. **Clone Your Fork**: Clone the repository to your local machine
3. **Create a Branch**: Create a branch for your specific task or experiment
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Contribution Workflow

### 1. Make Your Changes

- Work on your specific research task or analysis
- Keep changes focused and related to a single objective
- Write clear, documented code
- Add tests for new functionality

### 2. Commit Your Changes

Use descriptive commit messages that explain what and why:

```bash
git commit -m "Added data collection script for experiment X"
```

Good commit message examples:
- "Implemented statistical analysis for hypothesis testing"
- "Added visualization for result set Y"
- "Fixed bug in data preprocessing function"

### 3. Write Tests

- Add tests in the `TESTS/` directory
- Ensure all tests pass before submitting
- Aim for good test coverage of new code

### 4. Update Documentation

- Update relevant documentation in `DOCS/`
- Add docstrings to functions and classes
- Update README if adding new features

### 5. Submit a Pull Request

- Push your branch to your fork
- Create a pull request to the main repository
- Provide a clear description of your changes
- Reference any related issues

## Code Standards

### Python Code Style

- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions focused and modular

### Documentation

- Use Markdown for documentation files
- Keep language clear and concise
- Include examples where helpful

## Directory Structure

Organize your contributions according to this structure:

- `DOCS/`: Research documentation and methodology
- `DATA/raw/`: Raw, unprocessed data
- `DATA/processed/`: Cleaned and processed data
- `SCRIPTS/`: Analysis and simulation scripts
- `RESULTS/figures/`: Generated plots and visualizations
- `RESULTS/tables/`: Result tables and summaries
- `TESTS/`: Unit tests and integration tests

## Peer Review Process

1. **Submit Pull Request**: Create PR with clear description
2. **Automated Checks**: Ensure tests pass
3. **Peer Review**: Other researchers review your code
4. **Address Feedback**: Make requested changes
5. **Approval**: Once approved, changes will be merged

## Research Ethics

- Ensure all data sources are properly cited
- Respect privacy and confidentiality requirements
- Follow ethical guidelines for your research domain
- Be transparent about methodology and limitations

## Questions or Issues?

- Open an issue for bugs or feature requests
- Use discussions for questions and ideas
- Tag maintainers for urgent matters

## License

By contributing, you agree that your contributions will be licensed under the same license as the project (see LICENSE file).

---

Thank you for contributing to open, collaborative research!
