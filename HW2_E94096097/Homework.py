import json
from ExampleData import department_table  # 系所代號對照資料Dictionary
from ExampleData import route_table  # 入學管道代號對照資料Dictionary


def HW2(text, user_id):  # text => 接收到的訊息字串;   user_id => User的Line ID

    ### 請在下方完成作業功能的程式碼 ###
    student_data = dict()  # 學生資料
    ID= {'name': text.split(":")[1].split("/")[0], 'user_id': user_id}
    student_data[(text.split(":")[2])] = ID

    department = department_table.get((text.split(":")[2])[0:2])  # 學號對應的系所
    route = route_table.get((text.split(":")[2])[5:6])  # 入學管道
    error=department_table.get((text.split(":")[2])[0:2])
    if (error == None):
        return ('找不到這個系所', student_data)
    else:
        return ('您的系所是 ' + department + ' ，入學管道是 ' + route, student_data)


