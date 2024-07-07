#!/usr/bin/env python
# coding: utf-8

# In[11]:
import torch
from torchvision import datasets, transforms, models
import torch.nn as nn
import gradio as gr
from PIL import Image


# In[4]:


# Load your model architecture and weights
model = models.resnet18(weights = models.ResNet18_Weights.DEFAULT)

# Modify the first convolutional layer to accept single-channel input
model.conv1 = nn.Conv2d(1, 64, kernel_size=(7, 7), stride=(2, 2), padding=(3, 3), bias=False)

# Modify the final layer to match the number of classes (binary classification in this case)
num_ftrs = model.fc.in_features
model.fc = nn.Linear(num_ftrs, 2)

model.load_state_dict(torch.load('model.pth' , map_location=torch.device('cpu')))
model.eval()


# In[6]:


# Define the transformations
transform = transforms.Compose([
    transforms.Grayscale(num_output_channels=1),
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

# Prediction function
def predict(image):
    image = Image.fromarray(image)
    image = transform(image).unsqueeze(0)
    with torch.no_grad():
        outputs = model(image)
        _, predicted = torch.max(outputs, 1)
    return "Fractured" if predicted.item() == 1 else "Not Fractured"


# In[17]:



iface = gr.Interface(
    fn=predict,
    inputs=gr.Image(type='numpy'),
    outputs="text",
    title="Bone Fracture Detection",
    description="Upload an X-ray image to detect if there is a bone fracture."
)

# Launch the interface
iface.launch(share=True)


# In[ ]:




