# suggestic-api
API that flattens a nested sequence into a single list of values.


## Clone and initialize the project

    git clone https://github.com/adalcima/suggestic-api.git

## Build and run the Docker image

    cd suggestic-api
    docker build -t suggestic .
    docker run -p 8888:5000 suggestic:latest

## How to use it

1. Use the following endpoint to POST your input in the json format:
    http://127.0.0.1:8888/flatten

    Input:
    {
    "items": [1, 2, [3, 4, [5, 6], 7], 8]
    }
