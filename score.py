import json
import numpy as np
import tensorflow as tf
from tensorflow import keras
#from sklearn.externals import joblib
import azureml
from azureml.contrib.services.aml_request import AMLRequest, rawhttp
from azureml.contrib.services.aml_response import AMLResponse
from azureml.core.model import Model
from io import BytesIO

import PIL
from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array, ImageDataGenerator
from keras.preprocessing import image
from PIL import Image
import traceback
    
def init():
    global model
    # Replace filename if needed.
    model_path = Model.get_model_path('classification_model')
    # model = joblib.load(model_path)
    model = tf.keras.models.load_model(model_path)

@rawhttp
def run(request):
	global testType
	global testType2
	try:
		if(request.method=='POST'):
			#file_bytes = request.files['image']
			file_bytes = request.data

			my_image = Image.open(BytesIO(file_bytes)).convert('RGB')
			testType=type(my_image)
			#image = (Image.open(file_bytes.stream))
			#image.save('api_call_image\testphoto.png', 'PNG')
			#my_image = load_img('api_call_image\testphoto.png', target_size=(224, 224))
			my_image = my_image.resize((224,224))

			my_image = my_image.convert('L')
			testType2=type(my_image)
			my_image = image.img_to_array(my_image)
			my_image/=255
			my_image = np.expand_dims(my_image, axis=0)
			prediction = model.predict(my_image)[0][0]#

			confidence = abs(.5-prediction)*2
			if(prediction>.5):
				answer = "positive"
			else:
				answer = "negative"

			#print("prediction is ", prediction)
			#print("confidence is ", confidence)
			#print("diagnosis is ", answer)
			dict1 ={
			   "diagnosis": str(answer),
			   "confidence": str(confidence),
			   "probability": str(prediction)
					}

			return AMLResponse(json.dumps(dict1), 200)
			
		else:
			return AMLResponse(json.dumps("bad request"), 500)


	except Exception as e:
		dict2 ={
			"exception": "error is",
			"error": str(e),
			"tb": traceback.format_exc(),
			"type": str(testType),
			"type2": str(testType2)

				}
		
		return AMLResponse(json.dumps(dict2) , 200)
	

    
 
