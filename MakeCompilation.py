from moviepy.editor import *
import os

def makeCompilation(path,intro,outro):  #Compiling Videos
    nameOfAllFiles = os.listdir(path)   #Storing Name Of All Downloaded Files/Videos In a List[]
    clips = []
    if intro!= "":  #Adding Intro Video
         clips.append(VideoFileClip(intro))
    for i in nameOfAllFiles:
        if i.endswith("mp4"):   #Checking If File Is mp4(video)
            clip = VideoFileClip(path+'\\'+i)
            clip = clip.resize(width=1920)  #Resizing Video Width
            clip = clip.resize(height=1080) #Resizing Video Height
            clips.append(clip)  #Adding Videos in a List[]
    if outro != "": #Adding Outro Video
        clips.append(VideoFileClip(outro))
    outputVideo = concatenate_videoclips(clips,method='compose')
    outputVideo.to_videofile("output.mp4",threads=8, remove_temp=True)  #Converting Everything Into Final Video

if __name__ == "__main__":
    makeCompilation("./DownlodedVideos","","")