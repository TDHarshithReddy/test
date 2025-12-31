# Contributing to Dental Mobile Application

Thank you for your interest in contributing to the Dental Mobile Application! This document provides guidelines for contributing to the project.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/your-username/dental-mobile-app.git`
3. Create a new branch: `git checkout -b feature/your-feature-name`
4. Make your changes
5. Test your changes thoroughly
6. Commit your changes: `git commit -m "Add your feature"`
7. Push to your fork: `git push origin feature/your-feature-name`
8. Open a Pull Request

## Development Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

## Code Style

- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings to classes and functions
- Keep functions small and focused
- Comment complex logic

## Testing

Before submitting a PR, please ensure:

1. The application runs without errors
2. All existing features still work
3. New features are properly integrated
4. Code passes syntax checks: `python -m py_compile main.py`

## Feature Requests

We welcome feature requests! Please open an issue with:

- Clear description of the feature
- Use case and benefits
- Any implementation ideas

## Bug Reports

When reporting bugs, please include:

- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Python version
- Operating system
- Error messages or screenshots

## Pull Request Guidelines

- **One feature per PR** - Keep PRs focused on a single feature or bug fix
- **Update documentation** - Update README.md if adding new features
- **Test thoroughly** - Ensure your changes work on desktop and mobile
- **Follow existing code style** - Match the existing code structure
- **Write clear commit messages** - Use descriptive commit messages

## Areas for Contribution

Here are some areas where we'd love contributions:

### High Priority
- Unit tests and integration tests
- Input validation and error handling
- Search and filter functionality for patients
- Export data to CSV/PDF
- Appointment reminders

### Medium Priority
- Dark mode support
- Multi-language support
- Custom themes and colors
- Image storage for X-rays
- Backup and restore functionality

### Low Priority
- Cloud synchronization
- Multi-user support
- Advanced analytics
- Integration with external systems
- Mobile-specific optimizations

## Code Review Process

1. A maintainer will review your PR within 3-5 business days
2. You may be asked to make changes
3. Once approved, your PR will be merged
4. Your contribution will be credited in the release notes

## Questions?

Feel free to open an issue with your question, or reach out to the maintainers.

## License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to making dental practice management easier! 🦷
