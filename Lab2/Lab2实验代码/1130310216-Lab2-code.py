# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 09:22:55 2015

@author: asus-pc
"""

from time import clock

def select_data(service, process, element_num, std_quality, std_money):
    """Select feasible services from a large service set"""
    number = []
    ser = []
    app3 = number.append
    app4 = ser.append
    j = 0
    temp_a = -1
    while j < len(service)/3:
        if service[j*3][0] in process:
            app3(0) #初始化
            temp_a = temp_a + 1
            temp_l = 0
            while temp_l < 500:
                temp_b = j+temp_l
                if service[temp_b * 3 + 1] > std_quality: #不取等
                    temp_n = service[temp_b * 3 + 2]
                    if temp_n < std_money:
                        app4(service[temp_b * 3:temp_b * 3 + 3])
                        number[temp_a] += 1
                temp_l += 1

        j += 500

    ser.sort(key=lambda z: (z[0][0], z[1]))      #tr从小到大排
#二次筛
    k = 0
    i = 0
    while k != len(ser):
        j = number[i]-1
        tp_sep = ser[k+j][2]
        tr_first = ser[k+j][1]
        j -= 1#以第一个元素为基准，从第二个元素开始(此时第一个元素总会留下来)

        while j != -1:
            if ser[k+j][2] < tp_sep:
                if ser[k+j][1] == tr_first:
                    ser.pop(k+j+1)
                    number[i] -= 1
                else:   #小于
                    tr_first = ser[k+j][1]
                tp_sep = ser[k+j][2]
                j -= 1

            else:
                ser.pop(k+j)
                number[i] -= 1
                j -= 1

        k += number[i]
        i += 1

    for j in xrange(element_num-1):
        number[j+1] = number[j]+number[j+1]

    return ser, number

def choose_service(element_num, number, std_quality, std_money, ser):
    """Search for optimal solution in the feasible service set"""
    result = [0]*element_num  #保存合格服务(过程中)
    final = [0]*element_num    #最佳
    tra_tr = [1]*element_num
    tra_tp = [0]*element_num
    travel = [num - 1 for num in number] #记录每个元素最后一个数下标

    big_q = 0
    flag = 1
    level = element_num - 1    #从最后一个活动开始遍历
    num0 = number[0]

    while flag == 1:
        while level != 0:
            visit = travel[level]   #该活动第一个元素(或上次访问到的最后一个元素),x从0开始
            board = number[level-1]-1
            if level == element_num-1:
                tr_r = 1
                tp_p = 0
            else:
                tr_r = tra_tr[level+1]
                tp_p = tra_tp[level+1]
            while 1:   #找到或最后一个停止循环(该循环内n相同)
                if visit == board:    #超出该层范围（表明该层最后一个已经检测过）
                    travel[level] = number[level] - 1
                    level += 1
                    if level == element_num:
                        flag = 0  #超出范围，表明所有都遍历结束
                    break
                fresh_tr = tr_r*ser[visit][1]
                if fresh_tr > std_quality:
                    fresh_tp = tp_p+ser[visit][2]
                    if fresh_tp >= std_money:
                        visit -= 1
                    else:
                        result[level] = ser[visit][0]
                        tra_tr[level] = fresh_tr
                        tra_tp[level] = fresh_tp
                        travel[level] = visit-1       #如果x已是最后一个数则超出范围
                        level -= 1
                        if level == 0:
                            tr1 = tra_tr[1]
                            tp1 = tra_tp[1]
                        break
                else:
                    visit = board
            if flag == 0:
                break

        if level == 0:
            i = num0 - 1
            while i != 0:
                fresh_tr = tr1*ser[i][1]
                if fresh_tr > std_quality:
                    fresh_tp = tp1+ser[i][2]
                    if fresh_tp < std_money:
                        new_q = fresh_tr-fresh_tp/100
                        if new_q > big_q:
                            result[0] = ser[i][0]
                            tra_tr[0] = fresh_tr  #记录TR
                            tra_tp[0] = fresh_tp  #记录TP
                            big_q = new_q
                            for j in xrange(element_num):  #记录最佳
                                final[j] = result[j]

                else:
                    break

                i -= 1

        level += 1#返回上一层
    prc = tra_tp[0]
    rly = tra_tr[0]
    return prc, rly, big_q, final

def print_service(start, finish, pro, process, final, prc, rly, big_q):
    """Print the best solution"""
    for j in pro:
        if  j in process:
            i = 0
            while final[i][0] != j:
                i += 1
            print final[i],
        else:
            print j,

    print"Reliability=", rly, ",Cost=", prc, ",Q=", big_q, '\n'
    print "start:", start, "\nfinish:", finish
    print "time:", finish-start

#@profile
def func():
    """The main function"""
    service = []
    app5 = service.append
    ##----------read data----------------
    #service
    for i in open('SERVICE.txt'):
        app5(i.split(' ')[0])
        app5(float(i.split()[2]))
        app5(float(i.split()[4]))

    #req
    req = [i.split('(')[1].split(')')[0].split(',') for i in open('REQ.txt')]

    #process
    f_file = open('PROCESS.txt')
    for i in xrange(4):
        print "--------------process", i+1, ":--------------", '\n'
        pro = f_file.readline()
        process = []            #a service set
        app2 = process.append
        for j in pro:
            if 'A' <= j <= 'Z' and j not in process:
                app2(j)

        element_num = len(process)
        number = []                        #count the numbers of all
        std_quality = float(req[i][0])
        std_money = float(req[i][1])
        ser = []

        final = []
        big_q = 0
        prc = 0
        rly = 1

        start = clock()
        ser, number = select_data(service, process, element_num,
                                  std_quality, std_money)
        prc, rly, big_q, final = choose_service(element_num, number,
                                                std_quality, std_money, ser)
        finish = clock()

        print_service(start, finish, pro, process, final, prc, rly, big_q)


func()
