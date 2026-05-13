# Fashion MNIST Image Classifier

A deep learning-based fashion image classification project built using TensorFlow/Keras and deployed with Streamlit.

This project trains an Artificial Neural Network (ANN) to classify fashion products from grayscale images using the Fashion MNIST dataset and provides a web interface for users to upload clothing images for prediction.

---

## Project Overview

This project demonstrates an end-to-end deep learning workflow for image classification.

The workflow includes:

- Loading and preprocessing image datasets
- Building and training an Artificial Neural Network (ANN)
- Model evaluation
- Prediction on unseen images
- Confusion matrix analysis
- Saving/loading trained models
- Streamlit deployment

The trained model predicts fashion product categories from grayscale clothing images.

---

## Features

- Fashion image classification
- ANN-based deep learning model
- TensorFlow/Keras implementation
- Confusion matrix evaluation
- Accuracy and loss tracking
- Streamlit web application
- Upload custom fashion images for prediction

---

## Dataset

This project uses the **Fashion MNIST Dataset**.

Fashion MNIST contains 70,000 grayscale images of fashion products.

### Image Details
- Image size: 28 × 28 pixels
- Grayscale images
- 10 classes

### Categories

| Label | Class Name |
|------|------------|
| 0 | T-shirt / Top |
| 1 | Trouser |
| 2 | Pullover |
| 3 | Dress |
| 4 | Coat |
| 5 | Sandal |
| 6 | Shirt |
| 7 | Sneaker |
| 8 | Bag |
| 9 | Ankle Boot |

### Dataset Split
- Training images: 60,000
- Test images: 10,000

---

## Tech Stack

### Programming Language
- Python 3

### Libraries & Frameworks
- TensorFlow
- Keras
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Pillow
- Streamlit

---

## Model Architecture

Artificial Neural Network (ANN)

```text
Input Image (28x28)
        ↓
Flatten Layer
        ↓
Dense Layer (128 neurons, ReLU)
        ↓
Output Layer (10 neurons, Softmax)
        ↓
Fashion Category Prediction
```

### Layer Explanation

**Input Layer**
- Accepts 28×28 grayscale fashion image

**Flatten Layer**
- Converts 2D image into 784-dimensional vector

**Hidden Layer**
- Dense layer with 128 neurons
- ReLU activation function

**Output Layer**
- 10 neurons
- Softmax activation
- Predicts probabilities for each fashion category

---

## Training Configuration

- Optimizer: Adam
- Loss Function: Sparse Categorical Crossentropy
- Evaluation Metric: Accuracy
- Epochs: 5
- Batch Size: Default TensorFlow batch size

---

## Installation

Clone repository:

```bash
git clone https://github.com/VivekSingh1201/mnist-fashion-classifier.git
cd fashion-mnist-classifier
```

Create virtual environment:

```bash
python -m venv DLenv
```

Activate environment:

### macOS/Linux
```bash
source DLenv/bin/activate
```

### Windows
```bash
DLenv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Project Structure

```text
fashion-mnist-classifier/
│
├── app.py
├── train_model.py
├── fashion_mnist_model.keras
├── requirements.txt
├── README.md
└── images/
```

---

## Training the Model

Run:

```bash
python train_model.py
```

This script:

- loads Fashion MNIST dataset
- preprocesses images
- trains ANN model
- evaluates performance
- saves trained model

Saved model:

```text
fashion_mnist_model.keras
```

---

## Running the Web App

Start Streamlit:

```bash
streamlit run app.py
```

Then open:

```text
http://localhost:8501
```

---

## Example Workflow

1. Launch Streamlit app
2. Upload a fashion image
3. Image gets resized and normalized
4. Model predicts clothing category
5. Confidence score displayed

---

## Model Evaluation

Evaluation methods:

- Test Accuracy
- Test Loss
- Confusion Matrix

Confusion matrix helps identify:

- which classes are predicted correctly
- class confusion
- weak-performing categories

Example:

- Shirt confused with T-shirt
- Sneaker confused with Sandal

---

## Sample Prediction Classes

Possible outputs:

```text
T-shirt / Top
Trouser
Pullover
Dress
Coat
Sandal
Shirt
Sneaker
Bag
Ankle Boot
```

---

## Future Improvements

- Replace ANN with CNN for higher accuracy
- Add support for colored real-world fashion images
- Deploy on Streamlit Cloud / Render
- Add probability visualization
- Improve UI design
- Add drag-and-drop upload

---

## Learning Outcomes

This project demonstrates understanding of:

- Artificial Neural Networks
- Deep Learning fundamentals
- Activation functions
- ReLU
- Softmax
- Loss functions
- Optimizers
- Fashion image classification
- Confusion matrix interpretation
- Model deployment

---

## Author

**Vivek Kumar Singh**  
B.Tech CSE Student

---

## License

MIT License
