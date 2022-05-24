from tokenize import Number
import scipy.io 
import numpy as np

def cut(A):
    for i in A:
        A[i] = sorted(A[i].find(Number))
    return A

def fixTransactions(transactions):  
    temp = [i[1][j] for i in transactions for j in range(0, len(i[1]))]
    return temp

def fixProducts(products):
    for i in range(products.shape[0]):
        for j in range(products.shape[1]):
            products[i][j] = products[i][j].strip()
    return products

def fixHistory(history):
    temp = list()
    for i in history:
        temp.append(i[0])
        temp.append(len(i[1]))
    return temp

def fixHistory1(history):
    for i in range(len(history)):
        for j in range(len(history[i])):
            for k in range(len(history[i][j])):
                history[i][j][k]=history[i][j][k].strip()
    return history

def sortMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            if matrix[i][1] == matrix[j][1]:
                temp = matrix[i][0]
                matrix[i][0] = matrix[j][0]
                matrix[j][0] = temp
    return matrix


def req1(transactions):
    temp1 = fixTransactions(transactions)
    index = sorted(list(set(temp1)))
    
    buf = [temp1.count(k) for k in index]
            
    maximum = sorted([index[i] for i in range(len(buf)) if buf[i] == max(buf)])
    minimum = sorted([index[i] for i in range(len(buf)) if buf[i] == min(buf)])
    
    maximum = cut(maximum)
    
    return maximum, minimum

def req2(products):
    index = fixProducts(products)
    
    buf = list(index[:, 2])
    for i in range(len(buf)):
        buf[i] = int(buf[i])
    
    result = products[:, 0]
    
    maximum = sorted([result[i] for i in range(len(buf)) if buf[i] == max(buf)])
    minimum = sorted([result[i] for i in range(len(buf)) if buf[i] == min(buf)])
    
    return maximum, minimum

def req3(transactions, products):
    temp1 = fixTransactions(transactions)
    temp2 = fixProducts(products)
    
    q = temp2[:, 0]
    p = list(temp2[:,1])
    
    for i in range(len(p)):
        p[i] = int(p[i])
    
    total_revenue = 0
    for i in range(len(q)):
        total_revenue = total_revenue + temp1.count(q[i])*p[i]
    return total_revenue

def req4(transactions, products):
    
    temp1 = fixTransactions(transactions)
    temp2 = fixProducts(products)
    
    p = list(temp2[:,1])
    q = temp2[:, 0]

    for i in range(len(p)):
        p[i] = int(p[i])
    
    total_revenue = [temp1.count(q[i])*p[i] for i in range(len(q))]
            
    result = [q[i] for i in range(len(total_revenue)) if total_revenue[i] == max(total_revenue)]
    return result

def req5(history, k):
    temp = fixHistory(history)
    temp = np.hstack(temp)
    index = temp.reshape(int(len(temp)/2), 2)
    index = index[np.argsort(index[:, 1])][::-1]
    
    index = sortMatrix(index)
    
    result = [index[i][0] for i in range(0, k)]
    return result

def req6(transactions, history, k):
    temp1 = list(np.hstack(history[:,0]))
    temp2 = list(history[:,1])
    temp3 = list(np.hstack(transactions[:,0]))
    temp4 = list(transactions[:,1])

    for i in range(len(temp1)):
        if temp1[i] == k:
            index = temp2[i]
    
    flag = [temp4[j] for i in range(len(index)) for j in range(len(temp3)) if index[i] == temp3[j]]
    flag = list(np.hstack(flag))
    buf = sorted(list(set(flag)))
    
    var = [flag.count(i) for i in buf]
    
    result = [buf[i] for i in range(len(var)) if var[i] == max(var)]
    return result