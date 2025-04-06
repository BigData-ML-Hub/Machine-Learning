```bash
 realtime_object_detection/
 ├── data/
 │   └── coco.names                   # List of class labels
 ├── models/
 │   └── yolov5s.pt                   # Pre-trained YOLO model (downloaded)
 ├── utils/
 │   ├── draw.py                     # Drawing utility for bounding boxes
 │   └── yolo_utils.py               # Load model and inference
 ├── main.py                             # Entry point: Live camera object detection
 ├── requirements.txt                   # Python dependencies
 ├── config.py                          # Paths, configs, and settings
 ├── idea.md                             # Project write-up and vision

```


# Real-Time Object Detection Using YOLO & OpenCV

## Overview
A hands-on computer vision project designed to:
- Detect objects in real time from webcam feeds.
- Use YOLOv5 with PyTorch and CUDA acceleration.
- Integrate OpenCV for video capture and drawing.

## Goals
- Understand object detection pipelines
- Implement and run YOLO models
- Learn to optimize with CUDA
- Build a minimal working app with webcam

## Learning Outcomes
- PyTorch model inference
- Working with OpenCV
- CUDA integration and GPU testing
- COCO dataset & label mapping
- Drawing bounding boxes and scores

## Milestones
1. Setup YOLOv5 with torch & CUDA
2. Test on static images
3. Add webcam input
4. Draw predictions on video feed
5. Package into a single script

## 📁 File Structure
(See project root above)

## Next Steps
- Add image/video upload for inference
- Try different YOLO sizes (s, m, l, x)
- Export as ONNX or TensorRT for deployment



### The class names are directly defined in config.py as LABELS