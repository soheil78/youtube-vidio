```python
from googleapiclient.discovery import build

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

# استفاده از کلاس:
api_key = 'AIzaSyARvq-gK0G2bmA2DOIRvf9jny_Zt05Pcn0'  # جایگزین با API Key دریافتی از Google Cloud Console
scraper = YouTubeScraper(api_key)

# جستجوی ویدیوهای آموزشی مرتبط با "Python tutorials"
videos = scraper.search_videos('Python tutorials', max_results=5)

# نمایش ویدیوهای استخراج شده
if videos:
    for video in videos:
        print(f"Title: {video['title']}")
        print(f"Description: {video['description']}")
        print(f"Channel: {video['channel_title']}")
        print(f"Published at: {video['publish_time']}")
        print(f"Video URL: {video['video_url']}")
        print('-' * 50)
else:
    print("No videos found.")

import pandas as pd

# داده‌های مورد نظر برای ورود به اکسل
data = [
    {
        'Title': 'Python for Beginners - Learn Python in 1 Hour',
        'Description': 'Learn Python basics in 1 hour! ⚡ This beginner-friendly tutorial will get you coding fast. Want to dive deeper? Check out my ...',
        'Channel': 'Programming with Mosh',
        'Published at': '2020-09-16T13:00:20Z',
        'Video URL': 'https://www.youtube.com/watch?v=kqtD5dpn9C8'
    },
    {
        'Title': 'Python Tutorial - Python Full Course for Beginners',
        'Description': 'Become a Python pro! This comprehensive tutorial takes you from beginner to hero, covering the basics, machine learning, and ...',
        'Channel': 'Programming with Mosh',
        'Published at': '2019-02-18T15:00:08Z',
        'Video URL': 'https://www.youtube.com/watch?v=_uQrJ0TkZlc'
    },
    {
        'Title': 'Python Tutorial for Beginners (with mini-projects)',
        'Description': 'Learn Python programming in this complete course for beginners. This tutorial features mini-projects throughout so you can put ...',
        'Channel': 'freeCodeCamp.org',
        'Published at': '2023-09-19T14:33:56Z',
        'Video URL': 'https://www.youtube.com/watch?v=qwAFL1597eM'
    },
    {
        'Title': 'Learn Python in Less than 10 Minutes for Beginners (Fast & Easy)',
        'Description': "In this crash course I'll be teaching you the basics of Python in less than 10 minutes. Python is super easy to learn compared to ...",
        'Channel': 'Indently',
        'Published at': '2021-05-26T12:32:40Z',
        'Video URL': 'https://www.youtube.com/watch?v=fWjsdhR3z3c'
    },
    {
        'Title': 'Python Tutorial for Beginners - Learn Python in 5 Hours [FULL COURSE]',
        'Description': "Python Tutorial for Beginners | Full Python Course | Learn Python in 2023 The Ultimate IT Beginner's Course: ...",
        'Channel': 'TechWorld with Nana',
        'Published at': '2021-03-05T14:10:17Z',
        'Video URL': 'https://www.youtube.com/watch?v=t8pPdKYpowI'
    }
]

# ایجاد یک DataFrame از داده‌ها
df = pd.DataFrame(data)

# ذخیره DataFrame به فایل اکسل
df.to_excel('youtube_videos.xlsx', index=False)

print("Data has been successfully saved to 'youtube_videos.xlsx'")

```

    Title: Python for Beginners - Learn Python in 1 Hour
    Description: Learn Python basics in 1 hour! ⚡ This beginner-friendly tutorial will get you coding fast. Want to dive deeper? Check out my ...
    Channel: Programming with Mosh
    Published at: 2020-09-16T13:00:20Z
    Video URL: https://www.youtube.com/watch?v=kqtD5dpn9C8
    --------------------------------------------------
    Title: Python Tutorial - Python Full Course for Beginners
    Description: Become a Python pro! This comprehensive tutorial takes you from beginner to hero, covering the basics, machine learning, and ...
    Channel: Programming with Mosh
    Published at: 2019-02-18T15:00:08Z
    Video URL: https://www.youtube.com/watch?v=_uQrJ0TkZlc
    --------------------------------------------------
    Title: Python Tutorial for Beginners (with mini-projects)
    Description: Learn Python programming in this complete course for beginners. This tutorial features mini-projects throughout so you can put ...
    Channel: freeCodeCamp.org
    Published at: 2023-09-19T14:33:56Z
    Video URL: https://www.youtube.com/watch?v=qwAFL1597eM
    --------------------------------------------------
    Title: Learn Python in Less than 10 Minutes for Beginners (Fast &amp; Easy)
    Description: In this crash course I'll be teaching you the basics of Python in less than 10 minutes. Python is super easy to learn compared to ...
    Channel: Indently
    Published at: 2021-05-26T12:32:40Z
    Video URL: https://www.youtube.com/watch?v=fWjsdhR3z3c
    --------------------------------------------------
    Title: Python Tutorial for Beginners - Learn Python in 5 Hours [FULL COURSE]
    Description: Python Tutorial for Beginners | Full Python Course | Learn Python in 2023 The Ultimate IT Beginner's Course: ...
    Channel: TechWorld with Nana
    Published at: 2021-03-05T14:10:17Z
    Video URL: https://www.youtube.com/watch?v=t8pPdKYpowI
    --------------------------------------------------
    Data has been successfully saved to 'youtube_videos.xlsx'
    


```python
jupyter nbconvert --to markdown Untitled21.ipynb

```


      Cell In[8], line 1
        jupyter nbconvert --to markdown Untitled21.ipynb
                ^
    SyntaxError: invalid syntax
    



```python

```
