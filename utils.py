import json
import urllib.request

def load_class_index():
    class_idx_url = "https://s3.amazonaws.com/deep-learning-models/image-models/imagenet_class_index.json"
    with urllib.request.urlopen(class_idx_url) as url:
        class_idx = json.loads(url.read().decode())
    idx2label = {int(key): value[1] for key, value in class_idx.items()}
    return idx2label

def is_food_detected(label):
    food_keywords = ['pizza', 'burger', 'sushi', 'steak', 'salad', 'apple', 'orange', 'banana', 'cake', 'pasta', 'sandwich', 'ice_cream', 'donut', 'taco', 'soup','chocolate_sauce']
    return any(food in label.lower() for food in food_keywords)
