![](https://codimd.s3.shivering-isles.com/demo/uploads/upload_d4509ad99b8a6347c33ce990f67a7571.jpg)

# Facebook API
新增 新的function   用來讓同學知道哪幾天的dataset是不會有問題的  詳細說明請下滑 有詳細說明
```python=
get_fine_dataset_date()
```
##BUG note
- 10/21~10/26 這段期間 的dataset 皆沒有問題

- 11/10~11/12 資料皆沒有問題

- 9/29~10/21 dataset FB名子 id 為 英文者

id可能有殘缺 舉例
Nicolas Hei dataset 的id 為Nicolas

- 10/27~11/09  reaction 相關資料會有錯誤先不要抓取

## Insallation
- 移動到你要工作的資料夾打開 git bash
```shell=
$ git clone https://playlab.computing.ncku.edu.tw:4001/khduh/facebook_api_file.git
```
***

![](https://codimd.s3.shivering-isles.com/demo/uploads/upload_147003c5e7b1df138f1de6c93df821eb.png)
- **package you need to install**
    - google-api-python-client
    - oauth2client


***
![](https://codimd.s3.shivering-isles.com/demo/uploads/upload_5c367b466f7ab106e09427d45ea300ce.png)


***
- **設定引用library**

![](https://codimd.s3.shivering-isles.com/demo/uploads/upload_e0ae3a01768edf468a5ab44a89e60b35.png)


- **測試**

***

![](https://codimd.s3.shivering-isles.com/demo/uploads/upload_036fd11dbee4868765c1fc8514fbda0a.png)

***


![](https://codimd.s3.shivering-isles.com/demo/uploads/upload_2b327297eea4f1474d74cc4233ca6764.png)




## Function List
## 建議事項
- **若你對json檔格式熟悉者 僅須使用第一個函示庫 即可得到社團上的參與度資料檔 並自行分析得到自己想要的資訊**
- **若你對如何處理資料不太熟悉 可以參考API中函式庫提取資訊的寫法 這樣對日後的project想要提取自己想要的資訊 EMOJI COMMENT CONTENT.......會有較大的幫助**
***
### 1. **function 說明 : 下載google cloud 上的 json檔 到本機電腦**
- 引數 date 輸入日期可以得到對應日期的社團資訊 從 9/29 開始皆有檔案 輸入格式參考如下
```python=
get_json_from_cloud(date)
```
- **範例 取10/21 社團資訊**
```python=
dataset=get_json_from_cloud(date="1021")
```
- >**回傳 一個DICT 的dataset**
- >**dict的架構如下**
```python=
{
	'post_info':[{
                       'post_id':''
			'poster': '',
			'post_content': '',
			'post_share_link': [],
			'comment_number': '',
			'reaction':[{'emoji_id': '',
					  'emoji_type': ''
					  }],
			'comment':[{
						'comment_id': '',
						'comment_content': '',
						'comment_link_num': '',
						'comment_gif_num': '',
						'comment_img_num': '',
						'comment_sticker': '',
						'comment_below':[{'comment_id':'',
											  'comment_content':'',
											  'comment_link_num':'',
											  'comment_gif_num':'',
											  'comment_img_num':'',
											  'comment_sticker':'',
											  'comment_reaction':[{'emoji_id': '',  'emoji_type': '' }]}]}],
			
					  
						'comment_reaction': [{'emoji_id': '', 'emoji_type': ''  }],
				}]
	'member_info'=[],
        'announcement_info'=[{
			'poster': '',
			'post_content': '',
			'post_share_link': [],
			'comment_number': '',
			'reaction':[{'emoji_id': '',
					  'emoji_type': ''
					  }],
			'comment':[{
						'comment_id': '',
						'comment_content': '',
						'comment_link_num': '',
						'comment_gif_num': '',
						'comment_img_num': '',
						'comment_sticker': '',
						'comment_below':[comment_below_dict = {'comment_id':'',
											  'comment_content':'',
											  'comment_link_num':'',
											  'comment_gif_num':'',
											  'comment_img_num':'',
											  'comment_sticker':'',
											  'comment_reaction':[emoji_dict ={'emoji_id': '',  'emoji_type': '' }]}]}],
			
					  
						'comment_reaction': [{'emoji_id': '', 'emoji_type': ''  }]
				}]
}

```

***

### 2. **function 說明 : 得到社團內成員清單**
- > **回傳一LIST**
```python=
get_all_user_ids(dataset):
```
- >**使用範例**
```
dataset = get_json_from_cloud(date='1021')
userid_list=get_all_user_ids(dataset)
print(userid_list)
```

***


### 3. **function 說明 : 回傳對應postid貼文資訊**
- > ***回傳 一個 dict 為 PO 文資訊***   
```python=
get_posts_by_post_id(dataset,post_id)
```
- >**使用範例  回傳POSTID=2的PO文資訊**
```python=
dataset = get_json_from_cloud(date='1021')
single_post_info=get_posts_by_post_id(dataset=dataset,post_id=2)
print(single_post_info)
```

***


### 4. **function 說明 : 回傳對應post type貼文資訊**
- > **回傳 一個list 的PO 文資訊**
- > 依據使用者輸入的type 搜索對應的PO文
- type 可更改為下列選項:
    - HW Submission
    - Class Discussion
    - In-Class Test
    - Q&A_Lecture
    - Teacher Announcement
    - TA Announcement
    - Joint Note
    - Voting Announcement
    - Reference
```python=
get_all_posts_by_type(dataset,type)
```
- >**使用範例  回傳 post-type 為 Q&A 的PO文資訊*
```python=
dataset = get_json_from_cloud(date='1021')
post_list=get_all_posts_by_type(dataset=dataset,type='Q&A')
print(post_list)
```
***

### 5. **function 說明 : 回傳postid對應PO文下的主留言資訊**
- > **回傳一個LIST**

```python=
main_comment=get_all_main_comments_by_post_id_user_id(dataset, post_id,user_id)
```
- >**使用範例**
```python=
dataset = get_json_from_cloud(date='1021')
comment_list=get_all_main_comments_by_post_id_user_id(dataset=dataset,post_id=1,user_id='Nicolas Hei')
print(comment_list)
```

***
### 6. **function 說明 : 回傳postid對應PO文下的 主留言下的留言 資訊**
- > **回傳一個LIST**
```python=
get_all_below_comments_by_post_id_user_id(dataset, post_id,user_id)
```
- >**使用範例**
```python=
dataset = get_json_from_cloud(date='1021')
comment_list=get_all_below_comments_by_post_id_user_id(dataset=dataset, post_id=1, user_id='Nicolas Hei')
print(comment_list)
```

***
### 7. **function 說明 : 回傳post id 對應 PO文下的 表情符號資訊 資訊**
- > **回傳一個LIST**
```python=
get_post_emojis_by_post_id(dataset,post_id)
```
- >**使用範例**
```python=
dataset = get_json_from_cloud(date='1021')
emoji_list=get_post_emojis_by_post_id(dataset=dataset,post_id=1)
print(emoji_list)
```
***
### 8. **function 說明 : 回傳 userid 在社團貼文按表情符號資訊 資訊**
- > **回傳一個DICT**
```python=
get_all_posts_emojis_times_by_user_id(dataset,user_id)
```
- >**使用範例**
```python=
dataset = get_json_from_cloud(date='1021')
user_emojitimes=get_all_posts_emojis_times_by_user_id(dataset=dataset,user_id='Nicolas Hei')
print(user_emojitimes)
```
***
### 9. **function 說明 : 回傳 所有 userid 在社團貼文留言次數 資訊**
- > **回傳一個DICT**
```python=
get_all_posts_all_user_comments_times(dataset=dataset)
```
- >**使用範例**
```python=
dataset = get_json_from_cloud(date='1021')
data = get_all_posts_all_user_comments_times(dataset=dataset)
print(data)
```
***
### 10. **function 說明 : 回傳 userid 在社團按表情符號次數 資訊**
- > **回傳一個DICT**
```python=
get_user_emoji_times_by_user_id(dataset,user_id)
```
- >**使用範例**
```python=
dataset = get_json_from_cloud(date='1021')
allemojitimes=get_user_emoji_times_by_user_id(dataset=dataset,user_id='高士鈞')
print(allemojitimes)
```
***
### 11. **function 說明 : 回傳正確無誤的dataset日期**
- > **回傳一個LIST**
```python=
get_fine_dataset_date()
```
- >**使用範例**
```python=
date_list=get_fine_dataset_date()
print(date_list)
```
***













