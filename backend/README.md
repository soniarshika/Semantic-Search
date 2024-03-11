# Text similarity between two documents

## Objective
This repository contains the code and configurations for setting up a Semantic Search System. The system utilizes FastAPI for creating a REST API endpoint, Qdrant for vector search, Sentence Transformers for sentence embeddings, and Langchain for document loading and processing.

## Introduction
This Semantic Search project is designed to facilitate efficient document retrieval based on semantic similarity. It leverages cutting-edge technologies such as FastAPI for REST API development, Qdrant for vector search, Sentence Transformers for generating semantic embeddings, and Langchain for document loading and processing.

## Components

#### FastAPI:

FastAPI is a modern, fast, and web framework for building APIs with Python 3.7+ based on standard Python type hints. The provided FastAPI application exposes a single API endpoint for semantic search.


#### Qdrant:

Qdrant is an open-source vector search engine that provides fast and efficient search capabilities for high-dimensional vectors.The Qdrant server is utilized to index and search vectors, enabling semantic similarity search.


#### Sentence Transformers:

Sentence Transformers is a Python library for transforming sentences into semantic embeddings.
It employs pre-trained models to generate vector representations that capture the semantic meaning of input sentences.


#### Langchain:

Langchain is a library for document processing in Python. It offers tools for loading and processing documents, making it easier to integrate diverse document data into the search system.


## Prerequisites
- Python 3.8 or later
- Docker (for Qdrant server)


## Directory Structure

src/: Contains the source code for the FastAPI application.
data/patent_jsons/: Folder with sample JSON files containing patent data.
Dockerfile: Used for building the application Docker image.
requirements.txt: Lists the Python dependencies for the project.


## Setup

1.**Clone the Repository**: Clone this repository to your local machine:

```
git clone https://github.com/soniarshika/Semantic-Search.git
cd Semantic-Search\
```

2.**Install Dependencies**: Create a virtual environment and Install the required dependencies using pip:

```
python3 -m venv venv
source venv/bin/activate
pip3 install -r frontend/requirements.txt
pip3 install -r backend/requirements.txt
```

3. **Run qdrant server**: Run Qdrant Server using:

```
docker pull qdrant/qdrant
docker run -p 6333:6333 qdrant/qdrant
```

4. **Load data using:**

```python3 backend/data_loader.py```


4. **Start the server**: To start the server for the model you can run:

```python3 backend/main.py```

and in new terminal start frontend server using streamlt UI:

```streamlit run streamlit_app.py```


### Input
The  input of this module the query from the user. Now to send request to the server you can use:

```
curl -X GET "http://0.0.0.0:8000/api/search" -G --data-urlencode "query=What is the proposed solution for reducing a pipeline stall caused by a data hazard in a superscalar system, and how does it aim to improve processing speed?" -H "Accept: application/json"
```



## Containerising this code

To ensure the consistency between different environments we should encapsulate our application using Docker. Docker containers can be easily packaged, shipped, and deployed across different environments. Containers share the host system's kernel, which reduces the overhead of running multiple instances of an operating system. Docker facilitates a streamlined CI/CD pipeline. With containers, you can build, test, and deploy applications consistently and automatically. 

1. If you want to run this in a docker container, the docker compose file is already made for this purpose. You can just build the image and run the container using:

```
sudo docker-compose up 
```


**NOTE: There were some issues with my open ai api access. So used sentence transformers here. But can be replaced with open ai keys with a bit code modifications.**