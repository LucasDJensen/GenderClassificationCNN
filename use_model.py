import os

import numpy as np
from keras.models import load_model
from keras.utils import load_img

model = load_model('model_saved.h5')

dir_path = "E:\img_align_celeba\img_align_celeba"
for path in os.listdir(dir_path):
    # check if current path is a file
    join = os.path.join(dir_path, path)
    if os.path.isfile(join):
        image = load_img(join, target_size=(178, 218))
        img = np.array(image)
        img = img / 255.0
        img = img.reshape(1, 178, 218, 3)
        label = model.predict(img)
        # print("Predicted Class (0 - female , 1- male): ", label[0][0], join)
        if label[0][0] < 0.5:
            sub = 'ai_female'
        else:
            sub = 'ai_male'
        # print(join)
        li = os.path.split(join)
        joined_pa = os.path.join(li[0], sub, li[1])
        # print(joined_pa)
        os.rename(join, joined_pa)
