from ultralytics import YOLO
import cv2
# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch
#model = YOLO("/home/ntq/khai/runs/detect/train2/weights/best.pt")  # load a pretrained model (recommended for training)
model = YOLO("/home/ntq/khai/ultralytics/yolov8n.pt")
#model= ("/home/ntq/khai/runs/detect/predict3/Cars-and-City-Heat-Fotolia_26282305_S.jpg", save=True, imgsz=320, conf=0.01)
#r = model("/home/ntq/khai/runs/detect/predict3/Cars-and-City-Heat-Fotolia_26282305_S.jpg", conf = 0.3 )[0]
#out = r.plot()
#cv2.imwrite('out.jpg', out)


# Use the model
model.train(data="/home/ntq/khai/ultralytics/ultralytics/datasets/coco-pose.yaml", epochs=3)  # train the model
#metrics = model.val()  # evaluate model performance on the validation set
#results = model("/home/ntq/khai/ultralytics/dataset/vistas/images/validation/_2yFuPMD1eo4D1sHkx-c4Q.jpg")  # predict on an image
# path = model.export(format="onnx")  # export the model to ONNX format