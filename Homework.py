import json
import urllib.request, csv

from ExampleData import department_table
from ExampleData import route_table

# Global variable
student_data = dict()


def HW2(text, user_id):  # text => 接收到的訊息字串;   user_id => User的Line ID

    student_data = dict()  # 學生資料
    # department = '尚未實作'   # 學號對應的系所
    # route = '尚未實作'  # 入學管道

    ### 請在下方完成作業功能的程式碼 ###
    ID = {'name': text.split(":")[1].split("/")[0], 'user_id': user_id}
    student_data[(text.split(":")[2])] = ID

    department = department_table.get((text.split(":")[2])[0:2])  # 學號對應的系所
    route = route_table.get((text.split(":")[2])[5:6])  # 入學管道

    if (department == None):
        return ('找不到這個系所', student_data)
    else:
        return ('您的系所是 ' + department + ' ，入學管道是 ' + route, student_data)


def HW3_1(text, user_id):  # text => 接收到的訊息字串(Ex. '姓名:王曉明/學號:A01234567');   user_id => User的Line系統ID

    url = 'https://playlab.computing.ncku.edu.tw:8000/student-list/1/csv'  # CTPS 2021 Spring 修課名單下載連結
    webpage = urllib.request.urlopen(url)
    data = csv.DictReader(webpage.read().decode('utf-8-sig').splitlines())  # 下載的修課名單
    # Hint: 可試著透過 print() 觀察 data 的型態，以判斷如何操作喔

    RegisteredData_path = './registered_data.json'  # 已註冊資料儲存位置
    # reply = '尚未實作'  # 回覆的訊息

    # Todo:
    # 1. 判斷傳入訊息的姓名、學號是否存在於修課名單，不存在則回覆 '使用者資料錯誤，請重新輸入，謝謝！'
    # 2. 倘若該user_id已註冊，回覆 '您已經註冊過囉！'
    # 3. 將使用者的資訊依下列格式的 dictionary 存放至 registered_data.json，並回覆 '註冊成功！'
    # {
    #     user_id: {
    #         "Name": name,
    #         "Student_ID": student_id,
    #     }
    # }

    ### 請在下方完成作業功能的程式碼 ###
    with open(RegisteredData_path, 'r', encoding="utf-8-sig") as file:

        register = json.load(file)

    name = text.split(":")[1].split("/")[0]
    ID = text.split(":")[2]
    user = {}
    for i in data:
        if name not in i['姓名'] or ID not in i['學號']:
            reply = '使用者資料錯誤，請重新輸入，謝謝！'
        elif name == i['姓名'] and ID == i['學號'] and user_id in register:
            reply = '您已經註冊過囉！'
            break
        elif name == i['姓名'] and ID == i['學號'] and user_id not in register:
            with open(RegisteredData_path, 'w', encoding="utf-8-sig") as file:
                userdic = {user_id: {'Name': name, 'Student_ID': ID}}
                user.update(userdic)
                json.dump(user, file, indent=2)
                reply = '註冊成功！'
                break
        elif name != i['姓名'] or ID != i['學號']:
            continue

    ### 請在上方完成作業功能的程式碼 ###

    return reply


def HW3_2():
    url = 'https://data.nhi.gov.tw/resource/mask/maskdata.csv'  # 衛服部口罩存量即時資料下載連結

    # Todo: 自 url 位址下載口罩存量即時資料，解讀為csv並放入data

    webpage = urllib.request.urlopen(url)  # 開啟網頁
    data = csv.DictReader(webpage.read().decode('utf-8-sig').splitlines())  # 讀取資料到data陣列中
    return data


def HW3_3(text, maskdata):  # text => 接收到的訊息字串(Ex. '機構:臺南市東區衛生所剩下多少成人口罩');    maskdata => 已下載的口罩存量資料

    # reply = 'HW3-3未完成，加油唷(❁´◡`❁)'

    # Todo:
    # 1. 若類型輸入錯誤，回覆 '口罩類型輸入錯誤！'
    # 2. 若機構名稱不存在，回覆 '醫事機構不存在！'
    # 3. 若該機構仍存有口罩，回覆 '還有XX個'
    # 4. 若該機構已無口罩，回覆 '已經銷售一空了！'

    ### 請在下方完成作業功能的程式碼 ###
    for i in maskdata:
        if text.split(":")[1].split("剩")[0] == i['醫事機構名稱'] and text.split("少")[1] == "成人口罩" and i['成人口罩剩餘數'] == 0:
            reply = "已經銷售一空了！"
            break
        elif text.split(":")[1].split("剩")[0] == i['醫事機構名稱'] and text.split("少")[1] == "兒童口罩" and i['兒童口罩剩餘數'] == 0:
            reply = "已經銷售一空了！"
            break
        elif text.split(":")[1].split("剩")[0] == i['醫事機構名稱'] and text.split("少")[1] == "成人口罩":
            reply = "還有{}個".format(i['成人口罩剩餘數'])
            break
        elif text.split(":")[1].split("剩")[0] == i['醫事機構名稱'] and text.split("少")[1] == "兒童口罩":
            reply = "還有{}個".format(i['兒童口罩剩餘數'])
            break
        elif text.split("少")[1] != "成人口罩" and text.split("少")[1] != "兒童口罩":
            reply = "口罩類型輸入錯誤！"
        elif text.split(":")[1].split("剩")[0] != i['醫事機構名稱']:
            continue
    else:
        reply = i['醫事機構名稱']

    ### 請在上方完成作業功能的程式碼 ###

    return reply


def HW3_4(text, maskdata):  # text => 接收到的訊息字串(Ex. '地區:臺南市剩下多少兒童口罩');  maskdata => 已下載的口罩存量資料

    # reply = 'HW3-4未完成，加油唷(❁´◡`❁)'

    # Todo:
    # 1. 若類型輸入錯誤，回覆 '口罩類型輸入錯誤！'
    # 2. 若地區名稱不存在，回覆 '醫事機構不存在！'
    # 3. 若該地區仍存有口罩，回覆 '還有XX個'
    # 4. 若該地區已無口罩，回覆 '已經銷售一空了！'

    ### 請在下方完成作業功能的程式碼 ###
    region = text.split(":")[1].split("剩")[0]
    kind = text.split("少")[1].split("口")[0]
    amount = 0
    for i in maskdata:
        if region == i['醫事機構地址'][0:3] and kind == '成人':
            amount += int(i['成人口罩剩餘數'])
            continue
        if region == i['醫事機構地址'][0:3] and kind == '兒童':
            amount += int(i['兒童口罩剩餘數'])
            continue
        elif region != i['醫事機構地址'][0:3]:
            continue

    if region in i['醫事機構地址'][0:3] and amount == 0:
        reply = "已經銷售一空了！"
    elif amount != 0:
        reply = "還有{}個".format(amount)
    elif region not in i['醫事機構地址'][0:3] and amount == 0 and kind == "成人" and kind == "兒童":
        reply = '醫事機構不存在！'
    elif kind != "成人" and kind != "兒童":
        reply = "口罩類型輸入錯誤！"

    ### 請在上方完成作業功能的程式碼 ###

    return reply


if __name__ == '__main__':
    pass
