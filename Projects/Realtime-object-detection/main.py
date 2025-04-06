import cv2
from utils.yolo_utils import load_model, infer, load_class_names
from utils.draw import draw_boxes

model = load_model()
class_names = load_class_names("data/coco.names")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = infer(model, frame)
    frame = draw_boxes(frame, results, class_names)

    cv2.imshow("Real-Time Object Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
