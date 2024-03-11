FROM python:3.8

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx

# Install Python dependencies
COPY requirements.txt /app/
COPY qdrant_creation.sh /app/

WORKDIR /app
RUN pip install --upgrade pip 
    # && pip install wheel setuptools pip --upgrade \

# RUN chmod +x qdrant_creation.sh
# RUN ./qdrant_creation.sh

# RUN pip install -r requirements.txt

RUN pip install fastapi && pip install qdrant-client && pip install sentence-transformers && pip install langchain && pip install langchain-community

RUN python3 /app/data_loader.py 
ENTRYPOINT python3 /app/main.py