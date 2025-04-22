# bills-comparison-solar
An interactive dataviz to show the comparison of power bills with &amp; without solar
# household-model

Estimates a household's emissions and cost savings from electrification. Please refer to [METHODOLOGY.md](METHODOLOGY.md) for how we calculate this.

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
pipenv run black -S . --exclude src/openapi_client
```