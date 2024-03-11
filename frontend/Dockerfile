FROM python:3.8
USER root
ENV PYTHONUNBUFFERED=TRUE
COPY . /app
WORKDIR /app
RUN apt-get update
RUN pip install --upgrade pip
RUN apt install -y libgl1-mesa-glx
RUN pip install wheel setuptools pip --upgrade
RUN pip install -r requirements.txt
ENTRYPOINT streamlit run streamlit_app.py 