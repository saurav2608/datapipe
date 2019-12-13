# Read the wine-quality csv file from the URL
import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

csv_url =\
    'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'

connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
container_name = 'data'
blob_service_client = BlobServiceClient.from_connection_string(connect_str)
local_file_name='landing_zone/raw_data.csv'
# Create a blob client using the local file name as the name for the blob
blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)
blob_client.upload_blob(csv_url, overwrite=True)