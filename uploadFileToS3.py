import argparse
import boto3
import os
from dotenv import load_dotenv

def upload_to_s3(bucket_name, file_key, local_file_path):
    # Load environment variables from .env file
    load_dotenv()

    # Access AWS credentials from environment variables
    aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")

    # Create an S3 client using the credentials
    s3 = boto3.client(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )

    try:
        # Upload the file to S3
        s3.upload_file(local_file_path, bucket_name, file_key)
        print("File uploaded successfully to S3 bucket.")
    except Exception as e:
        print(f"Error uploading file to S3: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upload file to S3")
    parser.add_argument("bucket", help="S3 bucket name")
    parser.add_argument("file_key", help="S3 file key (path)")
    parser.add_argument("file_path", help="Local file path")
    args = parser.parse_args()

    upload_to_s3(args.bucket, args.file_key, args.file_path)


# run -> python uploadFileTos3.py <bucket-name> <file-key> <local-file-path>

