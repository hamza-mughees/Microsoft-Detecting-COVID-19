from azure.storage.blob import BlockBlobService
import os
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

csv_blob = BlockBlobService(account_name=STORAGEACCOUNTNAME, account_key=STORAGEACCOUNTKEY)
csv_blob.get_blob_to_path(CONTAINERNAME, CSV_FILE_BLOB_NAME, CSV_LOCAL_FILE_NAME)

img_blob = BlockBlobService(account_name=STORAGEACCOUNTNAME, account_key=STORAGEACCOUNTKEY)

# Original csv dataframe
csv_df = pd.read_csv(CSV_LOCAL_FILE_NAME)

X = csv_df.iloc[:, :-1].values
y = csv_df.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

for i in range(X_train.shape[0]):
    curr_img_name = X_train[i, 0]
    diagnosis = y_train[i]
    
    dst_path = TRAIN_POS if diagnosis == 'positive' else TRAIN_NEG

    print(f'{i}: Writing \'{curr_img_name}\' as {diagnosis} on the path: \'{dst_path}\'')
    img_blob.get_blob_to_path(CONTAINERNAME, f'{IMG_DIR_BLOB_NAME}/{curr_img_name}', f'{dst_path}/{curr_img_name}')

for i in range(X_test.shape[0]):
    curr_img_name = X_test[i, 0]
    diagnosis = y_test[i]

    dst_path = TEST_POS if diagnosis == 'positive' else TEST_NEG

    print(f'{i}: Writing \'{curr_img_name}\' as {diagnosis} on the path: \'{dst_path}\'')
    img_blob.get_blob_to_path(CONTAINERNAME, f'{IMG_DIR_BLOB_NAME}/{curr_img_name}', f'{dst_path}/{curr_img_name}')



'''
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
'''

















