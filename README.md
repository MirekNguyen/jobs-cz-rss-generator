# Jobs.cz RSS Generator

## Prerequisities

You can run the script in two ways

### 1. Using Docker:

-   Docker installed on your machine
-   docker-compose installed on your machine.

### 2. Using Python with pip

-   Python 3.x installed on your machine.
-   pip installed

## Building and Running with Docker

1. Navigate to the directory containing the Dockerfile.

```
cd <project>/docker
```

2. Run the following command to build the Docker image:

```
docker-compose up -d
```

3. Alternatively, you can build it using Dockerfile

-   Navigate to the root directory of the project

```
cd </project>
```

-   Build

```
docker build -t jobs-rss -f docker/Dockerfile .
```

-   Run

```
docker run -v ./out:/out jobs-rss -o /out/output.xml
```

## Output

Upon successful execution, the generated RSS feed will be available at:

```
<project>/out/output.xml
```
