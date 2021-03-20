from azure.storage.blob import BlockBlobService
import pandas as pd
import time
from PIL import Image

#import tables

# replace the variable with our specific values 
#storage account name will be the dns prefix we create 
#az login
#az storage account list -o table
#az storage account keys list -n YourAccount
#to extract key 
#az storage account keys list -n YourAccount -o json --query "[0].value"
#or else go to microsoft azure go to storage accounts select a name go to settings 
#and then copy the storage account name and key gi
STORAGEACCOUNTNAME= 'covid19detecti4594663496'
STORAGEACCOUNTKEY='eT6uCBypyr4cyEp8hWJbUtyJz5vbvWAzuSZmeZw3+Xs3dFKcoDunEisYTGG1uW2SOsbcIq9L/hI12CLQCVCMHA=='
CONTAINERNAME= 'sourcedata'
CSV_LOCAL_FILE_NAME= 'local_data_file.csv'
CSV_FILE_BLOB_NAME= 'Covid-19-1/data_file.csv'

IMG_LOCAL_DIR_NAME = 'local_image_dir'
IMG_FILE_BLOB_NAME = 'Covid-19-1/images'
TEMP_IMG_NAME = 'Covid-19-1/images/x-ray-0.jpeg'

#download from blob
t1=time.time()
csv_blob=BlockBlobService(account_name=STORAGEACCOUNTNAME,account_key=STORAGEACCOUNTKEY)
csv_blob.get_blob_to_path(CONTAINERNAME,CSV_FILE_BLOB_NAME,CSV_LOCAL_FILE_NAME)

img_blob=BlockBlobService(account_name=STORAGEACCOUNTNAME,account_key=STORAGEACCOUNTKEY)
img_blob.get_blob_to_path(CONTAINERNAME,TEMP_IMG_NAME,IMG_LOCAL_DIR_NAME)

t2=time.time()
print(("It takes %s seconds to download "+ CSV_FILE_BLOB_NAME) % (t2 - t1))

#read the data into a pandas dataframe from the downloadable file 
#localFile is the filepath 
csv_dataset = pd.read_csv(CSV_LOCAL_FILE_NAME)
img = Image.open(IMG_LOCAL_DIR_NAME)
print(img.size)

""" misc messing around with data

#inspect the number of rows and columns in dataset 
print('the size of the data is: %d rows and  %d columns' % dataframe_blobdata.shape)

# inspect the first/ last few rows in the dataset 
dataframe_blobdata.head(10)

dataframe_blobdata.tail(10)
#check the datatype of each column
for col in dataframe_blobdata.columns:
    print(dataframe_blobdata[col].name, ':\t', dataframe_blobdata[col].dtype)
    
#check for basic stats 
dataframe_blobdata.describe()

#look at the number of enteries for each column
dataframe_blobdata['<column_name>'].value_counts()

#count missing values vs acc numbrt of entreies
miss_num = dataframe_blobdata.shape[0] - dataframe_blobdata.count()
print(miss_num)

#replace the missing values :
dataframe_blobdata_mode = dataframe_blobdata.fillna(
    {'<column_name>': dataframe_blobdata['<column_name>'].mode()[0]})
"""