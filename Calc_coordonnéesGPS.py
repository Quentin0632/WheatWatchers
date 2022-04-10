import math
import numpy as np
import sys
from exif import Image
import copy

#Couple 1 : point GPS précédent
#Couple 2 : point GPS suivant

#######Calcul de distance en m entre deux points GPS
def calc_dist(La1,Long1,La2,Long2):
    R_Terre= 6378137 #Rayon de la terre en m
    x=math.sin(La1*np.pi/180)*math.sin(La2*np.pi/180)+math.cos(La1*np.pi/180)*math.cos(La2*np.pi/180)*math.cos((Long1-Long2)*np.pi/180)
    if(x<-1):
        return R_Terre*math.acos(-1)
    if(x>1):
        return R_Terre*math.acos(1)
    return R_Terre*math.acos(math.sin(La1*np.pi/180)*math.sin(La2*np.pi/180)+math.cos(La1*np.pi/180)*math.cos(La2*np.pi/180)*math.cos((Long1-Long2)*np.pi/180))


########Calcul de l'angle en radiant de direction entre les deux points GPS
def calc_direction(La1,Long1,La2,Long2):
    
    hyp=calc_dist(La1,Long1,La2,Long2)
    adj=calc_dist(La1,Long1,La1,Long2)
    if(abs(hyp)<sys.float_info.min):
        hyp=sys.float_info.min
        
    if(abs(adj/hyp)>1):
        if(adj>=0):
            return math.acos(1)
        math.acos(-1)
    
    return math.acos(adj/hyp)

#########Calcul des coordonnées du champ

# L :distance obtenue avec la stereo en m
def CoordChamp(latitude1,longitude1,latitude2,longitude2,L):

    R_Terre= 6378137 #Rayon de la terre en m
    
    deltaLat=latitude2-latitude1
    deltaLong=longitude2-longitude1
    
    #Calcul de l'angle de direction
    alpha=calc_direction(latitude1,longitude1,latitude2,longitude2)
    
    #Calcul des coordonnées du champ projetées par rapport au point actuel
    lat_proj=L*math.cos(alpha)
    long_proj=L*math.sin(alpha)
    
    theta_N=lat_proj*180/(np.pi*R_Terre)
    theta_E=long_proj*180/(np.pi*R_Terre)
    
    latitudeChamp=latitude2
    longitudeChamp=longitude2
    if(deltaLat>0 and deltaLong<0):
        latitudeChamp+= theta_N
        longitudeChamp+= theta_E
        
    if(deltaLat<0 and deltaLong>0):
        latitudeChamp-= theta_N
        longitudeChamp-= theta_E
        
    if(deltaLat<0 and deltaLong<0):
        latitudeChamp+= theta_N
        longitudeChamp-= theta_E
        
    if(deltaLat>0 and deltaLong>0):
        latitudeChamp-= theta_N
        longitudeChamp+= theta_E
        
    return latitudeChamp,longitudeChamp



def decimal_coords(coords):
 decimal_degrees = coords[0] + coords[1] / 60 + coords[2] / 3600
 return decimal_degrees


def image_coordinates(image_path):
    coords=0
    with open(image_path, 'rb') as src:
        img = Image(src)
    if img.has_exif:
        try:
            coords = (decimal_coords(img.gps_latitude),decimal_coords(img.gps_longitude))
        except AttributeError:
            print('No Coordinates')
    else:
        print('The Image has no EXIF information')
    return coords,img.datetime_original
  

def coordonneesGPSChamp1(profondeurImages,repertoire):
    listFinale=profondeurImages.copy()
    for i in range(len(profondeurImages)):
             imgL1=repertoire[i]
             imgL2=repertoire[i+1]
             coords1,time1=image_coordinates(imgL1)
             coords2,time2=image_coordinates(imgL2)
             for j in range(len(profondeurImages[0])):
                 listFinale[i][j][1]=CoordChamp(coords1[0],coords1[1],coords2[0],coords2[1],profondeurImages[i][j][1])
    return listFinale


def coordonneesGPSChamp(profondeurImages,repertoire):
    listFinale=copy.deepcopy(profondeurImages)
    for i in range(len(profondeurImages)):
             imgL1=repertoire[i]
             imgL2=repertoire[i+1]
             coords1,time1=image_coordinates(imgL1)
             coords2,time2=image_coordinates(imgL2)
             for j in range(len(profondeurImages[0])):
                 latitude,longitude=CoordChamp(coords1[0],coords1[1],coords2[0],coords2[1],profondeurImages[i][j][1])
                 listFinale[i][j][1]=latitude
                 listFinale[i][j]+=[longitude]
    return listFinale

def coordonneesGPSVoiture(profondeurImages,repertoire):
    voitureCoord=[]
    for i in range(len(profondeurImages)):
             imgL1=repertoire[i]
             imgL2=repertoire[i+1]
             coords1,time1=image_coordinates(imgL1)
             coords2,time2=image_coordinates(imgL2)
             voitureCoord+=[[imgL1,coords1[0],coords1[1]]]
    return voitureCoord
