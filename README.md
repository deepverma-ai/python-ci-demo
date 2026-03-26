# python-ci-demo

A demonstration Python project showing a CI pipeline with CircleCI, GitHub branch
protection rules, and automated quality gates.

## Tech Stack

- **Language**: Python 3.14
- **Linter**: flake8
- **Testing**: pytest + pytest-cov
- **CI**: CircleCI

## Local Setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
```

### Run the linter

```bash
flake8 src/ tests/
```

### Run the tests

```bash
pytest
```

## CI Pipeline

Every push (PR or `master`) triggers two CircleCI jobs:

| Job | Tool | What it checks |
|-----|------|----------------|
| `lint` | flake8 | PEP-8 style, unused imports, undefined names |
| `test` | pytest | All unit tests + code coverage report |

`test` only runs after `lint` passes (fan-out with dependency).

## Branch Protection (GitHub)

Configure these rules on `master` under **Settings → Branches**:

1. **Require status checks to pass** – add `lint` and `test` as required checks.
2. **Require pull request reviews** – set minimum approvals to **1**.
3. **Require linear history** – enforces squash-or-rebase merging.
4. **Include administrators** – applies rules to repo owners too (recommended).

## Project Structure

```
.
├── .circleci/
│   └── config.yml          # CircleCI pipeline definition
├── src/
│   ├── calculator.py       # Basic arithmetic operations
│   └── list_utils.py       # List manipulation utilities
├── tests/
│   ├── test_calculator.py
│   └── test_list_utils.py
├── .flake8                 # Linter configuration
├── .gitignore              # Git ignore rules
├── CI_Pipeline_Documentation.pdf # Comprehensive pipeline documentation
├── requirements.txt        # Runtime dependencies
├── requirements-dev.txt    # Dev/CI dependencies
└── setup.cfg               # pytest configuration
```

