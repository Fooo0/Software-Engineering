# -*- coding: utf-8 -*-

"""
Created on Mon Sep 21 18:39:18 2015

@author: 周丽艳 宋佳飞
"""
import time

class Activity():    # 活动类
    def __init__(self,name,rly,prc):
        self.name = name   # 候选活动名称
        self.rly = rly    # 可靠性
        self.prc = prc    # 价格

def Service(num,actsum):    # 数据处理
    global process,req_prc,req_rly
           
    f1 = open("PROCESS.txt","r")    # 活动流程 
    f2 = open("REQ.txt","r")    # 用户要求
    counter = 0
    while counter <= num:    # 行数读取控制
        line1 = f1.readline()    # 活动流程 
        line2 = f2.readline()    # 用户要求
        counter += 1
    f1.close()
    f2.close()    

    for ch in line1:    # 活动流程 
        if ch >= 'A' and ch <= 'Z' and ch not in process[num]:
            process[num].append(ch)

    req = line2.split('(')[1].split(')')[0].split(',')    # 用户要求
    req_rly = float(req[0])    # 可靠性
    req_prc = float(req[1])    # 价格

    # 候选集
    service = open("SERVICE.txt","r")
    i = 0
    mark = ' '
    for line3 in service:    # 读取某候选活动全部信息
        l = line3.split()
        name = l[0]    # 活动名称
        rly = float(l[2])    # 可靠性
        prc = float(l[4])    # 价格
        oneact = Activity(name,rly,prc)    # 构造活动对象
    
        if name[0] != mark:    # 新活动候选集中的活动
            if len(process[num]) == len(actsum):
                break
            elif name[0] in process[num]:
                if prc >= req_prc or rly < req_rly:    # 不满足用户要求
                    actsum.append([])
                else:    # 满足用户要求
                    actsum.append([oneact])
                i += 1
                mark = name[0]
        elif prc < req_prc and rly > req_rly:    # 该候选集中的候选活动
                actsum[i - 1].append(oneact)     # 单个候选活动添加，只加入价格和可靠性满足用户要求的
        
    service.close()
    for i in range(len(actsum)) :    # 排序
        actsum[i].sort(key = lambda act: act.prc)
        
    return line1,process[num],len(process[num])

def Search(i,actsum):    # 先深搜索
    global T,Q,F,req_prc,req_rly,one
    if(i == len(actsum) - 1):    # 最后一个活动的选取
        lastone = False
        price_temp = 0    # 省时，之前不会改变的选中的活动只计算一次
        reli_temp = 1
        for item in T:
            price_temp += item.prc
            reli_temp *= item.rly
        for act in actsum[i]:
            price = price_temp + act.prc
            reli = reli_temp * act.rly
            if price <= req_prc:    # 价格满足
                if reli >= req_rly:    # 可靠性满足
                    nowQ = reli - price / 100
                    if nowQ > Q:    # 更优解
                        Q = nowQ
                        temp = act
                        lastone = True     
            else:    # 按价格升序，若当前价格不满足，其后不需再遍历
                break
        if lastone :
            one = True    # 找到一个可行解，利用该可行解剪枝
            T.append(temp)
            F = T[:]
        return
    # 除最后一个之外的活动选取    
    price_temp = 0    # 省时，之前不会改变的选中的活动只计算一次
    reli_temp = 1
    for item in T:
        price_temp += item.prc
        reli_temp *= item.rly
    for act in actsum[i]:
        T = T[:i]
        prc = price_temp + act.prc
        rly = reli_temp * act.rly
        if one == False:    # 没找到可行解
            if prc <= req_prc:
                if rly >= req_rly:
                    T.append(act)
                    Search(i + 1,actsum)
            else:
                break
        else:    # 找到可行解
            if prc <= req_prc:
                if act.prc > F[i].prc :
                    if act.rly > F[i].rly and rly >= req_rly: # 否则一定不能构成最优解
                        nowQ = rly - prc/100
                        if nowQ > Q:
                            T.append(act)
                            Search(i + 1,actsum)    # 继续搜索
                else:
                    if rly >= req_rly:
                        nowQ = rly - prc/100
                        if nowQ > Q:
                            T.append(act)
                            Search(i + 1,actsum)    # 继续搜索
            else:
                break

def Printresult(F,old_DAG,pre,actnum,start,end):    # 结果打印
    rly = 1
    prc = 0
    index = 0
    print 'Start at',start,'\nEnd at',end,'\nLast for',end - start,'s'
    while actnum > 0: 
        new_DAG = old_DAG.replace(pre[index],F[index].name)
        old_DAG = new_DAG
        actnum -= 1
        index += 1
    print new_DAG
    for item in F:
        prc += item.prc
        rly *= item.rly
    Q = rly - prc / 100
    print 'reliability = ',rly,'\nprice = ',prc,'\nQoS = ',Q,'\n'

         
req_rly = 0
req_prc = 0
process = [[],[],[],[]]    # 四个流程
actsum_all = [[],[],[],[]]    # 四个活动候选

for j in range(4):
    one = False
    F = []
    T = []
    Q = 0
    print 'Process',j + 1,':'
    a = time.clock()
    old_DAG,pre,actnum=Service(j,actsum_all[j])
    Search(0,actsum_all[j])
    b = time.clock()
    Printresult(F,old_DAG,pre,actnum,a,b)