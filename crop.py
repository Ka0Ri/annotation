import os
import cv2
import numpy as np

name_file = "confused-case"

try:
    os.makedirs(name_file)    
    print("Directory " , name_file ,  " Created ")
except FileExistsError:
    print("Directory " , name_file ,  " already exists")

img = cv2.imread(os.path.join("crop example images", name_file + ".jpg"))
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
h_img, w_img = img.shape[:2]



with open(os.path.join("crop example images", name_file + ".txt")) as f:
    lines = f.readlines()
    count = 0
    for bb in lines:
        cl, x, y, w, h = bb[:-1].split(" ")
        cl, x, y, w, h = float(cl), float(x) * w_img, float(y) * h_img, float(w) * w_img, float(h) * h_img
        print(cl, x, y, w, h)
        
        sub_img = img[int((y - h/2)):int((y + h/2)), int((x - w/2)):int((x + w/2))]
        cv2.rectangle(img, (int((x - w/2)), int((y - h/2))), (int((x + w/2)), int((y + h/2))), (255,0 ,0), thickness=5)
        cv2.imwrite(os.path.join(name_file, str(count) + ".jpg"), sub_img)
        count += 1
    cv2.imwrite(os.path.join(name_file, "img.jpg"), img)

    