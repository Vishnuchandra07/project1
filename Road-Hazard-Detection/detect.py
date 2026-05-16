from ultralytics import YOLO
import cv2

# load your trained model
model = YOLO("runs/detect/train/weights/best.pt")  # adjust if needed

# give test image path
img_path = "test.jpg"   # put any image here

# run detection
results = model(img_path)

# show result
annotated = results[0].plot()

cv2.imshow("Detection Result", annotated)
cv2.waitKey(0)
cv2.destroyAllWindows()

# save result
cv2.imwrite("output.jpg", annotated)
