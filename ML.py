import torch
import numpy as np
import cv2

def machineLearningIdentification(repertoire,modelPath):        
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=modelPath, force_reload=True)
    results=[]
    for i in range(len(repertoire)):
        img=repertoire[i]
        results += [model(img)]
        cv2.imwrite('RESULTATS/result'+str(i)+'.jpeg', np.squeeze(results[-1].render())) 
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