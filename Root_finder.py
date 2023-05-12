import re,math

def linear_quation(eq):
    if '=' not in eq:
        raise Exception ("Please enter a equation with '=' sign")
    var = find_variable(eq)
    digit = find_digit(var)
    var = var.split('=')
    x_value = remove_x_linear(var[0],var[1])
    if x_value != 0:
        if str(digit)[0]=='-' and str(x_value)[0]=='-':
            fraction = f'{str(digit)[1:]}/{str(x_value)[1:]}'
        elif str(x_value)[0]=='-':
            fraction = f'-{str(digit)}/{str(x_value)[1:]}'
        else:
            fraction = f'{digit}/{x_value}'
        print('The root is :',simplest_fraction(fraction))
    else:
        print("We can't find the root for this equation")


def quadratic_equation(eq):
    if '=' not in eq:
        raise Exception ("Please enter a equation with '=' sign")
    var = find_variable(eq)
    c = find_digit(var)
    var = var.split('=')
    rom = re.compile(r'''[-]?[\d]*[x][\^]?[2]?''',re.VERBOSE) 
    b = remove_x_linear(var[0],var[1])
    a = remove_x_quadratic(var[0],var[1])
    if a !=0 :
        D = check_roots(a,b,c)
        if 'i' not in D and '√' not in D and D!='0':
            root_1 = simplest_fraction(f'{-b-int(D)}/{2*a}')
            root_2 = simplest_fraction(f'{-b+int(D)}/{2*a}')
        elif 'i' not in D and D !='0':
            root_1 = simple_fraction_with_roots(b,D,a,'+')
            root_2 = simple_fraction_with_roots(b,D,a,'-')
        elif D=='0':
            root_1 = root_2 = simplest_fraction(f'{-b}/{2*a}')
        elif '√' in D and 'i' in D:
            root_1 = simple_fraction_with_roots(b,D,a,'+')
            root_2 = simple_fraction_with_roots(b,D,a,'-')
        elif '√' not in D and 'i' in D:
            root_1 = simple_fraction_with_roots_2(b,D,a,'+')
            root_2 = simple_fraction_with_roots_2(b,D,a,'-')
        print("The roots are-",root_1,root_2)
    else:
        print('The root is ',simplest_fraction(f'{-c}/{b}'))
    

def is_perfect_square(n):
    sq = math.sqrt(abs(n))
    if int(sq+0.5)**2==abs(n):
        return True
    else:
        ans=1
        for i in range(2,int(abs(n)/2)+2):
            ch = 0
            while ch==0:
                if n%(i**2)==0:
                    ans = ans*i
                    n = int(n/(i**2))
                else:
                    ch = 1
        if ans!=1:
            if n>0:
                return f'{ans}√{n}'
            else:
                return f'{ans}√{abs(n)}i'
        else:
            if n>0:
                return f'{ans}√{n}'
            else:
                return f'√{abs(n)}i'


def simple_fraction_with_roots(b,d,a,sign):
    a = a*2
    a1 = a
    prime = []
    if 'i' in d:
        d1 = str(d)[:len(str(d))-1]
        d1 = d1.split('√')
    else:
        d1 = d.split('√')
    if d1[0]!='':
        d1[0]=int(d1[0])
        for i in range(2,int(abs(a1/2)+2)):
            ch = 0
            while ch==0:
                if a1%i==0:
                    prime.append(i)
                    a1 = int(a1/i)
                else:
                    ch = 1
        for i in prime:
            if b!=0:
                if b%i==0 and d1[0]%i==0:
                    b = int(b/i)
                    d1[0] = int(d1[0]/i)
                    a = int(a/i)
            else:
                for i in prime:
                    if d1[0]%i==0:
                        d1[0] = int(d1[0]/i)
                        a = int(a/i) 
    if d1[0]==1:
        d1[0]=''
    
    if b!=0:
        if "i" in d:
            if a!=1:
                return f'({-b}{sign}{d1[0]}√{d1[1]}i)/{a}'
            else:
                return f'{-b}{sign}{d1[0]}√{d1[1]}i'
        else:
            if a!=1:
                return f'({-b}{sign}{d1[0]}√{d1[1]})/{a}'
            else:
                return f'{-b}{sign}{d1[0]}√{d1[1]}'                         
    else:  
        if "i" in d:
            if a!=1:
                return f'({sign}{d1[0]}√{d1[1]}i)/{a}'
            else:
                return f'{sign}{d1[0]}√{d1[1]}i'
        else:
            if a!=1:
                return f'({sign}{d1[0]}√{d1[1]})/{a}'
            else:
                return f'{sign}{d1[0]}√{d1[1]}'


