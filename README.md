[![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](LICENSE.md)
[![](https://badgen.net/badge/API/Youtube/red?icon=instgrame)]()



## Table of Contents

<table>
  <tr>
    <td style="vertical-align: top;">
      <ul>
        <li><a href="#elbm-coclust-and-selbm-coclust">ELBMcoclust and SELBMcoclust</a></li>
        <li><a href="#datasets">Datasets</a></li>
        <li><a href="#Implement">Implement</a></li>
        <li><a href="#visualization">Visualization</a></li>
        <li><a href="#word-cloud-of-poissonselbm-for-classic3">Word Cloud of PoissonSELBM for Classic3</a></li>
	<li><a href="#contributions">Contributions</a></li>
        <li><a href="#highlights">Highlights</a></li>
        <li><a href="#supplementary-materials">Supplementary Materials</a></li>
        <li><a href="#data-availability">Data Availability</a></li>
	<li><a href="#cite">Cite</a></li>
        <li><a href="#references">References</a></li>
      </ul>
    </td>
    <td>
      <img src="https://github.com/Saeidhoseinipour/ELBMcoclust/blob/main/Images/WC_classic3_three_color_3_3.svg" alt="Saeid Hoseinipour" style="width:250px; box-shadow: 5px 5px 15px rgba(0,0,0,0.3); transform: rotateY(10deg);">
    </td>
    <td>
      <img src="https://github.com/Saeidhoseinipour/ELBMcoclust/blob/main/Images/bar_chart_words_classic3_V4_3_3.svg" alt="Saeid Hoseinipour" style="width:200px; box-shadow: 5px 5px 15px rgba(0,0,0,0.3); transform: rotateY(-10deg);">
    </td>
  </tr>
</table>


```python
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
```

```python
------------------------------------------------------------------------------------------------------------------------------------------
answer
-----------------------------------------------------------------------------------------------------------------------------------------
Processing video: Python for Beginners - Learn Python in 1 Hour
Processing video: Python Tutorial - Python Full Course for Beginners
Processing video: Python Tutorial for Beginners (with mini-projects)
Processing video: Python Tutorial for Beginners - Learn Python in 5 Hours [FULL COURSE]
Processing video: Learn Python in Less than 10 Minutes for Beginners (Fast &amp; Easy)
Data has been successfully saved to 'youtube_videos_with_speech_text.xlsx'

Videos Output:
--------------------------------------------------
Title: Python for Beginners - Learn Python in 1 Hour
Description: Learn Python basics in 1 hour! ⚡ Get 6 months of PyCharm FREE with the coupon in the description! Want to dive deeper?
Channel: Programming with Mosh
Published at: 2020-09-16T13:00:20Z
Video URL: https://www.youtube.com/watch?v=kqtD5dpn9C8
Transcript: خطا در استخراج متن: 
Could not retrieve a transcript for the video https://www.youtube.com/watch?v=kqtD5dpn9C8! This is most likely caused by:

Subtitles are disabled for this video

If you are sure that the described cause is not responsible for this error and that a transcript should be retrievabl...
--------------------------------------------------
Title: Python Tutorial - Python Full Course for Beginners
Description: Learn Python for machine learning and web development! Get 6 months of PyCharm FREE with the coupon in the description!
Channel: Programming with Mosh
Published at: 2019-02-18T15:00:08Z
Video URL: https://www.youtube.com/watch?v=_uQrJ0TkZlc
Transcript: خطا در استخراج متن: 
Could not retrieve a transcript for the video https://www.youtube.com/watch?v=_uQrJ0TkZlc! This is most likely caused by:

Subtitles are disabled for this video

If you are sure that the described cause is not responsible for this error and that a transcript should be retrievabl...
--------------------------------------------------
Title: Python Tutorial for Beginners (with mini-projects)
Description: Learn Python programming in this complete course for beginners. This tutorial features mini-projects throughout so you can put ...
Channel: freeCodeCamp.org
Published at: 2023-09-19T14:33:56Z
Video URL: https://www.youtube.com/watch?v=qwAFL1597eM
Transcript: خطا در استخراج متن: 
Could not retrieve a transcript for the video https://www.youtube.com/watch?v=qwAFL1597eM! This is most likely caused by:

Subtitles are disabled for this video

If you are sure that the described cause is not responsible for this error and that a transcript should be retrievabl...
--------------------------------------------------
Title: Python Tutorial for Beginners - Learn Python in 5 Hours [FULL COURSE]
Description: Python Tutorial for Beginners | Full Python Course | Learn Python in 2023 The Ultimate IT Beginner's Course: ...
Channel: TechWorld with Nana
Published at: 2021-03-05T14:10:17Z
Video URL: https://www.youtube.com/watch?v=t8pPdKYpowI
Transcript: خطا در استخراج متن: 
Could not retrieve a transcript for the video https://www.youtube.com/watch?v=t8pPdKYpowI! This is most likely caused by:

Subtitles are disabled for this video

If you are sure that the described cause is not responsible for this error and that a transcript should be retrievabl...
--------------------------------------------------
Title: Learn Python in Less than 10 Minutes for Beginners (Fast &amp; Easy)
Description: In this crash course I'll be teaching you the basics of Python in less than 10 minutes. Python is super easy to learn compared to ...
Channel: Indently
Published at: 2021-05-26T12:32:40Z
Video URL: https://www.youtube.com/watch?v=fWjsdhR3z3c
Transcript: خطا در استخراج متن: 
Could not retrieve a transcript for the video https://www.youtube.com/watch?v=fWjsdhR3z3c! This is most likely caused by:

Subtitles are disabled for this video

If you are sure that the described cause is not responsible for this error and that a transcript should be retrievabl...
--------------------------------------------------
```
