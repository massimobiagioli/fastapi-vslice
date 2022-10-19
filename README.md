# FastAPI - Vertical Slice Architecture Example

## Pre-requisites

- Python 3.9
- Poetry 1.2.1
- Docker

## Install dependencies

```
poetry install
```

## Commands

Start docker containers:
```
make up
```

Stop docker containers:
```
make down
```

Start local server
```
make start-local
```

Populate db with fake data
```
make load-fixtures
```

Launch tests
```
make test
```

Launch test with coverage
```
make coverage
```

Launch test with features coverage
```
make coverage-features
```