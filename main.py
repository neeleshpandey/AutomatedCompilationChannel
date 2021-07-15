from CleanUp import cleanUp
from ScrapeVideos import scrapeVideos
from MakeCompilation import makeCompilation
from UploadOnYoutube import uploadOnYoutube
from CleanUp import cleanUp
import InstagramLoginInfo


PATH_OF_VIDEOS = "./DownlodedVideos" #Enter The Folder Where You Want To Download Videos
INTRO_VIDEO = "" #Enter The Path Of Intro Video(If You Want)
OUTRO_VIDEO = "" #Enter The Path Of Outro Video(If You Want)

#Step 1:Scrapping Videos From Instagram
print("\nStep 1: Scrapping Videos\n")
scrapeVideos(username = InstagramLoginInfo.InstagramId,
            password = InstagramLoginInfo.InstagramPassword,
            downloadVideosIn = PATH_OF_VIDEOS)
print("\nStep 1 Complete\n")


#Step 2: Make Compilation
print("\nStep 2: Compiling Videos\n")
makeCompilation(path = PATH_OF_VIDEOS, 
                intro = INTRO_VIDEO, 
                outro = OUTRO_VIDEO)
print("\nStep 2 complete\n")

#Step 3: Upload Videos On Youtube
print("\nStep 3: Uploading Output Video On Youtube\n")
uploadOnYoutube()
print("\nStep 3 complete\n")


#Step 4: Clean Up
print("\nStep 4: Cleaning Up The Memory\n")
cleanUp(folder = PATH_OF_VIDEOS)
print("\nStep 4 complete\n")


print("MISSION ACCOMPLISHED")