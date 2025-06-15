FROM python:3.11-slim
LABEL maintainer="Dhiraj Patra <dhiraj.patra@gmail.com>"
LABEL description="Docker image for Kubeflow model serving with scikit-learn"

WORKDIR /app
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python"]
