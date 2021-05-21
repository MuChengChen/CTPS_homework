#coding=utf-8

import json
import download as d
import os
import re
from collections import Counter
# for dataset before 1020 you can use show function to list the post id
def get_json_from_cloud(date):
	d.main(is_download_file_function=bool(True), download_drive_service_name=(date+'.json'), download_file_path=os.getcwd() + '/')
	with open((date+'.json'), 'r', encoding='utf-8') as f:
		dataset = json.load(f)
	return dataset

def get_all_user_ids(dataset):
	return dataset['member_info']

def get_posts_by_post_id(dataset, post_id):
	return dataset['post_info'][post_id]

def get_all_posts_by_type(dataset,type):
	match_list=[]
	if type=='Q&A':
		pattern = '\[ Q&amp;A'
	else:
		pattern='\[ '+type
	# pattern=r'{}'.format(label)
	for single_post in dataset['post_info']:
		search_standard=re.match(pattern,str(single_post['post_content']))
		if (search_standard!=None):
			match_list.append(single_post)
			pass
	return match_list

def get_all_main_comments_by_post_id_user_id(dataset, post_id,user_id):
	match_list=[single_comment for single_comment in dataset['post_info'][post_id]['comment'] if single_comment['comment_id']==user_id]
	return match_list

def get_all_below_comments_by_post_id_user_id(dataset, post_id,user_id):
	match_list=[]
	for single_comment in dataset['post_info'][post_id]['comment']:
		match_list=match_list+[single_below_comment for single_below_comment in single_comment['comment_below'] if single_below_comment['comment_id']==user_id]
	return match_list

def get_post_emojis_by_post_id(dataset,post_id):
	return dataset['post_info'][post_id]['reaction']


def get_all_posts_emojis_times_by_user_id(dataset,user_id):
	allemoji_list=[]
	for single_post in dataset['post_info']:
		allemoji_list=allemoji_list+[single_emoji['emoji_type']  for single_emoji in single_post['reaction']if single_emoji['emoji_id']==user_id]
	return Counter(allemoji_list)

def get_all_posts_all_user_comments_times(dataset):
	comment_list1=[]
	comment_list2=[]
	for single_post in dataset['post_info']:
		comment_list1=comment_list1+[singlecomment['comment_id']for singlecomment in single_post['comment']]

	for single_post in dataset['post_info']:
		for singlecomment in single_post['comment']:
			comment_list2=comment_list2+[singlecommentbelow['comment_id'] for singlecommentbelow in singlecomment['comment_below']]

	return Counter(comment_list1+comment_list2)

def get_user_emoji_times_by_user_id(dataset,user_id):
	allemoji_list=[]
	allemoji_list2 = []
	allemoji_list3 = []
	# 主PO文
	for single_post in dataset['post_info']:
		allemoji_list=allemoji_list+[single_emoji['emoji_type']  for single_emoji in single_post['reaction']if single_emoji['emoji_id']==user_id]
	# 主留言
	for single_post in dataset['post_info']:
		for singlecomment in single_post['comment']:
			allemoji_list2=allemoji_list2+[singleemoji['emoji_type'] for singleemoji in singlecomment['comment_reaction'] if singleemoji['emoji_id']==user_id]
	# 留言下的留言
	for single_post in dataset['post_info']:
		for singlecomment in single_post['comment']:
			for singlecommentbelow in singlecomment['comment_below']:
				allemoji_list3 = allemoji_list3+[singleemojibelow['emoji_type'] for singleemojibelow in singlecommentbelow['comment_reaction'] if singleemojibelow['emoji_id'] == user_id]
	return Counter(allemoji_list+allemoji_list2+allemoji_list3)
def get_fine_dataset_date():
	d.main(is_download_file_function=bool(True), download_drive_service_name=('fine_dataset.json'), download_file_path=os.getcwd() + '/')
	with open(('fine_dataset.json'), 'r', encoding='utf-8') as f:
		date_list = json.load(f)
	# date_list=['1021','1022','1023','1024','1025','1026','1027','1110','1011','1012']
	return date_list





if __name__ == '__main__':
	# with open(('1021' + '.json'), 'r', encoding='utf-8') as f:
	# 	dataset = json.load(f)
	dataset = get_json_from_cloud(date='1021')
	# single_post_info = get_posts_by_post_id(dataset=dataset, post_id=2)
	# print(single_post_info)
	# userid_list = get_all_user_ids(dataset)
	# print(userid_list)
	# post_list = get_all_posts_by_type(dataset=dataset, type='Q&A')
	# print(post_list)
	# comment_list = get_all_main_comments_by_post_id_user_id(dataset=dataset, post_id=1, user_id='Nicolas Hei')
	# print(comment_list)
	# emoji_list = get_post_emojis_by_post_id(dataset=dataset, post_id=1)
	# print(emoji_list)
	# user_emojitimes = get_all_posts_emojis_times_by_user_id(dataset=dataset, user_id='Nicolas Hei')
	# print(user_emojitimes)
	# data = get_all_posts_all_user_comments_times(dataset=dataset)
	# print(data)
	# allemojitimes = get_user_emoji_times_by_user_id(dataset=dataset, user_id='高士鈞')
	# print(allemojitimes)
