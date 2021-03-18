import numpy as np
import tensorflow as tf
from tensorflow import keras
import os

IMG_SIZE = (224, 224)
SAMPLE_SIZE = 50
EPOCHS = 3
LEARNING_RATE = 0.0001
CSV_FILE = 'dataset'

def pixels_from_path(file_path):
    im = Image.open(file_path)
    im = im.resize(IMG_SIZE)
    np_im = np.array(im) #matrix of pixel RGB values
    return np_im

returnDataset(csv)
with open(file, 'r') as f:
        files = f.readlines()
    return files
    


              
class Dataset():
	def init(csvFile):
		self.dataset= returnDataset(csvFile)
		self.shuffle = true
		self.batchSize = SAMPLE_SIZE
		self.epochs = EPOCHS
		
