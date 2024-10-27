from googleapiclient.discovery import build
try:
    from youtube_transcript_api import YouTubeTranscriptApi
except ModuleNotFoundError:
    print("Module 'youtube_transcript_api' not found. Please install it using: pip install youtube-transcript-api")
    exit()
import pandas as pd

class YouTubeScraper:
    def __init__(self, api_key):
        self.api_key = api_key
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)

    def search_videos(self, query, max_results=5):
        """جستجوی ویدیوهای آموزشی در یوتیوب."""
        request = self.youtube.search().list(
            part='snippet',
            q=query,
            type='video',
            maxResults=max_results
        )
        response = request.execute()

        videos = []
        for item in response['items']:
            video_data = {
                'title': item['snippet']['title'],
                'description': item['snippet']['description'],
                'video_id': item['id']['videoId'],
                'channel_title': item['snippet']['channelTitle'],
                'publish_time': item['snippet']['publishedAt'],
                'video_url': f"https://www.youtube.com/watch?v={item['id']['videoId']}"
            }
            videos.append(video_data)

        return videos

    def get_transcript(self, video_id):
        """استخراج متن گفتاری از ویدیو با استفاده از YouTube Transcript API."""
        try:
            transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
            transcript_text = " ".join([entry['text'] for entry in transcript_list])
            return transcript_text
        except Exception as e:
            return f"خطا در استخراج متن: {e}"

# استفاده از کلاس:
if __name__ == "__main__":
    api_key = 'AIzaSyARvq-gK0G2bmA2DOIRvf9jny_Zt05Pcn0'  # جایگزین با API Key دریافتی از Google Cloud Console
    scraper = YouTubeScraper(api_key)

    # جستجوی ویدیوهای آموزشی مرتبط با "Python tutorials"
    videos = scraper.search_videos('Python tutorials', max_results=5)

    # نمایش ویدیوهای استخراج شده و تبدیل به متن گفتاری
    if videos:
        video_results = []

        for video in videos:
            print(f"Processing video: {video['title']}")

            # استخراج متن گفتاری از ویدیو با استفاده از YouTube Transcript API
            transcript = scraper.get_transcript(video['video_id'])

            # اضافه کردن متن به ویدیو
            video['transcript'] = transcript
            video_results.append(video)

        # ایجاد یک DataFrame از داده‌ها
        df = pd.DataFrame(video_results)

        # ذخیره DataFrame به فایل اکسل
        df.to_excel('youtube_videos_with_speech_text.xlsx', index=False)

        # چاپ اطلاعات ویدیوها به فرمت مشخص شده
        print("Data has been successfully saved to 'youtube_videos_with_speech_text.xlsx'")
        print("\nVideos Output:")
        print("--------------------------------------------------")

        for video in video_results:
            print(f"Title: {video['title']}")
            print(f"Description: {video['description']}")
            print(f"Channel: {video['channel_title']}")
            print(f"Published at: {video['publish_time']}")
            print(f"Video URL: {video['video_url']}")
            print(f"Transcript: {video['transcript'][:300]}...")  # نمایش بخشی از متن برای جلوگیری از طولانی شدن خروجی
            print('-' * 50)
    else:
        print("No videos found.")
