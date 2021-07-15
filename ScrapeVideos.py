import instaloader
from instalooter.looters import InstaLooter, ProfileLooter
import datetime
import dateutil.relativedelta
import os

def scrapeVideos(username = "",
                 password = "",
                 downloadVideosIn = "./DownlodedVideos",
                 ):
                 
    if not os.path.exists(downloadVideosIn):
        os.makedirs(downloadVideosIn)   #Making a directory to Download
        
    print("Starting Scraping")

    L = instaloader.Instaloader()
    L.login(username, password) #This will Login to Your Account 
    profile = instaloader.Profile.from_username(L.context, username)
    following = profile.get_followees() #Getting your all your Following
    # for profile in following:
    #     print(profile.username)   #If You Want To See Your Following


    today = datetime.date.today()   #Todays Date
    timeframe = (today, today - dateutil.relativedelta.relativedelta(days=today.day-(today.day-7))) #A Week Before 
    #Generating a Timeline


    for profile in following:
            acc = profile.username
            looter = ProfileLooter(acc,videos_only=True)    #If You Want Photos Make videos_only=False
            if not looter.logged_in():
                looter.login(username, password)
            print("Scraping From Account: " + acc)
            try:
                numDowloaded = looter.download(downloadVideosIn,timeframe=timeframe)
                print("Downloaded " + str(numDowloaded) + " videos successfully")
                print("")   #Downloading Videos Account Wise
            except Exception as e:
                print("Skipped acc " + acc + "because of")
                print(e)
#You can Modify constraints according to your requirements

if __name__ == "__main__":
    scrapeVideos(username = "",
                 password = "")
