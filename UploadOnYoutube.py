from Google import Create_Service
from googleapiclient.http import MediaFileUpload

CLIENT_SECRET_FILE = 'client_secrets.json'  #API File Add Here(client Secret File)
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

def uploadOnYoutube():  #Video Uploading Function
    service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

    request_body={
        'snippet':{
            'categoryId':23,    #Add Category Code(Type of video[Example: 23 is for Comedy])
            'title':'', #Add Title Of Your Youtube Video
            'description':'',   #Add Description Of Your Youtube Video
            'tags':[]   #Add Tags
        },
        'status':{
            'privacyStatus':'public',       #Add Privacy Status ["public","private","unlisted"]
            'selfDeclaredMadeForKids': False
        },
    'notifySubscribers': False
    }

    mediaFile = MediaFileUpload('.\output.mp4') #Selecting File(video) Which Is To Be Uploded

    response_upload = service.videos().insert(
        part='snippet,status',
        body=request_body,
        media_body=mediaFile
    ).execute()

if __name__ == "__main__":
    uploadOnYoutube()