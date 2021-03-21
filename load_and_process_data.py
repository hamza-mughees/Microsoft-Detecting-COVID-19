from azure.storage.blob import BlockBlobService
import numpy as np
import pandas as pd
import time
from PIL import Image

STORAGEACCOUNTNAME= 'covid19detecti4594663496'
STORAGEACCOUNTKEY='1xRicfWfUa9rgqyMyiASbzIS+E+kNPKKIropOG/UT63z2/E9+oqrH3Htv/0PjYj6EkH+vSC7PaazBJNjW03lJA=='
CONTAINERNAME= 'sourcedata'
CSV_LOCAL_FILE_NAME= 'local_data_file.csv'
CSV_FILE_BLOB_NAME= 'Covid-19-1/data_file.csv'
IMG_DIR_BLOB_NAME = 'Covid-19-1/images'

csv_blob = BlockBlobService(account_name=STORAGEACCOUNTNAME, account_key=STORAGEACCOUNTKEY)
csv_blob.get_blob_to_path(CONTAINERNAME, CSV_FILE_BLOB_NAME, CSV_LOCAL_FILE_NAME)

img_blob = BlockBlobService(account_name=STORAGEACCOUNTNAME, account_key=STORAGEACCOUNTKEY)

# Original csv dataframe
csv_df = pd.read_csv(CSV_LOCAL_FILE_NAME)

def pixels_from_path(file_path, new_size):
    img = Image.open(file_path)
    img = img.convert('L')
    img = img.resize(new_size)
    np_img = np.array(img)
    return np_img

processed_data_file_name = 'processed_data.csv'

resize_to = 224
data = []

for i in range(csv_df.shape[0]):
    curr_img_name = csv_df['filename'][i]
    img_blob.get_blob_to_path(CONTAINERNAME, f'Covid-19-1/images/{curr_img_name}', 'current_image.jpeg')

    np_img = pixels_from_path(file_path='current_image.jpeg', new_size=(resize_to, resize_to))
    np_img = np_img.reshape(1, resize_to*resize_to)

    diagnosis = 1 if csv_df['diagnosis'][i] == 'positive' else 0
    row = np.append(np_img[0], [diagnosis], axis=0)

    data.append(row)

    print(f'Successfully processed \'{curr_img_name}\'')
    
    if i == 20:
        break

df = pd.DataFrame(np.array(data))

#print(df)

data_file = open(f'./{processed_data_file_name}', 'w')
data_file.write(df.to_csv(index=False))
data_file.close()


















