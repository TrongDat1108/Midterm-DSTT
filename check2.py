import scipy.io 
import numpy as np

mat = scipy.io.loadmat('data.mat')
transactions = mat["transactions"]
products = mat["products"]
history = mat["history"]

########## Requirements ######
def req1(transactions):
    if type(transactions).__name__ != 'ndarray':
        return [],[]
    re = [transactions[0][1][0]]
    for i in transactions:
        for j in i[1]:
            if j in re:
                continue
            else:
                re.append(j)
    temp = [0 for i in range(len(re))]
    for i in transactions:
        for j in i[1]:
            if j in re:
                temp[re.index(j)]+=1
    mx = max(temp)
    mn = min(temp)
    remax = []
    remin = []
    for i in range(len(temp)):
        if temp[i]==mx:
            remax.append(re[i])
    for i in range(len(temp)):
        if temp[i]==mn:
            remin.append(re[i])
    remax.sort()
    remin.sort()
    return remax,remin
 
def req2(products):
    if type(products).__name__ != 'ndarray':
        return [],[]
    temp = [int(i[2].strip()) for i in products]
    mx = np.max(temp)
    mn = np.min(temp)
    remax = []
    remin = []
    for i in products:
        if mx == int(i[2]):
            remax.append(i[0].strip())
        if mn == int(i[2]):
            remin.append(i[0].strip())
    remax.sort()
    remin.sort()
    return remax,remin

def req3(transactions, products):
    if type(transactions).__name__ != 'ndarray' or type(products).__name__ != 'ndarray':
        return None
    re = [transactions[0][1][0]]
    for i in transactions:
        for j in i[1]:
            if j in re:
                continue
            else:
                re.append(j)
    temp = [0 for i in range(len(re))]
    for i in transactions:
        for j in i[1]:
            if j in re:
                temp[re.index(j)]+=1
    for i in re:
        for j in products:
            if i == j[0].strip():
                temp[re.index(i)] *= int(j[1])
    result = round(sum(temp),1)
    return result

def req4(transactions, products):
    if type(transactions).__name__ != 'ndarray' or type(products).__name__ != 'ndarray':
        return []
    re = [transactions[0][1][0]]
    for i in transactions:
        for j in i[1]:
            if j in re:
                continue
            else:
                re.append(j)
    temp = [0 for i in range(len(re))]
    for i in transactions:
        for j in i[1]:
            if j in re:
                temp[re.index(j)]+=1
    for i in re:
        for j in products:
            if i == j[0].strip():
                temp[re.index(i)] *= int(j[1])
    result = []
    result.append(re[temp.index(max(temp))])
    result.sort()
    return result

def req5(history, k):
    if type(history).__name__ != 'ndarray' or type(k)!= int:
        return []
    result = []
    if k>=0 and k <= len(history):
        temp = [len(i[1]) for i in history]
        temp1 = [i[0] for i in history]
        for i in range(len(temp)-1):
            m = i
            for j in range(m+1,len(temp1)):
                if temp[j] > temp[m]:
                    temp[j],temp[m] = temp[m],temp[j]
                    temp1[j],temp1[m] = temp1[m],temp1[j]
        for i in temp1:
            if k>0:
                result.append(i[0])
                k-=1
    return result

def req6(transactions, history, k):
    if type(history).__name__ != 'ndarray' or type(transactions).__name__ != 'ndarray':
        return []
    tempT = []
    for i in history:
        for j in i[1]:
            if i[0] == k:
                tempT.append(j)
    tempI = []
    for i in transactions:
        for m in tempT:
            if m == i[0]:
                for j in i[1]:
                    tempI.append(j)
    dict = {}
    for i in tempI:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    if dict != {}:
        mx = max(dict.values())
        result = [key for key,i in dict.items() if i==mx]
        result.sort()
    else:
        result = []
    return result

def req7(transactions, history):
    if type(history).__name__ != 'ndarray' or type(transactions).__name__ != 'ndarray':
        return []
    temp = []
    for i in history:
        temp.append(len(i[1]))
    mn = min(temp)
    re = []
    temp1 =[]
    for i in history:
        if len(i[1]) == mn:
            for j in i[1]:
                temp1.append(j)
    re = {}
    for k in transactions:
        for m in k[0]:
            if m in temp1:
                for n in k[1]:
                    if n in re:
                        re[n] +=1
                    else:
                        re[n] = 1
    mx = max(re.values())
    result = [key for key,i in re.items() if i==mx]
    result.sort()
    return result

def req8(transactions, history, k):
    if type(history).__name__ != 'ndarray' or type(transactions).__name__ != 'ndarray':
        return []
    def solveCosine(u,v):
        return np.sum(u*v)/(np.linalg.norm(u)*np.linalg.norm(v))
    def countMH(lst,arr):
        temp = [0 for i in lst]
        for i in arr:
            if i in lst:
                temp[lst.index(i)]+=1
        return temp
    te1 = []
    for i in range(len(history)):
        if history[i][0] == k :
            for m in history[i][1]:
                for j in range(len(transactions)):
                    if transactions[j][0] == m: 
                        te1 = [k for k in transactions[j][1]]
    lst = [transactions[0][1][0]]
    for i in transactions:
        for j in i[1]:
            if j not in lst:
                lst.append(j)
    lst.sort()
    result = {}
    kArray = np.array(countMH(lst,te1))
    for i in history:
        temp1 = []
        if i[0] != k:
            for j in i[1]:
                for n in transactions:
                    if j == n[0]:
                        for m in n[1]:
                            temp1.append(m)
            te = np.array(countMH(lst,temp1))
            result[i[0][0]] = solveCosine(te,kArray)
    mx = max(result.values())
    re = [key for key,value in result.items() if value == mx]
    return re

def req9(transactions, history, products):
    if type(history).__name__ != 'ndarray' or type(transactions).__name__ != 'ndarray' or type(products).__name__ != 'ndarray':
        return []
    temp = []
    for i in transactions:
        for j in i[1]:
            temp.append(j)
    temp = list(set(temp))
    result = []
    for i in products:
        k = i[0].strip()
        if k not in temp:
            result.append(k)
    return result

def req10(history, transactions, products, k):
    if type(history).__name__ != 'ndarray' or type(transactions).__name__ != 'ndarray' or type(products).__name__ != 'ndarray' or type(k)!=str:
        return None
    def solve(te,check,pro):
        tem = {}
        for i in check:
            if i not in tem:
                tem[i] = 0
        for j in te:
            for i in pro:
                if j == i[0].strip():
                    tem[int(i[3])] +=1
        return tem
    lst = [transactions[0][1][0]]
    for i in transactions:
        for j in i[1]:
            if j not in lst:
                lst.append(j)
    lst.sort()
    check = [int(products[0][3])]
    for i in products:
        if int(i[3]) not in check:
            check.append(int(i[3]))
    check.sort()
    te = []
    his_lst = []
    for i in history:
        his_lst.append(i[0])
    if k not in his_lst:
        return None
    for i in history:
        if i[0] == k:
            for j in i[1]:
                for n in transactions:
                    if j == n[0]:
                        for m in n[1]:
                            te.append(m)
    re = solve(te,check,products)
    mx = [key for key,value in re.items() if value == max(re.values())]
    return mx[0]




print(req1(transactions))
print(req2(products))
print(req3(transactions, products))
print(req4(transactions, products))
print(req5(history, 3))
print(req6(transactions, history, 'U2'))
print(req7(transactions, history))
print(req8(transactions, history, 'U5'))
print(req9(transactions, history, products))
print(req10(history, transactions, products, 'U2'))