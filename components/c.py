import pandas as pd
from transformers import pipeline
import numpy as np
from deep_translator import GoogleTranslator
import opennsfw2 as n2
import os

class kynspector:
    def __init__(self):
        self.classifier = pipeline("sentiment-analysis", model="michellejieli/NSFW_text_classifier")
        self.translate=GoogleTranslator(source='auto', target='en')
    def video_check(self,video_path):
        file_path = os.path.join("E:/Code/python/kyn/temp/", video_path.name)
        with open(file_path, "wb") as f:
            f.write(video_path.getbuffer())
        elapsed_seconds, nsfw_probabilities = n2.predict_video_frames(file_path)
        largest_number = np.max(nsfw_probabilities)
        if largest_number>=0.4:
            category="inappropriate"
        elif largest_number>=0.2 and largest_number<=0.4:
            category="mildly_appropriate"
        else:
            category="appropriate"
        return {"category":category,"prob":largest_number,}
    
    def image_check(self,image_path):
        file_path = os.path.join("E:/Code/python/kyn/temp/", image_path.name)
        with open(file_path, "wb") as f:
            f.write(image_path.getbuffer())
        nsfw_probabilities = n2.predict_image(file_path)
        if nsfw_probabilities>=0.4:
            category="inappropriate"
        elif nsfw_probabilities>=0.2 and nsfw_probabilities<=0.4:
            category="mildly_appropriate"
        else:
            category="appropriate"
        return {"category":category,"prob":nsfw_probabilities}
    def text_check(self,text):
            print(text)
            text=self.translate.translate(text)
            op=self.classifier(text)[0]
            if op['label']=="NSFW":
                category="inappropriate"
            else:
                category="appropriate"
            return {"category":category}
        