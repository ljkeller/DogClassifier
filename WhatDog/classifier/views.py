from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.core.files.storage import FileSystemStorage

import os

from fastai.learner import *

# Assumes cwd is DogClassifier/WhatDog
MODEL='export.pkl'

def index(request):
    if request.method == 'POST' and request.FILES['image']:
        image_fp = request.FILES['image']

        # need to store image for client & processing
        fs = FileSystemStorage()

        fs_image = fs.save(image_fp.name, image_fp) # use for prediction
        uploaded_file_url = fs.url(fs_image) # use for viewing image
        image_path = os.path.join(os.getcwd(), 'media', fs_image)

        classifier = load_learner(MODEL)
        label, tensorL, tensor_all = classifier.predict(image_path)
        prob = '{:.1f}'.format(tensor_all[tensorL]*100)

        return render(request, "classifier/index.html", {
            'img_url': uploaded_file_url,
            'prediction_label': label,
            'prediction_prob': prob
        })
    
    else:
        return render(request, "classifier/index.html")

texts = ["Hot dog",
         "Wiener dog",
         "Cord Dog"]

def section(request, num):
    if 1<=num<=3:
        return HttpResponse(texts[num-1])
    else:
        raise Http404('No such section')
# Create your views here.
