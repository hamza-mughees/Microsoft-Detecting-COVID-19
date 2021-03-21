from azure.storage.blob import BlockBlobService
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

# This dataframe will be appended to with the numpy image arrays
df = pd.DataFrame(columns=['filename', 'diagnosis'])

print(df.head())

for i in range(csv_df.shape[0]):
    curr_img_name = csv_df['filename'][i]
    print(curr_img_name)
    img_blob.get_blob_to_path(CONTAINERNAME, f'Covid-19-1/images/{curr_img_name}', 'current_image.jpeg')

    img = Image.open('current_image.jpeg')
    print(img.size)

    if i == 3:
        break