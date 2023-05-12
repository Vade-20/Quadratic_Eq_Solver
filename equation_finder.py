import re
from fractions import Fraction

x = input('Please enter the first root here:')
y = input("Please enter the second root:")

def isfloat(n):
    try:
        n = str(n)
        n = float(eval(n))
        return True
    except:
        return False

def hcf(a,b,c):
    if all([i<0 for i in [a,b,c]]):
        hcf = -1
    else:
        hcf = 1
    min_ = min([abs(a),abs(b),abs(c)])
    for i in range(2,int(min_/2)+2):
        if all([j%i==0 for j in [a,b,c]]):
            hcf = hcf*i
            a = a/i
            b = b/i
            c = c/i
    return hcf

def isroot(n):
    if '√' in n or 'i'  in n:
        return True
    else:
        return False  

def inversing_fraction(n):
    if '/-' in n:
        d = str(n).replace('/-','/')
        d = '-'+d
        return d
    elif '/ -' in n:
        d = str(n).replace('/ -','/')
        d='-'+d
        return d
    else:
        return n
    

if x.isdigit() and y.isdigit():
    x = -int(x)
    y = -int(y)
    a = 1
    b = x+y
    c = x*y
    
elif isfloat(x) and isfloat(y):
    x = -Fraction(inversing_fraction(x))
    y = -Fraction(inversing_fraction(y))
    b = x+y
    c = x*y
    a = b.denominator*c.denominator
    b_1 = b.numerator*c.denominator
    c = c.numerator*b.denominator
    b = b_1
    div = hcf(a,b,c)
    a = int(a/div)
    b = int(b/div)
    c = int(c/div)

elif isroot(x) and isroot(y):
    d = x.split('/')
    po = ''
    for i in d[0]:
        if i not in ['(',')']:
            po+=i
    d[0] = po
    if '+' in d[0]:
        pp = d[0].split('+')
        b =[pp[0]] if '√' not in pp[0] or 'i' not in pp[0] else pp[1]
        D = [pp[1]] if '√'  in pp[1] or 'i' in pp[1] else pp[0]
    elif '-' in d[0] and len(d[0].split('-'))>2:
        pp = d[0].split('-')
        b = [pp[0]] if '√' not in pp[0] or 'i' not in pp[0] else pp[1]
        D = [pp[1]] if '√'  in pp[1] or 'i' in pp[1] else pp[0] 
    elif '√' in d[0] or 'i' in d[0]:
        D = [d[0]]
        b = '0'
    else:
        D = '0'
        b = [d[0]] 
            
    a = re.findall(r'[\-]?[\d]+',d[1]) if len(d)==2 else '1'
    if any([len(i)>1 for i in [b,D,a]]):
        print(b,D,a)
        raise Exception ('Please enter proper roots')

    b = -Fraction(int(b[0])) if b!='0' else 0
    a = Fraction(int(a[0]),2) if a!='1' else Fraction(int(a),2)
    if D!='0':
        d = D[0].split('√')
        if d[0]!='' and d[0]!='i':
            if 'i' in d[1]:
                d[1] = str(d[0]).replace('i','')
                D = -(int(d[0])**2)*int(d[1])
            else:
                D = (int(d[0])**2)*int(d[1])
        elif d[0]=='i':
            D = -1
        else:
            if 'i' in d[1]:
                d[1] = str(d[1]).replace('i','')
                D = -int(d[1])
            else:
                D = int(d[1])
        D = Fraction(str(D))
    else:
        D = 0
    c = (b**2-D)/(4*a)
    a_ = a.numerator*b.denominator*c.denominator
    b_ = b.numerator*a.denominator*c.denominator
    c_ = c.numerator*a.denominator*b.denominator
    a = a_
    b = b_
    c = c_
    div = hcf(a,b,c)
    a = int(a/div)
    b = int(b/div)
    c = int(c/div)
else:
    raise Exception ("Please enter a proper roots")


if a==1:
    a = ''
elif a==-1:
    a = '-'

if b==1:
    b = '+'
elif b==-1:
    b = '-'
elif b==0:
    b = '+0'
elif b>0:
    b = f'+{b}'


if c==1:
    c = '+1'
elif c==-1:
    c = '-1'
elif c==0:
    c = '+0'
elif c>0:
    c = f'+{c}'

print(f"The equation is : {a}x^2{b}x{c}=0")




            
        


