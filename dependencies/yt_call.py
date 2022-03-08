import os
import googleapiclient.discovery

class YT_Call():
    def __init__(self, video_id):
        self.video_id = video_id
    
    def call(video_id, n_pages = 10, priority = 'time'):
        # Disable OAuthlib's HTTPS verification when running locally.
        # *DO NOT* leave this option enabled in production.
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        DEVELOPER_KEY = "AIzaSyA83OoEIerPAYRDe-hcotFENGP95-Ov_XA"

        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, developerKey = DEVELOPER_KEY)


        request = youtube.commentThreads().list(           
            part ="snippet",
            textFormat = 'plainText',
            maxResults = 1000,
            order = priority,
            videoId = video_id)

        i = 0

        response = dict([])
        response[i] = request.execute()

        npt = False
        if 'nextPageToken' in response[i]:
            npt = response[i]['nextPageToken']

        while npt:
            i = i+1
            print(i)
            request = youtube.commentThreads().list(
            part ="snippet",
            textFormat = 'plainText',
            maxResults = 1000,
            order = priority,
            videoId = video_id,
            pageToken = npt)
            response[i] = request.execute()
            if 'nextPageToken' in response[i]:
                npt = response[i]['nextPageToken']
            else:
                break
            if i > n_pages-1:
                break

        return response
