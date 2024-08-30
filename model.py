import torch
from torchvision import models
from utils import load_class_index

class_idx = load_class_index()

def load_model():
    model = models.resnet50(pretrained=True)
    model.eval()
    return model

def classify_image(image_tensor):
    model = load_model()
    with torch.no_grad():
        outputs = model(image_tensor)
    _, predicted = torch.max(outputs, 1)
    return class_idx[predicted.item()]
