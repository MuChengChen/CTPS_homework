# -*- coding: utf-8 -*-
import json
from requests import request
import urllib.request, csv

from ExampleData import department_table  # 系所代號對照資料Dictionary
from ExampleData import route_table  # 入學管道代號對照資料Dictionary
import json
import urllib.request, csv

# Global variable
student_data = dict()


def HW2(text, user_id):
    department = '尚未實作'
    route = '尚未實作'

    return '您的系所是 ' + department + ' ，入學管道是 ' + route, student_data


def HW3_1(text, user_id):
    reply = '尚未實作'

    return reply


def HW3_2():
    url = 'https://data.nhi.gov.tw/resource/mask/maskdata.csv'
    webpage = urllib.request.urlopen(url)
    data = csv.DictReader(webpage.read().decode('utf-8-sig').splitlines())

    return data


def HW3_3(text, maskdata):
    reply = '尚未實作'

    return reply


def HW3_4(text, maskdata):  # text = '地區:臺南市剩下多少兒童口罩'
    reply = '尚未實作'
    return reply


def HW4_1(text, user_id):
    reply = '請完成HW4-1'

    return reply


def HW4_2(user_id):
    url = 'https://playlab.computing.ncku.edu.tw:8000/homework-record/1/json'  # 作業繳交紀錄 url
    homework_record = json.loads(request('GET', url).text)

    reply = '還沒完成作業，加油加油 (๑´ㅂ`๑)'
    return reply


def HW4_3(text, user_id):

    reply = '還沒完成作業，加油加油 (๑´ㅂ`๑)'

    return reply


if __name__ == '__main__':
    print(HW4_1(text='請在每週四的12時提醒我作業進度', user_id='your user_id'))
    print(HW4_2(user_id='your user_id'))
    print(HW4_3(text='請問全班有幾位同學拿到excellent的成績', user_id='your user_id'))
