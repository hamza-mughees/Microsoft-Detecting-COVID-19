from azure.storage.blob import BlockBlobService
import numpy as np
import pandas as pd
import time
from PIL import Image

STORAGEACCOUNTNAME= 'covid19detecti4594663496'
STORAGEACCOUNTKEY=''
CONTAINERNAME= 'sourcedata'
CSV_LOCAL_FILE_NAME= 'local_data_file.csv'
CSV_FILE_BLOB_NAME= 'Covid-19-1/data_file.csv'
IMG_DIR_BLOB_NAME = 'Covid-19-1/images'

csv_blob = BlockBlobService(account_name=STORAGEACCOUNTNAME, account_key=STORAGEACCOUNTKEY)
csv_blob.get_blob_to_path(CONTAINERNAME, CSV_FILE_BLOB_NAME, CSV_LOCAL_FILE_NAME)

img_blob = BlockBlobService(account_name=STORAGEACCOUNTNAME, account_key=STORAGEACCOUNTKEY)

# Original csv dataframe
csv_df = pd.read_csv(CSV_LOCAL_FILE_NAME)

def pixels_from_path(file_path, new_size):   #returns matrix of pixel RGB values
    img = Image.open(file_path)
    img = img.convert('L')
    img = img.resize(new_size)
    np_img = np.array(img)
    return np_img

for i in range(335, csv_df.shape[0]):
    curr_img_name = csv_df['filename'][i]
    img_blob.get_blob_to_path(CONTAINERNAME, f'Covid-19-1/images/{curr_img_name}', 'current_image.jpeg')

    np_img = pixels_from_path(file_path='current_image.jpeg', new_size=(224, 224))

    np_img = np_img.reshape(1, 50176)
    row = np.append(np_img[0], [1], axis=0)

    if i == 0:
        data = np.array([row])
    else:
        data = np.append(data, np.array([row]), axis=0)

df = pd.DataFrame(data)

print(df.head())






















