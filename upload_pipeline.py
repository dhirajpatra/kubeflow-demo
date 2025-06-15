# upload_pipeline.py
from kfp import Client

client = Client()  # Optionally: Client(host="http://localhost:8080")
client.upload_pipeline(
    pipeline_package_path="kfp_pipeline.yaml",
    pipeline_name="iris-classifier-pipeline"
)
