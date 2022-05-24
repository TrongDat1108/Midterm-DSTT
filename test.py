def req7(transactions, history):
    history=dep2(history)
    a=list(np.hstack(history[:,0]))
    b=list(history[:,1])
    c=list(np.hstack(transactions[:,0]))
    d=list(transactions[:,1])
    e=[]
    for i in range(len(b)):
        e.append(len(b[i]))

    for i in range(len(e)):
        if(e[i]==min(e)):
            m=b[i]
    f=[]    
    for i in range(len(m)):
        for j in range(len(c)):
            if(m[i]==c[j]):
                f.append(d[j])
    f=list(np.hstack(f))            
    return f
def doibungque(a,b,c,d,k):
    for i in range(len(a)):
        if(a[i]==k):
            giaodich=b[i]
    r=[]        
    for i in range(len(giaodich)):
        for j in range(len(c)):
            if(giaodich[i]==c[j]):
                r.append(d[j])
    r=np.hstack(r)            
    return list(set(r))
def themsinhto(u,v):
    for i in range(len(u)):
        u[i]=int(u[i])      
    for i in range(len(v)):
        v[i]=int(v[i])
    u=np.array(u)
    v=np.array(v)    
    n=sum(u*v)/(np.linalg.norm(u,2)*np.linalg.norm(v,2))
    return n
def banhtrangnuong(f,s):
    a=list(np.hstack(s))
    for i in range(len(s)):
        if(f.count(s[i])>0):
            a[i]=1
        else:
            a[i]=0    
    return a    
def req8(transactions, history, k):
    transactions=dep2(transactions)
    history=dep2(history)
    a=list(np.hstack(history[:,0]))
    b=list(history[:,1])
    c=list(np.hstack(transactions[:,0]))
    d=[]
    for i in transactions:
        d.append(i[1])
    e=list(set(np.hstack(d)))
    e=sorted(e)
    for i in range(len(d)):
        d[i]=list(np.hstack(d[i]))
    x=[]
    for i in range(len(a)):
        x.append(doibungque(a,b,c,d,a[i]))
    s=sorted(list(set(list(np.hstack(x)))))     
    f=[]    
    for i in range(len(x)):
        f.append(banhtrangnuong(x[i],s))
    m=[]
    z=[] 
    for i in range(len(a)):
        if(k==a[i]):  
            id=i
    for i in range(len(f)):
        if(i!=id and len(f[id])==len(f[i])):
            m.append(themsinhto(f[id],f[i]))
            z.append(a[i])
    ketquacuoicung=[]        
    for i in range(len(m)):
        if(m[i]==max(m)):
            ketquacuoicung.append(z[i])
    return ketquacuoicung