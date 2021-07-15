import os
import shutil
def cleanUp(folder):
  shutil.rmtree(folder[2::],ignore_errors=True) #To Delete All Downloaded Videos
  shutil.rmtree("__pycache__",ignore_errors=True) #To Delete Cache formed in the process
  if os.path.exists("output.mp4"):
    os.remove("output.mp4") #To Delete Final Video After Uploading

if __name__ == "__main__":
  cleanUp("./DownlodedVideos")