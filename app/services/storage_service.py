import boto3
import os

class StorageService:
    
    def __init__(self):
        self.client = boto3.client(
            "s3",
            endpoint_url=os.getenv("MINIO_URL"),
            aws_access_key_id=os.getenv("MINIO_USER"),
            aws_secret_access_key=os.getenv("MINIO_PASSWORD")
        )
    
    def upload_file(self, file, filename: str) -> str:
        self.client.upload_fileobj(file, "documents", filename)
        return filename
    
    def get_file_url(self, filename: str) -> str:
        return self.client.generate_presigned_url(
            "get_object",
            Params={"Bucket": "documents", "Key": filename},
            ExpiresIn=900  
        )