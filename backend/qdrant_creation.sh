#!/bin/bash

# Pull the Qdrant Docker image
docker pull qdrant/qdrant

# Run the Qdrant Docker container
docker run -p 6333:6333 qdrant/qdrant
