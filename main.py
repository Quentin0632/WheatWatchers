import glob
import arrayToCSV as csvConverter
import Calc_coordonnéesGPS as GPS
import ML
import distanceCarToCrop as carToCrop

baseline=40
f = 35           
alpha = 86 
coutMax=1    
confidenceMin=0.4
modelPath='yolov5/runs/train/exp10/weights/last.pt'
#modelPath='yolov5/runs/train/exp_960_8_150_m/weights/best_960_8_150_m'


repertoireGLOBAL= glob.glob('FRAMES/LEFT/*')+glob.glob('FRAMES/RIGHT/*')
repertoire=[]
for i in range(len(repertoireGLOBAL)):
    repertoire+=glob.glob(repertoireGLOBAL[i]+"/*")


results=ML.machineLearningIdentification(repertoire,modelPath)

profondeurImages = carToCrop.depth(repertoire,baseline,f,alpha,coutMax,confidenceMin,results)       


headerCrop = ['crop', 'latitude', 'longitude']
dataCrop = carToCrop.createDataCropCSV(repertoire,profondeurImages,results) 

headerVoiture = ['image', 'latitude', 'longitude']
dataVoiture = GPS.coordonneesGPSVoiture(profondeurImages,repertoire)

fileCrop='CSV/cropData.csv'
fileVoiture='CSV/carData.csv'


csvConverter.arrayToCSV(fileCrop,headerCrop,dataCrop)
csvConverter.arrayToCSV(fileVoiture,headerVoiture,dataVoiture)