def simple_fraction_with_roots_2(b,d,a,sign):
    a = a*2
    a1 = a
    prime = []
    d1 = int(d[len(d)-2])
    for i in range(2,int(abs(a1/2)+2)):
        ch = 0
        while ch==0:
            if a1%i==0:
                prime.append(i)
                a1 = int(a1/i)
            else:
                ch = 1
    for i in prime:
        if b!=0:
            if b%i==0 and d1%i==0:
                b = int(b/i)
                d1= int(d1/i)
                a = int(a/i)
        else:
            for i in prime:
                if d1%(i**2)==0:
                    d1 = int(d1/i)
                    a = int(a/i) 
    if d1==1:
        d1 = ''
    if b!=0:
        if a!=1:
            return f'({-b}{sign}{d1}i)/{a}'                        
        else:
            return f'{-b}{sign}{d1}i'                        
    else:  
        if a==1:
            return f'{sign}{d}i'
        else:
            return f'({sign}{d})/{a}'                    


def find_variable(n):
    d = set()
    for i in n:
        if str(i).isalpha():
            d.add(i)
    d = list(d)
    for i in range(len(n)):
        if i != len(n)-1:
            if n[i]+n[i+1]==d[0]+d[0]:
                raise Exception('Please enter the proper fomat of equation')
            elif n[i]=='x' and n[i+1] not in ['+','-','=','(',')','^',' ']:
                raise Exception('Please enter the proper format of  equation')   
    if len(d)>1:
        raise Exception("Please enter a equation in one variable")
    elif len(d)==1:
        return str(n).replace(d[0],'x')
    elif len(d)==0:
        return eval(n)

def remove_x_linear(n,m):
    rom = re.compile(r'''([-]?[\d]*)([x])(?![\^][2])''') 
    lhs = 0
    rhs = 0
    for i in rom.findall(n):
        if i[0]!=''and i[0]!='-':
            lhs += int(i[0])
        elif i[0]=='-':
            lhs +=-1
        else:
            lhs += 1
    for i in rom.findall(m):
        if i[0] !='' and i[0]!='-':
            rhs += int(i[0])
        elif i[0]=='-':
            rhs +=-1    
        else:
            rhs += 1
    return lhs-rhs


def remove_x_quadratic(n,m):
    rom = re.compile(r'''([-]?[\d]*)([x][\^][2])''') 
    lhs = 0
    rhs = 0
    for i in rom.findall(n):
        if i[0]!='' and i[0]!='-':
            lhs += int(i[0])
        elif i[0]=='-':
            lhs += -1
        else:
            lhs += 1
    for i in rom.findall(m):
        if i[0] !='' and i[0]!='-':
            rhs += int(i[0])
        elif i[0]=='-':
            rhs += -1
        else:
            rhs += 1
    return lhs-rhs


def find_digit(n): #Find and return the sum of constant present 
    n1 = n.split('=')
    rom = re.compile(r'\b([-^]?[\d]+)(?!x)\b')
    lhs = sum([int(i) for i in rom.findall(n1[0]) if i!='^2'])
    rhs = sum([int(i) for i in rom.findall(n1[1]) if i!='^2'])
    data = re.search(r'[\^][2]',n)
    if data is None:
        return rhs-lhs
    else:
        return lhs-rhs


def simplest_fraction(n):
    n = list(map(lambda x:int(x),n.split('/')))
    for i in range(2,int(abs(n[0])/2)+2):
        ch = 0
        while ch==0:
            if n[0]%i==0 and n[1]%i==0:
                n[0] = int(n[0]/i)
                n[1] = int(n[1]/i)
            else:
                ch = 1
    if n[0]<0 and n[1]<0:
        n[0] = abs(n[0])
        n[1] = abs(n[1])
    if n[0]==0:
        return 0 
    if n[1]==1:
        return n[0]
    else:
        return f'{n[0]}/{n[1]}'


def check_roots(a,b,c):
    D = (b**2) - (4*a*c)
    if D>0:
        if is_perfect_square(D) is True:
            return str(int(math.sqrt(D)))
        else:
            return f'{is_perfect_square(D)}'
    elif D==0:
        return '0'
    elif D<0:
        pov = abs(D)
        if is_perfect_square(pov) is True:
            D = str(int(math.sqrt(pov)))+'i'
            return D
        else:
            return f'{is_perfect_square(D)}'

if __name__=='__main__':
            n = input("Please enter you equation :")
            ans = ''
            cc = 0
            for i in n:
                if i=='^':
                    cc = 1
                    ans+=i
                elif i!=' ':
                    ans+=i
            if cc == 0:
                linear_quation(ans)
            else:
                quadratic_equation(ans)

