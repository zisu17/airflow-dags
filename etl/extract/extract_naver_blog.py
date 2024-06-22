import datetime
import requests
import json
import pandas as pd


def extract_naver_blog(keyword_list, client_id, client_secret):
    for keyword in keyword_list:
        collect_count = 0
        drop_count = 0
        print('-' * 200)
        print('keyword :', keyword)

        url = 'https://openapi.naver.com/v1/search/blog.json'
        headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret}
        params = {'query': keyword,
                  'sort': 'date',
                  'display': 100}
        response = requests.get(url, headers=headers, params=params)
        rescode = response.status_code
        std_date = datetime.datetime.now().date()

        if (rescode == 200):
            data = json.loads(response.text)
            blog_items = data['items']
            blog_df = pd.DataFrame(blog_items, columns=['title', 'link', 'description', 'bloggername', 'postdate'])
            blog_df['postdate'] = pd.to_datetime(blog_df['postdate'])
            blog_df = blog_df[blog_df['postdate'].dt.date >= std_date]
        else:
            print("Error Code:" + rescode)

        for i in range(len(blog_df)):
            post_date_str = blog_df['postdate']
            postdate = datetime.strptime(post_date_str, "%Y%m%d")
            blog_name = blog_df['bloggername'][i]
            url = blog_df['link'][i]
