"""
Run all the process (excepted the conversion videos->frames) and create the CSV files with the GPS locations and labels in the directory CSV
"""

import glob
import arrayToCSV as csvConverter
import Calc_coordonnéesGPS as GPS
import ML
import distanceCarToCrop as carToCrop

#Camera holder parameter
baseline=40      #distance between both cameras in centimeters
#Camera parameters
f = 35           #focal lenght
alpha = 86       #Field of view
#Machine learning parameters
confidenceMin=0.4   #minimum level of convidence to identify an object
modelPath='yolov5/runs/train/exp10/weights/last.pt'   #path to our model
#modelPath='yolov5/runs/train/exp_960_8_150_m/weights/best_960_8_150_m'

coutMax=1


repertoireGLOBAL= glob.glob('FRAMES/LEFT/*')+glob.glob('FRAMES/RIGHT/*')
repertoire=[]
for i in range(len(repertoireGLOBAL)):
    repertoire+=glob.glob(repertoireGLOBAL[i]+"/*")

dir='RESULTATS'
results=ML.machineLearningIdentification(dir,repertoire,modelPath)

profondeurImages = carToCrop.depth(repertoire,baseline,f,alpha,coutMax,confidenceMin,results)       


headerCrop = ['crop', 'latitude', 'longitude']
dataCrop = carToCrop.createDataCropCSV(repertoire,profondeurImages,results) 

headerVoiture = ['image', 'latitude', 'longitude']
dataVoiture = GPS.coordonneesGPSVoiture(profondeurImages,repertoire)

fileCrop='CSV/cropData.csv'
fileVoiture='CSV/carData.csv'


csvConverter.arrayToCSV(fileCrop,headerCrop,dataCrop)
csvConverter.arrayToCSV(fileVoiture,headerVoiture,dataVoiture)



