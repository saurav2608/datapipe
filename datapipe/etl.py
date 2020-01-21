import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
container_name = 'data'
blob_service_client = BlobServiceClient.from_connection_string(connect_str)
source_file_name = 'landing_zone/raw_data.csv'
target_file_name = 'semantic_layer/final_data.csv'

# Create a blob client using the local file name as the name for the blob
blob_downlaod_client = blob_service_client.get_blob_client(container=container_name, blob=source_file_name)


with open("./data.csv", "wb") as my_blob:
    blob_data = blob_downlaod_client.download_blob()
    blob_data.readinto(my_blob)

blob_upload_client = blob_service_client.get_blob_client(container=container_name, blob=target_file_name)
with open('./data.csv', "rb") as data:
    blob_upload_client.upload_blob(data, overwrite=True)