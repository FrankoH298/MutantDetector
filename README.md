# MutantDetector

### Python

- Versión: 3.12.7
- Documentación: https://docs.python.org/es/3.12/

### Requirements

| Paquete | Version |
|:---|:---:|
| annotated-types | 0.7.0 |
| anyio | 4.6.2.post1 |
| click | 8.1.7 |
| colorama | 0.4.6 |
| coverage | 7.6.4 |
| fastapi | 0.115.4 |
| h11 | 0.14.0 |
| httptools | 0.6.4 |
| idna | 3.10 |
| iniconfig | 2.0.0 |
| packaging | 24.2 |
| pluggy | 1.5.0 |
| pydantic | 2.9.2 |
| pydantic_core | 2.23.4 |
| pytest | 8.3.3 |
| python-dotenv | 1.0.1 |
| PyYAML | 6.0.2 |
| sniffio | 1.3.1 |
| starlette | 0.41.2 |
| typing_extensions | 4.12.2 |
| uvicorn | 0.32.0 |
| watchfiles | 0.24.0 |
| websockets | 14.0 |

### Instructions

#### Manual installation

```shell
git clone https://github.com/FrankoH298/MutantDetector.git ./MutantDetector
cd MutantDetector
pip install -r requirements.txt
```

#### Post-installation execution

To run the application, enter the following in the terminal:

```shell
uvicorn app:app --reload
```