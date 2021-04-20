from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os
import io
import numpy as np
import pandas as pd
from glob import glob
from PIL import Image
from sklearn.model_selection import train_test_split

from dotenv import load_dotenv
load_dotenv()

load_dotenv(verbose=True)

from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

STORAGEACCOUNTNAME = os.getenv('STORAGEACCOUNTNAME')
STORAGEACCOUNTKEY = os.getenv('STORAGEACCOUNTKEY')
CONTAINERNAME = os.getenv('CONTAINERNAME')

CSV_LOCAL_FILE_NAME = 'local_data_file.csv'
CSV_FILE_BLOB_NAME = 'Covid-19-1/data_file.csv'
IMG_DIR_BLOB_NAME = 'Covid-19-1/images'

def initialize_directory(name):
    if not os.path.exists(name):
        os.mkdir(name)
    else:
        files = glob(f'{name}/*')
        for f in files:
            try:
                os.remove(f)
            except OSError as e:
                print('Exception: %s : %s' % (f, e.strerror))
    print(f'\'{name}\' initialized')

TRAIN_DIR = 'train'
TEST_DIR = 'test'

initialize_directory(TRAIN_DIR)
initialize_directory(TEST_DIR)

POSITIVE_DIR = 'positive'
NEGATIVE_DIR = 'negative'

TRAIN_POS = f'./{TRAIN_DIR}/{POSITIVE_DIR}'
TRAIN_NEG = f'./{TRAIN_DIR}/{NEGATIVE_DIR}'

initialize_directory(TRAIN_POS)
initialize_directory(TRAIN_NEG)

TEST_POS = f'./{TEST_DIR}/{POSITIVE_DIR}'
TEST_NEG = f'./{TEST_DIR}/{NEGATIVE_DIR}'

initialize_directory(TEST_POS)
initialize_directory(TEST_NEG)

container_name = os.getenv('CONTAINERNAME')
connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')

try:
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    container_client = blob_service_client.get_container_client(container_name)

    csv_blob_client = blob_service_client.get_blob_client(container=container_name, blob=CSV_FILE_BLOB_NAME)

    with open(CSV_LOCAL_FILE_NAME, "wb") as download_csv:
        download_csv.write(csv_blob_client.download_blob().readall())
    
    # Original csv dataframe
    csv_df = pd.read_csv(CSV_LOCAL_FILE_NAME)

    X = csv_df.iloc[:, :-1].values
    y = csv_df.iloc[:, -1].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

    img_blob_list = container_client.list_blobs(name_starts_with='Covid-19-1/images/')

    for i in range(X_train.shape[0]):
        curr_img_name = X_train[i, 0]
        diagnosis = y_train[i]
        
        dst_path = TRAIN_POS if diagnosis == 'positive' else TRAIN_NEG

        print(f'{i}: Writing \'{curr_img_name}\' as {diagnosis} on the path: \'{dst_path}\'')

        img_blob_client = container_client.get_blob_client(blob=f'Covid-19-1/images/{curr_img_name}')
        
        with open(f'{dst_path}/{curr_img_name}', 'wb') as img_file:
            img_file.write(img_blob_client.download_blob().readall())
    
    print('\nCompleted training set\n')
        
    for i in range(X_test.shape[0]):
        curr_img_name = X_test[i, 0]
        diagnosis = y_test[i]
        
        dst_path = TEST_POS if diagnosis == 'positive' else TEST_NEG

        print(f'{i}: Writing \'{curr_img_name}\' as {diagnosis} on the path: \'{dst_path}\'')

        img_blob_client = container_client.get_blob_client(blob=f'Covid-19-1/images/{curr_img_name}')
        
        with open(f'{dst_path}/{curr_img_name}', 'wb') as img_file:
            img_file.write(img_blob_client.download_blob().readall())
    
    print('\nCompleted test set\n')

except Exception as ex:
    print('Exception:', ex)