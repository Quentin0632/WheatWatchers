"""
machine learning identification and saving of the processed pictures with bounding boxes around identified objects in RESULTATS
"""

import torch
import numpy as np
import cv2
import os

def machineLearningIdentification(dir,repertoire,modelPath): 
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))       
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=modelPath, force_reload=True)
    results=[]
    for i in range(len(repertoire)):
        img=repertoire[i]
        results += [model(img)]
        cv2.imwrite(dir+'/result'+str(i)+'.jpeg', np.squeeze(results[-1].render())) 
    return results

def getIdentificationInfo(repertoire,results):
    allLabels=[]
    allLabelsName=[]
    for j in range(len(repertoire)):
        for i in range(results[j].xyxy[0].size()[0]):
            label=int(results[j].xyxy[0][i][5])
            if(label not in allLabels):
                allLabels+=[label]
                allLabelsName+=[results[j].pandas().xyxy[0]['name'].values[i]]
    allCaract=[]
    for j in range(len(repertoire)):
        caracVect=[]
        nbLignes=results[j].xyxy[0].size()[0]
        for ligne in range(nbLignes):
            xmin,ymin,xmax,ymax,confidence,classe=[float(elm) for elm in results[j].xyxy[0][ligne]]
            surface=(xmax-xmin)*(ymax-ymin)
            centre=[xmin+(xmax-xmin)/2,ymin+(ymax-ymin)/2]
            caracVect+=[[centre,surface,confidence,int(classe)]]
        allCaract+=[caracVect]
    return allLabels,allLabelsName,allCaract