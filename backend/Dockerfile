FROM python:3.8

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx

# Install Python dependencies
COPY . /app/

WORKDIR /app
RUN pip install --upgrade pip 

RUN pip install fastapi && pip install qdrant-client && pip install sentence-transformers && pip install langchain && pip install langchain-community


RUN python3 /app/data_loader.py 
ENTRYPOINT python3 /app/main.py