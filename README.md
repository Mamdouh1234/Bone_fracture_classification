# Global Health Medical Center - Bone Fracture Image Classification
A Deep Learning model for classifying bone fracture

## Business Scenario
In the rapidly evolving field of medical diagnostics, timely and accurate detection of bone fractures can significantly impact patient outcomes and healthcare efficiency. Emergency rooms and clinics around the world are often overwhelmed, leading to delayed diagnoses and increased patient suffering.

Imagine a scenario where a state-of-the-art AI system assists medical professionals by providing rapid, reliable, and precise identification of bone fractures from X-ray images. This technology can help reduce diagnostic errors, expedite treatment decisions, and ultimately save lives. By leveraging advanced machine learning techniques and powerful neural networks, this project aims to develop an automated solution for bone fracture detection.

This bone fracture classification system can be integrated into existing hospital workflows, assisting radiologists in their decision-making process. It can serve as a second opinion, catching fractures that might be missed during a busy shift or by less experienced practitioners. Additionally, in rural or under-resourced settings, where access to expert radiologists is limited, this AI system can provide critical support, ensuring that patients receive the care they need, when they need it.

By leveraging advanced machine learning techniques and a sophisticated convolutional neural network (CNN) architecture, this project seeks to develop a robust and reliable model for bone fracture detection. This AI system will provide significant support in:

- Reducing diagnostic errors: Acting as a second pair of eyes for radiologists, the system helps catch fractures that might be missed during hectic shifts or by less experienced practitioners.
- Expediting treatment decisions: Rapid and accurate fracture detection enables quicker treatment initiation, improving patient outcomes.
- Enhancing healthcare accessibility: In rural or under-resourced settings, where access to expert radiologists is limited, the AI system can provide essential diagnostic support.
Welcome to the future of medical diagnostics, where technology and healthcare unite to enhance patient care and streamline medical processes. Let's dive into the development of this groundbreaking bone fracture image classification model.

## Dataset
The dataset used in this project is Mura Dataset by Stanford university , it contains 40,561 images of fractured and unfractured body bones , 
more about the dataset can be found  [here](https://stanfordmlgroup.github.io/competitions/mura/).

## Model Architecture
The model used for this project is Resnet18(tested Resnet50 and Resnet101 , and achieved same results):


## Training
The model is trained using the Adam optimizer and CrossEntropyLoss. The learning rate is adjusted dynamically using a scheduler. The training process includes:

Loading the training & validation sets
Data augmentation for the training set
Training over 25 epoch.
Evaluation on the validation set after each epoch

## Evaluation
The model is evaluated using accuracy and loss metrics on both the validation and test sets. Cross-validation techniques can be employed to ensure robustness.

## Results
The final model achieved the following performance:

Train Accuracy: 83.92%
Validation Accuracy: 79.08%

These results demonstrate the model's effectiveness in classifying bone fractures.
