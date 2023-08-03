import json
import os

json_folder_path = "/home/ntq/khai/ultralytics/datasets/vistas/training/v2.0/polygons"
output_folder_path = "/home/ntq/khai/ultralytics/datasets/vistas/labels/train"


def polygon_to_xyxy(polygon):
    x_values = [point[0] for point in polygon]
    y_values = [point[1] for point in polygon]
    x1 = int(min(x_values))
    y1 = int(min(y_values))
    x2 = int(max(x_values))
    y2 = int(max(y_values))
    return x1, y1, x2, y2

def calculate(a, b, w, h, x1, y1, x2, y2, width, height):
    a = (x2 - x1) / width
    b = (y2 - y1) / height
    w = ((x1 + x2) / 2) / width
    h = ((y1 + y2) / 2) / height
    return a, b, w, h
# Tạo thư mục đầu ra nếu chưa tồn tại
#os.makedirs(output_folder_path, exist_ok=True)

for filename in os.listdir(json_folder_path):
    if filename.endswith('.json'):
        file_path = os.path.join(json_folder_path, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        height = data['height']
        width = data['width']
        
        objects = data['objects']

        car_objs = [obj for obj in objects if 'object--vehicle--car' in obj['label']]
        
        output_file_name = os.path.splitext(filename)[0]  # Remove the ".json" extension
        output_file_path = os.path.join(output_folder_path, f"{output_file_name}.txt")
        
        with open(output_file_path, 'w') as output_file:
            for car_obj in car_objs:
                polygon = car_obj['polygon']
                x1, y1, x2, y2 = polygon_to_xyxy(polygon)
                a, b, w, h = calculate(0, 0, 0, 0, x1, y1, x2, y2, width, height)
                output_file.write(f"0 {w} {h} {a} {b}\n")


