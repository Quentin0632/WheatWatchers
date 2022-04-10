import ML
import numpy as np
import boundingBoxesMatching as BBmatch
import Calc_coordonnéesGPS as GPS
import cv2

def triangulation(widthImage,baseline,f,alpha,horizontalShift):
    f_pixel = (widthImage * 0.5) / np.tan(alpha * 0.5 * np.pi/180)
    zDepth = (baseline*f_pixel)/horizontalShift
    return fcorrection(zDepth)

def fcorrection(z):
    return (np.sqrt(2335000*z+1387810)-1661)*0.0014133


def depth(repertoire,baseline,f,alpha,coutMax,confidenceMin,results):
    allLabels,allLabelsName,allCaract=ML.getIdentificationInfo(repertoire,results)     
    n=len(repertoire)//2
    profondeurImages=[]
    for i in range(n):
        allbBoxL=allCaract[i]
        allbBoxR=allCaract[i+n]
        bestCouples=BBmatch.costFunction(allbBoxL,allbBoxR,coutMax,confidenceMin)
        profParLabel=[]
        for label in allLabels:
            profondeur=0
            compteur=0
            for j in range(len(bestCouples)):
                [caractL,caractR]=bestCouples[j]
                if(caractL[3]==label):
                    compteur+=1
                    widthImage=cv2.imread(repertoire[i]).shape[1]
                    centreL=caractL[0]
                    centreR=caractR[0]
                    horizontalShift=abs(centreL[0]-centreR[0])
                    profondeur+=triangulation(widthImage,baseline,f,alpha,horizontalShift)
            if(compteur!=0):
                profondeur=profondeur/compteur
            profParLabel+=[[label,profondeur]]
        profondeurImages+=[profParLabel]
    return profondeurImages
 
def createDataCropCSV(repertoire,profondeurImages,results): 
    allLabels,allLabelsName,allCaract = ML.getIdentificationInfo(repertoire,results)
    labelAndCoords=GPS.coordonneesGPSChamp(profondeurImages,repertoire)   
    liste=[]
    for i in range(len(labelAndCoords)):
        for j in range(len(labelAndCoords[i])):
            for k in range(len(allLabels)):
                if(labelAndCoords[i][j][0]==allLabels[k] and profondeurImages[i][j][1]!=0):
                    labelAndCoords[i][j][0]=allLabelsName[k]
                    liste+=[labelAndCoords[i][j]]
    return liste