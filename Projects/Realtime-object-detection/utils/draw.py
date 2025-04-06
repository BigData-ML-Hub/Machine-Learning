import cv2

def draw_boxes(image, results, class_names):
    for *xyxy, conf, cls in results:
        label = f"{class_names[int(cls)]} {conf:.2f}"
        pt1 = (int(xyxy[0]), int(xyxy[1]))
        pt2 = (int(xyxy[2]), int(xyxy[3]))
        cv2.rectangle(image, pt1, pt2, (0, 255, 0), 2)
        cv2.putText(image, label, pt1, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    return image