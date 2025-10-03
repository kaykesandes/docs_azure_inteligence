import os
from azure.storage.blob import BlobServiceClient
import streamlit as st
from ultils.Config import Config

def upload_blob(file, file_name):
  try:
    blob_service_client = BlobServiceClient.from_connection_string(Config.CARTOES_CONNECTION_STRING)
    blob_client = blob_service_client.get_blob_client(container=Config.CONTAINER_NAME, blob=file_name)
    blob_client.upload_blob(file, overwrite=True)
    
    return blob_client.url
  except Exception as e:
    st.error(f"Error {str(e)}")
    return None
