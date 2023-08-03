import pandas as pd
import cv2
import matplotlib.pyplot as plt
import json
import os 

# Read the JSON file
file_json = r"C:\Users\User\convert\json\jEUk_wzXO_ft8gCIPp9ddA.json"
json_folder_path = "/home/ntq/khai/vistas/validation/v2.0/polygons"

for filename in os.listdir(json_folder_path):
    if filename.endswith('.json'):
        file_path = os.path.join(json_folder_path, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
             
"""
with open(file_json, "r") as read_file:
    data = json.load(read_file)
"""
# Extract the objects and labels from the data
objects = data['objects']
labels = [obj['label'] for obj in objects]

#print (labels)
# Filter the car objects
car_objs = [obj for obj in objects if 'object--vehicle--car' in obj['label']]
car_labels = [obj['label'] for obj in data['objects'] if obj['label'] == 'object--vehicle--car']
id_objs = [obj['id'] for obj in car_objs]  # id of car in file json 

# map full id class car
id_car = ['0' for _ in id_objs]

print(id_car)
#Load and display the image
img_path = 'jEUk_wzXO_ft8gCIPp9ddA.jpg'
img = cv2.imread(img_path)

# Define the polygon_to_xyxy() function to convert polygon coordinates to x1, y1, x2, y2
def polygon_to_xyxy(polygon):
    x_values = [point[0] for point in polygon]
    y_values = [point[1] for point in polygon]
    x1 = int(min(x_values))
    y1 = int(min(y_values))
    x2 = int(max(x_values))
    y2 = int(max(y_values))
    return x1, y1, x2, y2

# Create a figure and subplots
#fig, axs = plt.subplots(len(car_objs), 1, figsize=(6,  6 * len(car_objs)))
with open('data/jEUk_wzXO_ft8gCIPp9ddA.txt', 'w') as f:
    for i, car_obj in enumerate(car_objs):
        x1, y1, x2, y2 = polygon_to_xyxy(car_obj['polygon'])

        # Calculate normalized values
        height, width, _ = img.shape

        a = (x2 - x1) / width
        b = (y2 - y1) / height
        w = ((x1 + x2) / 2) / width
        h = ((y1 + y2) / 2) / height

        f.write("{:<1d} {:.4f} {:.4f} {:.4f} {:.4f}\n".format(0, a, b, w, h))


