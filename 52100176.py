from tokenize import Number
import scipy.io 
import numpy as np

# mat = scipy.io.loadmat('data.mat')
# transactions = mat["transactions"]
# products = mat["products"]
# history = mat["history"]


transactions = np.array([[np.array(['DON1'], dtype = object), np.array(['SP1', 'SP7', 'SP2', 'SP11'], dtype = object)],
                         [np.array(['DON3'], dtype = object), np.array(['SP6', 'SP1', 'SP6'],  dtype = object)],
                         [np.array(['DON2'], dtype = object), np.array(['SP8','SP10', 'SP2', 'SP3', 'SP5'], dtype = object)],
                         [np.array(['DON4'], dtype = object), np.array(['SP1', 'SP9'], dtype = object)],
                         [np.array(['DON5'], dtype = object), np.array(['SP6'], dtype = object)],
                         [np.array(['DON8'], dtype = object), np.array(['SP1', 'SP2', 'SP3', 'SP6', 'SP8'], dtype = object)],
                         [np.array(['DON9'], dtype = object), np.array(['SP2', 'SP7', 'SP1', 'SP9', 'SP3'], dtype = object)],
                         [np.array(['DON7'], dtype = object), np.array(['SP3', 'SP4', 'SP1'], dtype = object)],
                         [np.array(['DON6'], dtype = object), np.array(['SP6', 'SP7','SP10', 'SP3'], dtype = object)],
                         [np.array(['DON10'], dtype = object), np.array(['SP5', 'SP7', 'SP3', 'SP6'], dtype = object)]])
products = np.array([["SP1 ", '20', '5', '3'], 
                     ["SP4   ", '10', '8', '1'], 
                     ["SP9 ", '20', '11', '2'], 
                     ["SP6 ", '30', '0', '3'], 
                     ["SP5 ", '10', '5', '3'], 
                     ["SP3 ", '30', '1', '1'], 
                     ["SP7 ", '30', '4', '2'], 
                     ["SP8 ", '20', '11', '2'], 
                     ["SP10 ", '20', '3', '3'], 
                     ["SP11 ", '10', '10', '1'],
                     ["SP2", '20', '8', '1']])
history = np.array([[np.array(['KH7'], dtype= '<U3'), np.array(['DON9', 'DON4', 'DON2'], dtype= '<U4')],
                    [np.array(['KH2'], dtype= '<U3'), np.array(['DON5', 'DON7'], dtype= '<U4')],
                    [np.array(['KH5'], dtype= '<U3'), np.array(['DON2', 'DON3', 'DON7','DON10', 'DON8'], dtype= '<U4')],
                    [np.array(['KH6'], dtype= '<U3'), np.array(['DON1', 'DON5', 'DON7'], dtype= '<U4')],
                    [np.array(['KH3'], dtype= '<U3'), np.array(['DON5', 'DON1'], dtype= '<U4')],
                    [np.array(['KH4'], dtype= '<U3'), np.array(['DON3', 'DON2', 'DON10', 'DON1'], dtype= '<U4')],
                    [np.array(['KH1'], dtype= '<U3'), np.array(['DON1', 'DON3', 'DON11', 'DON2'], dtype='<U4')]])


########## Requirements ######
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
            
    maximum = [index[i] for i in range(len(buf)) if buf[i] == max(buf)]
    minimum = [index[i] for i in range(len(buf)) if buf[i] == min(buf)]
    
    maximum.sort()
    minimum.sort()
    
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
    
    total_revenue = 0
    for i in range(len(q)):
        total_revenue = round(total_revenue + temp1.count(q[i])*int(p[i]), 1)
    return total_revenue

def req4(transactions, products):
    
    temp1 = fixTransactions(transactions)
    temp2 = fixProducts(products)
    
    p = list(temp2[:,1])
    q = temp2[:, 0]
    
    total_revenue = [temp1.count(q[i])*int(p[i]) for i in range(len(q))]
            
    result = sorted([q[i] for i in range(len(total_revenue)) if total_revenue[i] == max(total_revenue)])
    return result

def req5(history, k):
    temp = np.hstack(fixHistory(history))
    index = temp.reshape(int(len(temp)/2), 2)
    index = index[np.argsort(index[:, 1])][::-1]
    
    index = sortMatrix(index)
    
    result = [index[i][0] for i in range(0, k)]
    return result

def req6(transactions, history, k):
    temp1 = list(np.hstack(history[:,0]))
    temp2 = list(np.hstack(transactions[:,0]))
    temp3 = list(history[:,1])
    temp4 = list(transactions[:,1])

    for i in range(len(temp1)):
        if temp1[i] == k:
            index = temp3[i]
    
    flag = [temp4[j] for i in range(len(index)) for j in range(len(temp2)) if index[i] == temp2[j]]
    flag = list(np.hstack(flag))
    buf = sorted(list(set(flag)))
    
    var = [flag.count(i) for i in buf]
    
    result = [buf[i] for i in range(len(var)) if var[i] == max(var)]
    return result

def req7(transactions, history):  
    for i in range(len(history)):
        for j in range(len(history[i])):
            for k in range(len(history[i][j])):
                history[i][j][k]=history[i][j][k].strip()
    
    temp1 = list(history[:,1])
    temp2 = list(np.hstack(transactions[:,0]))
    temp3 = list(transactions[:,1])
    
    index = [len(temp1[i]) for i in range(len(temp1))]
    
    for i in range(len(index)):
        if index[i] == min(index):
            tmp = temp1[i]
    
    result = [temp3[j] for i in range(len(tmp)) for j in range(len(temp2)) if tmp[i] == temp2[j]]
    
    result = sorted(list(np.hstack(result)))
    return result

def req8(transactions, history, k):
    return []

def req9(transactions, history, products):
    transactions = fixTransactions(transactions)
    products = fixProducts(products)
    
    index = sorted(list(set(transactions)))
    
    temp = products[:, 0]
    
    result = list(set(index) ^ set(temp))
    return result

def req10(history, transactions, products, k):
    products = fixProducts(products)
            
    temp = [j for i in history if i[0] == k for j in i[1]]
                   
    temp1 = [k for i in temp for j in transactions if i == j[0] for k in j[1]]
                
    index = [int(j[3]) for i in temp1 for j in products if i == j[0]]
    
    result = [0]*4
    for i in index:
        result[i] += 1
    
    return result.index(max(result))


print(req1(transactions))