import scipy.io
import numpy as np
data=scipy.io.loadmat('data.mat')
# print(data['transactions'])
# print(data['history'])
########## Requirements ######
def req1(transactions):
    a=[]
    for i in transactions:
        for k in range(len(i[1])):
            a.append((i[1][k]))         
    b=list(set(a))
    c=[]
    for j in b:
        c.append(a.count(j))
    lon=[]
    nho=[]    
    for e in range(len(c)):
        if(c[e]==max(c)):
            lon.append(b[e])
        if(c[e]==min(c)):
            nho.append(b[e])    
    return lon,nho
def dep(products):
    for i in range(products.shape[0]):
        for j in range(products.shape[1]):
            products[i][j]=products[i][j].strip()
    return products
# print(dep(data['products']))        
def req2(products):
    products=dep(products)
    a=list(products[:,2])
    for i in range(len(a)):
        a[i]=int(a[i])
    b=products[:,0]
    lon=[]
    nho=[]
    for i in range(len(a)):
        if(a[i]==max(a)):
            lon.append(b[i])
        if(a[i]==min(a)):
            nho.append(b[i])
    return lon,nho

def req3(transactions, products):
    a=[]
    for i in transactions:
        for k in range(len(i[1])):
            a.append((i[1][k])) 
    products=dep(products) 
    b=products[:,0]
    c=list(products[:,1])
    
    check = []
    
    for i in range(len(c)):
        c[i]=int(c[i])   
    sum=0
    for i in range(len(b)):
        sum=sum+a.count(b[i])*c[i]
        check.append(a.count(b[i]))
    return check

def req4(transactions, products):
    a=[]
    for i in transactions:
        for k in range(len(i[1])):
            a.append((i[1][k])) 
    products=dep(products) 
    b=products[:,0]
    c=list(products[:,1])
    for i in range(len(c)):
        c[i]=int(c[i])
    revenue=[]
    for i in range(len(b)):
        revenue.append(a.count(b[i])*c[i])
    r=[]    
    for i in range(len(revenue)):
        if(revenue[i]==max(revenue)):
            r.append(b[i])
    return r
def req5(history, k):
    a=[]
    for i in history:
        a.append(i[0])
        a.append(len(i[1]))
    a=np.hstack(a)
    b=a.reshape(int(len(a)/2),2)
    b = b[np.argsort(b[:, 1])][::-1]
    for i in range(len(b)):
        for j in range(i+1,len(b)):
            if(b[i][1]==b[j][1]):
                temp=b[i][0]
                b[i][0]=b[j][0]
                b[j][0]=temp
    c=[]
    for i in range(0,k):
        c.append(b[i][0])            
    return c
def req6(transactions, history, k):
    a=list(np.hstack(history[:,0]))
    b=list(history[:,1])
    c=list(np.hstack(transactions[:,0]))
    d=list(transactions[:,1])
    f=[]
    for i in range(len(a)):
        if(a[i]==k):
            e=b[i]
    for i in range(len(e)):
        for j in range(len(c)):
            if(e[i]==c[j]):
                f.append(d[j])
    f=list(np.hstack(f))
    x=list(set(f))
    g=[]
    for i in x:
        g.append(f.count(i))
    t=[]
    for i in range(len(g)):
        if(g[i]==max(g)):
            t.append(x[i])
    return t
def req7(transactions, history):
    
    return None

def req8(transactions, history, k):
    return None

def req9(transactions, history, products):
    return None

def req10(history, transactions, products, k):
    return None
# print(req1(data['transactions']))
# print(req2(data['products']))
# print(req3(data['transactions'], data['products']))
# print(req4(data['transactions'], data['products']))
# print(req5(data['history'], 3))
print(req6(data['transactions'],data['history'],'U2'))
# print(req7(data['transactions'],data['history']))