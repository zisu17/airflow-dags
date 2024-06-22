from googleapiclient.discovery import build

def extract_youtube_url(api_key, query):
    youtube_api_service_name = "youtube"
    youtube_api_version = "v3"
    youtube = build(youtube_api_service_name, youtube_api_version,
                    developerKey=api_key)

    request = youtube.search().list(
        part="snippet",
        order="date",
        q=query,
        regionCode="kr",
        maxResults=50
    )
    response = request.execute()
    return response
