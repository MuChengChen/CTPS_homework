
# -*- coding: utf-8 -*-
import json
from requests import request
import urllib.request, csv

from ExampleData import department_table  # 系所代號對照資料Dictionary
from ExampleData import route_table  # 入學管道代號對照資料Dictionary
import json
import urllib.request, csv
import re
import random


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
                json.dump(user, file,ensure_ascii=False ,indent=2)
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


def HW4_1(text, user_id):
    RegisteredData_path = './registered_data.json'
    day_dict={'一':'1','二':'2','三':'3','四':'4','五':'5','六':'6','日':'7'}
    hour_list=['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
    day = text.split("週")[1].split("的")[0]
    hour =text.split("的")[1].split("時")[0]

    with open(RegisteredData_path, 'r', encoding="utf-8-sig") as file:
        register=json.load(file)

    if user_id in register:
        if day not in day_dict:
            reply="星期輸入錯誤!"
        elif hour not in hour_list:
            reply="時間輸入錯誤!"
        else:
            with open(RegisteredData_path, 'w', encoding="utf-8-sig") as file:
                register[user_id]['Notify']={'Day':day_dict[day],'Hour':hour}
                json.dump(register,file,ensure_ascii=False,indent=2)
                reply="設定成功!將於星期{}的{}點提醒".format(day_dict[day],hour)
    else:
        reply="請先註冊，謝謝！"

    return reply


def HW4_2(user_id):
    url = 'https://playlab.computing.ncku.edu.tw:8000/homework-record/1/json'  # 作業繳交紀錄 url
    homework_record = json.loads(request('GET', url).text)
    RegisteredData_path = './registered_data.json'
    reply="已繳交作業:"
    store=""
    counter=0
    with open(RegisteredData_path, 'r', encoding="utf-8-sig") as file:
        register=json.load(file)

    if user_id in register:
        for HW_dict in homework_record:
            if HW_dict['Student_ID']==register[user_id]['Student_ID']:
                store+=HW_dict['HW']+","
                counter+=1
            else:
                continue
        if counter!=0:
            reply += store[:-1]
        else:
            reply="已繳交作業:無"
    else:
        reply = "請先註冊，謝謝！"


    return reply


def HW4_3(text, user_id):
    RegisteredData_path = './registered_data.json'
    score_path='./score_table.json'
    count=0

    with open(RegisteredData_path, 'r', encoding="utf-8-sig") as file1:
        register=json.load(file1)
    with open(score_path, 'r', encoding="utf-8-sig") as file2:
        grade=json.load(file2)



        def excellent(count):

            for i in grade.values():
                if i<=100 and i>=85:
                    count+=1
                else:
                    continue
            return count
        def good(count):

            for i in grade.values():
                if i<=84 and i>=70:
                    count+=1
                else:
                    continue
            return count
        def notbad(count):

            for i in grade.values():
                if i<=69 and i>=50:
                    count+=1
                else:
                    continue
            return count
        def bad(count):

            for i in grade.values():
                if i<=49 and i>=35:
                    count+=1
                else:
                    continue
            return count
        def unbelievable(count):

            for i in grade.values():
                if i<=34 and i>=0:
                    count+=1
                else:
                    continue
            return count


    grade_name = text.split('到')[1].split('的')[0]
    switch = {'excellent': excellent(count), 'good': good(count), 'notbad': notbad(count), 'bad': bad(count),
              'unbelievable': unbelievable(count)}
    if user_id in register:
        #if text.split('到')[1].split('的')[0] == 'excellent' or 'good' or 'notbad' or 'bad' or 'unbelievable':
         if grade_name in switch:
            reply = '共有{}位同學'.format(switch.get(grade_name))
         else:
            reply = '沒有這個等第！'
    else:
        reply = "請先註冊，謝謝！"

    return reply

def HW6_1(text,user_id):
    RegisteredData_path = './registered_data.json'
    with open(RegisteredData_path, 'r', encoding="utf-8-sig") as file:
        register = json.load(file)
    text1=text.split('算')[1].split('等')[0]
    print(text1)
    #負數需要括號，正數與0不要括號
    def MultipleAndDivision(text2):
        pattern1=re.compile('(\[-){0,1}[\d]+\.*[\d]*]{0,1}[*|/]{1}(\[-){0,1}[\d]+\.*[\d]*]{0,1}')
        if pattern1.search(text2)!=None:
            SimpleFormula1=pattern1.search(text2).group()
            print(SimpleFormula1)
            SimpleFormulaList1=re.findall('-{0,1}[\d]+\.*[\d]*',SimpleFormula1)
            print(SimpleFormulaList1)
            if re.search('[*|/]', SimpleFormula1).group()=='*':
                result1 = float(SimpleFormulaList1[0])*float(SimpleFormulaList1[1])
                print(result1)
            elif re.search('[*|/]', SimpleFormula1).group()=='/':
                result1 = float(SimpleFormulaList1[0])/float(SimpleFormulaList1[1])
                print(result1)
            if result1>=0:
                nexttext1=re.sub('(\[-){0,1}[\d]+\.*[\d]*]{0,1}[*|/]{1}(\[-){0,1}[\d]+\.*[\d]*]{0,1}',str(result1),text2,count=1,flags=re.A|re.X|re.DOTALL)
                print(nexttext1)
            elif result1<0:
                nexttext1 = re.sub('(\[-){0,1}[0-N]+\.*[0-N]*]{0,1}[*|/]{1}(\[-){0,1}[0-N]+\.*[0-N]*]{0,1}','['+str(result1)+']', text2, count=1, flags=re.A | re.X | re.DOTALL)
                print(nexttext1)
            return MultipleAndDivision(nexttext1)
        elif pattern1.search(text2)==None:
            return text2
    def PlusAndMinus(text3):
        pattern2=re.compile('(\[-){0,1}[\d]+\.*[\d]*]{0,1}[+|-]{1}(\[-){0,1}[\d]+\.*[\d]*]{0,1}')
        if pattern2.search(text3)!=None:
            #將最前面的最簡加減算式挑出來
            SimpleFormula2=pattern2.search(text3).group()
            print(SimpleFormula2)
            #以下判別式為避免將減號認為負號所設
            #若無負數
            if  re.search('(\[-){1}[\d]+\.*[\d]*]{1}',SimpleFormula2)==None:
                SimpleFormulaList2=re.findall('[\d]+\.*[\d]*',SimpleFormula2)
                num1 = SimpleFormulaList2[0]
                num2 = SimpleFormulaList2[1]
                print(SimpleFormulaList2)
            #若負數在前面或是兩個都是負數
            elif (len(re.findall('\[', SimpleFormula2))==1 and SimpleFormula2[0]!='[') or len(re.findall('\[', SimpleFormula2))==2:
                SimpleFormulaList2 = re.findall('-{0,1}[\d]+\.*[\d]*', SimpleFormula2)
                num1 =SimpleFormulaList2[0]
                num2 =SimpleFormulaList2[1]
                print(SimpleFormulaList2)
            #若負數在後面
            else:
                num1=re.search('-{1}[\d]+\.*[\d]*', SimpleFormula2).group()
                a=SimpleFormula2
                a=re.sub('-{1}[\d]+\.*[\d]*','',a,count=1)
                num2 = re.search('[\d]+\.*[\d]*', a).group()
            #將負號去掉以免以下判別式判別錯誤
            SimpleFormula2 = re.sub('\[-','',SimpleFormula2)
            SimpleFormula2 = re.sub(']', '', SimpleFormula2)
            if re.search('[+|-]', SimpleFormula2).group()=='+':
                result2 = float(num1)+float(num2)
                print(result2)
            elif re.search('[+|-]', SimpleFormula2).group()=='-':
                result2 = float(num1)-float(num2)
                print(result2)
            #將原算式替代成答案
            if result2>=0:
                nexttext2=re.sub('(\[-){0,1}[\d]+\.*[\d]*]{0,1}[+|-]{1}(\[-){0,1}[\d]+\.*[\d]*]{0,1}',str(result2),text3,count=1,flags=re.A|re.X|re.DOTALL)
                print(nexttext2)
            elif result2<0:
                nexttext2 = re.sub('(\[-){0,1}[\d]+\.*[\d]*]{0,1}[+|-]{1}(\[-){0,1}[\d]+\.*[\d]*]{0,1}','['+str(result2)+']', text3, count=1, flags=re.A | re.X | re.DOTALL)
                print(nexttext2)
            return PlusAndMinus(nexttext2)
        elif pattern2.search(text3)==None:
            return text3
    def Power(text4):
        pattern3=re.compile('(\[-){0,1}[\d]+\.*[\d]*]{0,1}\^{1}(\[-){0,1}[\d]+\.*[\d]*]{0,1}')
        if pattern3.search(text4)!=None:
            SimpleFormula3=pattern3.search(text4).group()
            print(SimpleFormula3)
            SimpleFormulaList3=re.findall('-{0,1}[\d]+\.*[\d]*',SimpleFormula3)
            result3 = float(SimpleFormulaList3[0])**float(SimpleFormulaList3[1])
            if isinstance(result3,complex):
                return "不接受複數運算"
            elif result3 is not complex:
                if result3>=0 :
                    nexttext3=re.sub('(\[-){0,1}[\d]+\.*[\d]*]{0,1}\^{1}(\[-){0,1}[\d]+\.*[\d]*]{0,1}',str(result3),text4,count=1,flags=re.A|re.X|re.DOTALL)
                    print(nexttext3)
                    return Power(nexttext3)
                elif result3<0 :
                    nexttext3 = re.sub('(\[-){0,1}[\d]+\.*[\d]*]{0,1}\^{1}(\[-){0,1}[\d]+\.*[\d]*]{0,1}','['+str(result3)+']', text4, count=1, flags=re.A | re.X | re.DOTALL)
                    print(nexttext3)
                    return Power(nexttext3)

        elif pattern3.search(text4)==None:
            return text4
    def preprocess(text5):
        pattern4=re.compile('(\(-){1}[\d]+\.*[\d]*\){1}')
        if pattern4.search(text5)!=None:
            negnum=pattern4.search(text5).group()
            negnum=re.sub('\(','[',negnum)
            negnum = re.sub('\)', ']', negnum)
            text5=re.sub('(\(-){1}[\d]+\.*[\d]*\){1}',negnum,text5,count=1)
            print(text5)
            return preprocess(text5)
        elif pattern4.search(text5)==None:
            return text5
    def changelist(text6):
        print(re.split('([(|)])', preprocess(text6)))
        ProcessList = re.split('([(|)])', preprocess(text6))
        formula = ''
        if len(ProcessList) == 1:
            if Power(ProcessList[0]) == "不接受複數運算":
                return "不接受複數運算"
            else:
                return PlusAndMinus(MultipleAndDivision(Power(ProcessList[0])))
        else:
            for i in range(len(ProcessList)):
                print(ProcessList[i])
                if ProcessList[i] == '' or ProcessList[i] == '(' or ProcessList[i] ==')' or ProcessList[i] =='+' or ProcessList[i] =='-' or ProcessList[i] =='*' or ProcessList[i] =='/' or ProcessList[i] =='^':
                    print(ProcessList[i])
                    print(ProcessList)
                    continue
                elif ProcessList[i][0] == '+' or ProcessList[i][0] =='-' or ProcessList[i][0] =='*' or ProcessList[i][0] =='/' or ProcessList[i][0] =='^':
                    ProcessList.insert(i, ProcessList[i][0])
                    ProcessList[i+1] = ProcessList[i+1][1:]
                    if ProcessList[i+1][-1] == '+' or ProcessList[i+1][-1] =='-' or ProcessList[i+1][-1] =='*' or ProcessList[i+1][-1] =='/' or ProcessList[i+1][-1] =='^':
                        ProcessList.insert(i+2, ProcessList[i+1][-1])
                        ProcessList[i+1] = ProcessList[i+1][:-1]
                    print(ProcessList[i])
                    print(ProcessList)
                    continue
                elif ProcessList[i][-1] == '+' or ProcessList[i][-1] =='-' or ProcessList[i][-1] =='*' or ProcessList[i][-1] =='/' or ProcessList[i][-1] =='^':
                    ProcessList.insert(i+1, ProcessList[i][-1])
                    ProcessList[i] = ProcessList[i][:-1]
                    if Power(ProcessList[i]) == "不接受複數運算":
                        return "不接受複數運算"
                    else:
                        ProcessList[i] = PlusAndMinus(MultipleAndDivision(Power(ProcessList[i])))
                        print(ProcessList[i])
                        print(ProcessList)
                        continue
                elif ProcessList[i-1] == '(' and ProcessList[i+1] == ')':
                    ProcessList[i-1] = ProcessList[i+1] = ''
                    ProcessList[i] = PlusAndMinus(MultipleAndDivision(Power(ProcessList[i])))
                    print(ProcessList[i])
                    print(ProcessList)
                    continue
                else :
                    ProcessList[i] = PlusAndMinus(MultipleAndDivision(Power(ProcessList[i])))
                    print(ProcessList[i])
                    print(ProcessList)
                    continue
            for i in ProcessList:
                formula+=i
            print(formula)
            return changelist(formula)

    if user_id in register:
        return changelist(text1)

    else:
        return "請先註冊，謝謝！"



def HW6_2(text,user_id):
    RegisteredData_path = './registered_data.json'
    num=int(text.split('出')[1].split('個')[0])

    with open(RegisteredData_path, 'r', encoding="utf-8-sig") as file:
        register = json.load(file)
    TeamOrderList=[]
    reply='報告順序:'
    if user_id in register:
        if num<=0:
            return '組別不能少於1組喔'
        else:
            for i in range(1,num+1):
                TeamOrderList.append('第{}組'.format(i))
            random.shuffle(TeamOrderList)
            for j in TeamOrderList:
                reply+=j+"->"
            return reply[:-2]
    else:
        return "請先註冊，謝謝！"

if __name__ == '__main__':

    print(HW6_2(text='請排出5個小組的報告順序', user_id='Ua7990e553bfd285a45702f6685e6932a'))
    print(HW6_1(text='計算6*5+4/3+8-5等於多少', user_id='Ua7990e553bfd285a45702f6685e6932a'))
    pass

