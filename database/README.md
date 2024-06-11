# Run Database with Docker

## Build Image
```bash
docker build -t my-mysql-image .
```

## Run Image
```bash
docker run -d -p "4000:3306" --name my-mysql-container my-mysql-image
```