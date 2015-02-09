## Challenge 180 from /r/dailyprogrammer: create a function that takes starts
## a look and say sequence with user-determined start and length.

def seq(a):
    a = str(a)
    k,last,result = 1,a[0],''
    for i in range(1,len(a)):
        if last==a[i]:k+=1
        else:
            result = result+str(k)+last
            k=1
        last = a[i]
    result = result+str(k)+last
    return result

def look_and_say(data=1, maxlen=5):
    res = []
    x = data
    for i in range(0,maxlen):
        if i==0:
            current = seq(data)
            res.append(current)
            x = current
        else:
            x = seq(x)
            res.append(x)
    return res