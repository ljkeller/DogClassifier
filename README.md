# WhatDog - Dog 🌭🐶 Classifier Web App

WhatDog is a web application (local) that uses machine learning to classify images of dogs[^dog]. The web app is built with Django and the neural network is a transfer-learned ResNet using [FastAI](https://www.fast.ai/) and PyTorch.

![WhatDog](https://user-images.githubusercontent.com/44109284/229381307-57fc50de-96f2-458e-8167-86af23ed1138.png)

[^dog]: a hot dog, wiener dog, or corn dog

## Data Acquisition and Model Training

The data used to train the model was acquired through Azure Cognitive Services, which is a simple Microsoft API that can be used to download images. 150 images for each class were stored in directories named after the image ground truth label. **Total dataset used: ~450 images before cleaning.**

> Note: I personally cleaned up invalid/incorrect images after gathering the data. There were roughly 10 corrupt images and 10 misslabeled or invalid images. Images were **resized to 224x224** and batches were [augmented](https://docs.fast.ai/vision.augment.html#aug_transforms) ofcourse.

Achieving 97% accuracy on the hold out set (20% of samples, randomly sampled), the WhatDog model was trained using FastAI and PyTorch.

**If you're interested in reproducing the model training**, you can follow the steps outlined in the `dog_classifier.ipynb` Jupyter notebook provided in this repository.

## Getting Started

### Prerequisites

To run the WhatDog app, you'll need:

- Python 3.x
- Django 3.x
- A modern web browser like Google Chrome or Mozilla Firefox

To train the WhatDog model, you'll need:

- Python 3.x (prefer an [Anaconda](https://www.anaconda.com/products/distribution) install)
- FastAI, PyTorch libraries, and much more captured in the `environment.yml`

(View the environment.yml for more information)

### Installing

1. Clone this repository to your local machine:
```bash
git clone https://github.com/ljkeller/DogClassifier.git
```
2. Install the required Python packages using [conda](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment):
```bash
conda env create -f environment.yml
```

### Usage
1. Run through the `dog_classifier.ipynb` until you've exported your model
2. Start the development server:
```bash
python manage.py runserver
```
3. Open your web browser and navigate to http://localhost:8000 to access the app.
4. Upload an image of a dog by clicking the "Choose File" button and selecting an image file from your computer.

5. Click the "Submit" button to get a prediction of the breed of the uploaded dog image.

## License
The WhatDog app is released under the MIT License. Feel free to use, modify, and distribute this code as you see fit.
