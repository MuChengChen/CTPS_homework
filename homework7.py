import time as t
import csv

def get_date():
    seconds = t.time()
    result = t.localtime(seconds)
    if result.tm_mon < 10:
        month = '0' + str(result.tm_mon)
    else:
        month = str(result.tm_mon)
    if result.tm_mday < 10:
        day = '0' + str(result.tm_mday)
    else:
        day = str(result.tm_mday)
    date = month + day
    print(date)
def class_participating_basic_score(id):
    basic_score = 0
    participation = '0'
    participation_score = '0'
    write='0'
    speak='0'
    teacher_quetion='0'
    TA_quetion='0'
    print(id)
    with open('class_participate.csv', newline='', encoding=('utf-8')) as csvfile:
        class_record = csv.reader(csvfile)
        for i in class_record:
            if id == i[0]:
                if i[9] != '':
                    participation = i[9]
                if i[14] != '':
                    participation_score = i[14]
                if i[2] != '':
                    write = i[2]
                if i[4] != '':
                    speak = i[4]
                if i[13] != '':
                    teacher_quetion= i[13]
                if i[15] != '':
                    TA_quetion = i[15]

                activity=(float(write) + float(speak) + float(teacher_quetion) + float(TA_quetion))* 0.3
                if activity> 3:
                    activity= 3

                basic_score= float(participation) + float(participation_score)*0.1+activity
                print(basic_score)
    return basic_score
def class_participating_homework_score(id):
    homework_score = 0
    TA_time = '0'
    teacher_office_hour='0'
    self_learning_python='0'
    print(id)
    with open('class_participate.csv', newline='', encoding=('utf-8')) as csvfile:
        class_record = csv.reader(csvfile)
        for i in class_record:
            if id == i[0]:
                if i[3] != '':
                    TA_time = i[3]
                if i[7] != '':
                    teacher_office_hour = i[7]
                if i[17] != '':
                    self_learning_python = i[17]

                homework_score=float(TA_time)*0.2 + float(teacher_office_hour)*0.2+float( self_learning_python )* 0.1
                print(homework_score)
                if homework_score>2:
                    homework_score = 2
                else:
                    continue
                print(homework_score)
    return homework_score
def class_participating_final_project_score(id):
    final_project_score = 0
    time = '0'
    print(id)
    with open('class_participate.csv', newline='', encoding=('utf-8')) as csvfile:
        class_record = csv.reader(csvfile)
        for i in class_record:
            if id == i[0]:
                if i[10] != '':
                    time = i[10]

                final_project_score = float(time) *0.2
                print(final_project_score)
                if final_project_score>2:
                    final_project_score = 2
                else:
                    continue
                print(final_project_score)
    return final_project_score
def class_participating_extra_score(id):
    extra_score = 0
    help_classmate = '0'
    message_TA = '0'
    print(id)
    with open('class_participate.csv', newline='', encoding=('utf-8')) as csvfile:
        class_record = csv.reader(csvfile)
        for i in class_record:
            if id == i[0]:
                if i[5] != '':
                    help_classmate = i[5]
                if i[8] != '':
                    message_TA= i[8]
                extra_score = (float(help_classmate)+float(message_TA))*0.1
                print(extra_score)
                if extra_score>1:
                    extra_score = 1
                else:
                    continue
                print(extra_score)
    return extra_score
def total_score(id):
    basic_score = class_participating_basic_score(id)
    homework_score = class_participating_homework_score(id)
    final_project_score=class_participating_final_project_score(id)
    extra_score = class_participating_extra_score(id)
    total_score = basic_score + homework_score + final_project_score + extra_score
    print(total_score)
    if total_score > 20:
        total_score = 20
    elif total_score<17:
        with open('class_participate.csv', newline='', encoding=('utf-8')) as csvfile:
            class_record = csv.reader(csvfile)
            for i in class_record:
                if id == i[0]:
                    if i[10] != '' and i[17] != '' :
                        if float(i[10])-10>0:
                            total_score=(float(i[10])-10)*0.15+total_score
                            print('ya')
                            print(total_score)
                        if float(i[17])-20>0:
                            total_score=(float(i[17])-20)*0.15+total_score
                            print('ya')
                            print(total_score)
                        if total_score>20:
                            total_score=20
    return total_score
def count_everyone_score():
    score = {}
    with open('class_participate.csv', newline='', encoding=('utf-8')) as csvfile:
        class_record = csv.reader(csvfile)
        for i in class_record:
            if i[0] != 'ID':
                score[i[0]] = total_score(i[0])
            continue
    print(score)
    return score

if __name__ == '__main__':
   # print(class_participating_basic_score('B24061338'))
   # print(class_participating_advance_score('B24061338'))
    #print(class_participating_extra_score('B24061338'))
   # print(total_score('B24051236'))
    print(count_everyone_score())

