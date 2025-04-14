from PIL import Image
import torch
import torchvision.transforms as transforms

def diagnose_image(image_file):
    image = Image.open(image_file).convert('RGB')
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor()
    ])
    image_tensor = transform(image).unsqueeze(0)
    labels = ['Tomato Blight', 'Rice Leaf Spot', 'Healthy']
    prediction = torch.randint(0, len(labels), (1,)).item()
    return f"Predicted Disease: {labels[prediction]}"
