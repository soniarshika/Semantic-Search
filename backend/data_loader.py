import json
from pathlib import Path
from typing import List, Optional, Union
from langchain.docstore.document import Document
from langchain.document_loaders.base import BaseLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Qdrant
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class JSONLoader(BaseLoader):
    def __init__(self, file_path: Union[str, Path], content_key: Optional[str] = None):
        self.file_path = Path(file_path).resolve()
        self._content_key = content_key

    def load(self) -> List[Document]:
        """Load and return documents from the JSON file."""
        docs = []

        # Load JSON file
        with open(self.file_path) as file:
            data = json.load(file)

            # Extract relevant information from the JSON
            patent_number = data.get("patent_number", "")
            titles = data.get("titles", [])
            abstracts = data.get("abstracts", [])
            claims = data.get("claims", [])
            descriptions = data.get("descriptions", [])
            inventors = data.get("inventors", [])
            assignees = data.get("assignees", [])
            ipc_classes = data.get("ipc_classes", [])
            legal_status = data.get("legal_status", "")
            priority_date = data.get("priority_date", "")
            application_date = data.get("application_date", "")
            publication_date = data.get("publication_date", "")
            family_members = data.get("family_members", [])

            # Combine text from titles, abstracts, claims, and descriptions
            page_content = " ".join([
                title.get("text", "") for title in titles
            ] + [
                abstract.get("paragraph_markup", "") for abstract in abstracts
            ] + [
                claim.get("paragraph_markup", "") if claim and claim else "" for claim in claims
            ] + [
                description.get("paragraph_markup", "") for description in descriptions
            ])

            # Create a Document instance for the loaded data
            metadata = dict(
                patent_number=patent_number,
                inventors=inventors,
                assignees=assignees,
                ipc_classes=ipc_classes,
                legal_status=legal_status,
                priority_date=priority_date,
                application_date=application_date,
                publication_date=publication_date,
                family_members=family_members,
            )
            docs.append(Document(page_content=page_content, metadata=metadata))

        return docs

# Path to the folder containing JSON files
folder_path = 'data/patent_jsons'


all_docs = []


for filename in os.listdir(folder_path):
    if filename.endswith(".json"):
        file_path = os.path.join(folder_path, filename)

        # Load documents using JSONLoader
        logger.info(f"Loading documents from file: {file_path}")
        loader = JSONLoader(file_path=file_path)
        docs = loader.load()

        # Extend the list of all_docs with the loaded documents
        all_docs.extend(docs)

# HuggingFace Embeddings
EMBEDDINGS_MODEL_NAME = 'sentence-transformers/all-MiniLM-L6-v2'
logger.info(f"Initializing HuggingFace Embeddings with model: {EMBEDDINGS_MODEL_NAME}")
embeddings = HuggingFaceEmbeddings(model_name=EMBEDDINGS_MODEL_NAME)

# Connecting to the Quadrant
url = "http://0.0.0.0:6333"
logger.info(f"Connecting to Qdrant at URL: {url}")
qdrant = Qdrant.from_documents(
    all_docs,
    embeddings,
    url=url,
    collection_name="patent_index",
    force_recreate=True
)

logger.info("Data loading: Process completed successfully.")