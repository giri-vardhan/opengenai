import subprocess
from datetime import datetime

def call_s3_upload(bucket_name, file_key_prefix, local_file_path):
    # Generate filename with prefix and current date
    today_date = datetime.now().strftime("%Y-%m-%d")
    file_key = f"{file_key_prefix}_{today_date}.csv"

    # Call the upload script
    subprocess.run(["python", "uploadFileTos3.py", bucket_name, file_key, local_file_path])

def main():
    # Set necessary variables
    bucket_name = "opengenai"
    file_key_prefix = "forecast"
    local_file_path = "/Users/sai.giri/Documents/work/opengenai/Store/forecast.csv"

    # Call the function with the set variables
    call_s3_upload(bucket_name, file_key_prefix, local_file_path)

if __name__ == "__main__":
    main()


# run -> python callS3Upload.py