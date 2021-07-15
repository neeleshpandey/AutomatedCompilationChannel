# Automated Compilation Channel
###### This is a piece of code that downloads videos from instagram, compiles them and uploads that compiled video on YouTube 

## Instructions

1. [Download](https://github.com/neeleshpandey/AutomatedCompilationChannel/archive/refs/heads/master.zip) or Clone this Repository in your Local Environment

2. Download and install [`Python3`](https://www.python.org/downloads/) and [`pip`](https://pip.pypa.io/en/stable/installing/)

3. Install libraries with `pip3 install -r requirements.txt` or `python3 -m pip install -r requirements.txt`

4. Get setup and create a Project with the Youtube API: `https://developers.google.com/youtube/v3/quickstart/python` Be sure to follow it carefully, as it won't work if you don't do this part right. Download your OATH file as `client_secrets.json` in your project folder.

5. Create an instagram account and follow accounts you want to scrape from

6. Open `main.py` in a text editor and add path of intro and outro video (Optional)

7. Open `InstagramLoginInfo.py` in a text editor and fill in credentials

8. Open `UploadOnYoutube.py` and add `categoryId`,`title`,`description`,`tags`,etc.

9. Run `python3 main.py` and authenticate your account 

10. Enjoy Your Automated Compilation Youtube Channel
