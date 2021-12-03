
import os
image_dir = r"E:\data\camera_calibration\chess_photo"
txt_file="data_list.txt"

image_path_list=[]

for image_path in os.listdir(image_dir):
    if not image_path.endswith('.jpg'): continue
    print("the image path is  {0}".format(image_path))
    image_path_list.append(os.path.join(image_dir, image_path))

with open(os.path.join(image_dir, txt_file),  'w') as file:
    file.writelines(["%s\n" % item for item in image_path_list])


