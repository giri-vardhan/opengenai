import subprocess
from datetime import datetime
import os
from dotenv import load_dotenv

def call_s3_upload(bucket_name, file_key_prefix, local_file_path):
    # Generate filename with prefix and current date
    today_date = datetime.now().strftime("%Y-%m-%d")
    file_key = f"{file_key_prefix}_{today_date}.csv"

    # Call the upload script
    subprocess.run(["python", "uploadFileTos3.py", bucket_name, file_key, local_file_path])

def main():
    # Load environment variables from .env file
    load_dotenv()

    # Set necessary variables
    bucket_name = os.getenv("BUCKET_NAME")
    file_key_prefix = os.getenv("FILE_KEY_PREFIX")
    local_file_path = os.getenv("LOCAL_FILE_PATH")

    # Call the function with the set variables
    call_s3_upload(bucket_name, file_key_prefix, local_file_path)

if __name__ == "__main__":
    main()


# run -> python callS3Upload.py