# bills-comparison-solar
An interactive dataviz to show the comparison of power bills with &amp; without solar, with &amp; without finance.

## Installation

```bash
pipenv install --dev
```

## Run

```bash
pipenv run streamlit run app.py
```

## Contributing

```bash
# Run tests
pipenv run python -m pytest

# Lint (skip string normalisation)
pipenv run black -S .
```