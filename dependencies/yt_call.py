import os

import googleapiclient.discovery

class YT_Call():
    def __init__(self, video_id):
        self.video_id = video_id
    
    def call(video_id):
        # Disable OAuthlib's HTTPS verification when running locally.
        # *DO NOT* leave this option enabled in production.
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        DEVELOPER_KEY = "AIzaSyA83OoEIerPAYRDe-hcotFENGP95-Ov_XA"

        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, developerKey = DEVELOPER_KEY)

        request = youtube.commentThreads().list(
            part="snippet",
            textFormat = 'plainText',
            maxResults = 1000,
            order = 'time',
            videoId= video_id
        )
        response = request.execute()
        return response
        print(f"{len(response)} Comments successfully retrieved.")
