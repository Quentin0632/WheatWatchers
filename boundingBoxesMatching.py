import numpy as np
import sys

def similarity (box1,box2):
    C1,S1,Cert1,lab1=box1
    C2,S2,Cert2,lab2=box2
    dist=np.sqrt(C1[0]-C2[0])**2
    Surface=1-np.minimum(S1,S2)/np.maximum(S1,S2)
    Surete=np.abs((Cert1-Cert2))
    cout=dist*Surface*Surete
    return(cout)


def costFunction(allbBoxL,allbBoxR,coutMax,confidenceMin):
    couplesbBox=[]
    bBoxL=[]
    bBoxR=[]
    for i in range(len(allbBoxL)):
        if(allbBoxL[i][2]>confidenceMin):
            bBoxL+=[allbBoxL[i]]
    for i in range(len(allbBoxR)):
        if(allbBoxR[i][2]>confidenceMin):
            bBoxR+=[allbBoxR[i]]     
    if(len(bBoxL)!=0 and len(bBoxR)!=0):
        for indLeft in range(len(bBoxL)):
            centreL,surfaceL,confidenceL,classeL=bBoxL[indLeft]
            coutMin=sys.float_info.max
            indRightMin=0
            for indRight in range(len(bBoxR)):
                centreR,surfaceR,confidenceR,classeR=bBoxR[indRight]
                if(classeL==classeR and centreL[0]>centreR[0]):
                    cout=similarity(bBoxL[indLeft],bBoxR[indRight])
                    if(cout<coutMin):
                        coutMin=cout
                        indRightMin=indRight
            couplesbBox+=[[bBoxL[indLeft],bBoxR[indRightMin],coutMin]]
    couplesbBoxSansDoublons=[]
    indicesRetires=[]
    for i in range(len(couplesbBox)):
        if(i not in indicesRetires):
            coutMin=couplesbBox[i][2]
            indMin=i            
            for j in range(len(couplesbBox)):
                if(couplesbBox[i][1][0]==couplesbBox[j][1][0]):
                    indicesRetires+=[j]
                if(i!=j and couplesbBox[i][1][0]==couplesbBox[j][1][0] and couplesbBox[j][2]<coutMin):
                    indMin=j
                    coutMin=couplesbBox[j][2]
            couplesbBoxSansDoublons+=[couplesbBox[indMin]]
    bestCouples=[]
    for i in range(len(couplesbBoxSansDoublons)):
        if(couplesbBoxSansDoublons[i][2]<coutMax):
            bestCouples+=[couplesbBoxSansDoublons[i][0:2]]
    return bestCouples
