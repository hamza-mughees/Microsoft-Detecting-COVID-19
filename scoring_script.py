import json
import joblib
import numpy as np
from azureml.core.model import Model
from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array, ImageDataGenerator
from keras.preprocessing import image
from PIL import Image

# Called when the service is loaded
def init():
    global model
    # Get the path to the registered model file and load it
    model_path = Model.get_model_path('classification_model')
    model = joblib.load(model_path)
    
# Called when a request is received
def run(request):
    file_bytes = request.files["image"]
        image = Image.open(file_bytes).convert('RGB')
    image.save('api_call_image/testphoto.png', 'PNG')
    my_image = load_img('api_call_image/testphoto.png', target_size=(224, 224))
    my_image = my_image.convert('L')
    my_image = image.img_to_array(my_image)
    my_image/=255
    my_image = np.expand_dims(my_image, axis=0) # image shape is (1, 12, 12, 3)
    prediction = model.predict(my_image)[0][0]#

    confidence = abs(.5-prediction)*2
    if(prediction>.5):
        answer = "positive"
    else:  
        answer = "negative"

    print("prediction is ", prediction)
    print("confidence is ", confidence)
    print("diagnosis is ", answer)
    dict1 ={
    "results": {
       "diagnosis": answer,
       "confidence": confidence,
       "probability": prediction
        }

    }

    return AMLResponse(json.dumps(dict1), 200)

    
 