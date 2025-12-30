# Contributing Guide

Thank you for your interest in contributing to this project! 🎉

We welcome all kinds of contributions, including bug reports, feature requests, documentation improvements, and code contributions.

Please read this guide carefully to ensure a smooth and consistent collaboration process.


## Code of Conduct

By participating in this project, you agree to maintain a respectful and professional environment. Harassment, discrimination, and abusive behavior will not be tolerated.


## Branching Strategy

We follow a simple branching model:

* main → production-ready code

* develop → integration branch

* feature/<short-description> → new features

* fix/<short-description> → bug fixes

* chore/<short-description> → maintenance tasks

* docs/<short-description> → all documentation

#### Example:

```bash
feature/user-authentication
fix/token-expiration
```

## Commit Message Convention

We use Conventional Commits to keep a clear consistent commit history.

### Format
```bash
<type>(optional scope): <short description>
```

### Common Types

* **feat:** A new feature
* **fix:** A bug fix
* **docs:** Documentation only change 
* **style:** Code style changes (fommatting, missins semicolons, etc)
* **refactor:** Code changes that neither fix a bug nor add a feature
* **test:** Adding or updating tests
* **chore:** Maintenance tasks

#### Example
```bash
feat(auth): Add JWT authentication
fix(users): Handle null email case
docs: Update API documentation
```

## Pull Request Guidelines
Before submitting a Pull Request, please ensure

- Your branch is up to date with dev.
- All tests pass successfully.
- Code follows the project standars.

### Pull Request Rules
- PR title must follow Conventional Commits format.
- PR description must clearly explain what and why
- Reference related issues when applicable
- Keep PRs small and focused.

#### Example PR title
```bash
feat(auth): #<issues>(optional) implement permission system
```

## Reporting Issues
When reporting an issue, please include:
- Clear and descriptive title
- Steps to reproduce
- Expected behavior
- Actual behavior
- Screenshots or logs (if applicable)

## Final notes
Thank you for helping improve this project! 🚀

If you have any questions, feel free to open an issue or start a discussion.
