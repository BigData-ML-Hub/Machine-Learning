import torch
from config import MODEL_PATH, DEVICE, LABELS_PATH

# Load class names
def load_class_names(path):
    with open(path, "r") as f:
        return [line.strip() for line in f.readlines()]

# Load model
def load_model():
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=MODEL_PATH)
    model.to(DEVICE).eval()
    return model

# Predict
@torch.no_grad()
def infer(model, frame):
    results = model(frame)
    return results.xyxy[0].cpu().numpy()