"""
transform a video into a succession of photos while keeping the GPS * information on each image created in the metadata
"""
import os
import shutil


root_vid_directory = "VIDEO"
frameRate=0.1

dir = 'FRAMES/RIGHT'
for f in os.listdir(dir):
    shutil.rmtree(os.path.join(dir, f))
    
dir = 'FRAMES/LEFT'
for f in os.listdir(dir):
    shutil.rmtree(os.path.join(dir, f))

dir = 'VIDEO/RIGHT'
for f in os.listdir(dir):
    if not f.endswith("MP4"):
        os.remove(os.path.join(dir, f))
        
dir = 'VIDEO/LEFT'
for f in os.listdir(dir):
    if not f.endswith("MP4"):
        os.remove(os.path.join(dir, f))

for path, directories, files in os.walk(root_vid_directory):
    print(files)
    for video_file in files:
        if video_file.endswith("MP4"):
            print(video_file)
            full_mp4_path = os.path.join(path, video_file)
            print(full_mp4_path)
            os.system('cmd /k "exiftool -ProjectionType=equirectangular '+full_mp4_path)
            print("PATH TO FRAMES : "+"FRAMES/RIGHT/"+video_file[:-4])
            if(path=="VIDEO\RIGHT"):
                dir = "FRAMES/RIGHT/"+video_file[:-4]
                os.system('cmd /k "python gf2gv.py -e exiftool.exe -f ffmpeg.exe -r '+str(frameRate)+' '+ full_mp4_path+' '+dir)
            if(path=="VIDEO\LEFT"):
                dir = "FRAMES/LEFT/"+video_file[:-4]
                os.system('cmd /k "python gf2gv.py -e exiftool.exe -f ffmpeg.exe -r '+str(frameRate)+' '+ full_mp4_path+' '+dir)


    