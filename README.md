# Starting With Docker
 
## Run manually
```bash
python -m uvicorn main:app --reload
```

## Docker build
```bash
docker build -t my-fast-api-image .
```

## Docker run
```bash
docker run -p "8000:8000" --name
my-fast-api-container my-fast-api-image
```