
import re,math

def linear_quation(eq):
    if '=' not in eq:
        raise Exception ("Please enter a equation with '=' sign")
    var = find_variable(eq)
    digit = find_digit(var)
    var = var.split('=')
    rom = re.compile(r'''[+-\^]?[\d]*[x]''',re.VERBOSE) 
    lhs = rom.findall(var[0])
    rhs = rom.findall(var[1])
    x_value = remove_x_linear(lhs,rhs)
    if str(digit)[0]=='-' and str(x_value)[0]=='-':
        fraction = f'{str(digit)[1:]}/{str(x_value)[1:]}'
    elif str(x_value)[0]=='-':
        fraction = f'-{str(digit)}/{str(x_value)[1:]}'
    else:
        fraction = f'{digit}/{x_value}'
    print('The root is :',simplest_fraction(fraction))


def quadratic_equation(eq):
    if '=' not in eq:
        raise Exception ("Please enter a equation with '=' sign")
    var = find_variable(eq)
    c = find_digit(var)
    var = var.split('=')
    rom = re.compile(r'''[+-\^]?[\d]*[x][\^]?[2]?''',re.VERBOSE) 
    tw0_var_lhs = [i for i in rom.findall(var[0]) if '^'  in i]
    tw0_var_rhs = [i for i in rom.findall(var[1]) if '^'  in i]
    one_var_lhs = [i for i in rom.findall(var[0]) if '^' not in i]
    one_var_rhs = [i for i in rom.findall(var[1]) if '^' not in i]
    b = remove_x_linear(one_var_lhs,one_var_rhs)
    a = remove_x_quadratic(tw0_var_lhs,tw0_var_rhs)
    D = check_roots(a,b,c)
    if str(D).isdigit() and D!=0:
        root_1 = simplest_fraction(f'{-b-D}/{2*a}')
        root_2 = simplest_fraction(f'{-b+D}/{2*a}')
    elif D==0:
        root_1 = root_2 = simplest_fraction(f'{-b}/{2*a}')
    else:
        root_1 = f'({-b}-{D})/{2*a}'
        root_2 = f'({-b}+{D})/{2*a}'
    print(f"The roots are: {root_1},{root_2}")

def is_perfect_square(n):
    sq = math.sqrt(n)
    if int(sq+0.5)**2==n:
        return True
    else:
        return False



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
            elif n[i]=='x' and n[i+1] not in ['+','-','=','(',')','^']:
                raise Exception('Please enter the proper format of  equation')
            
    if len(d)>1:
        raise Exception("Please enter a equation in one variable")
    elif len(d)==1:
        return str(n).replace(d[0],'x')
    elif len(d)==0:
        return eval(n)

def remove_x_linear(n,m):
    lhs = []
    for i in n:
        try:
            lhs.append(int(i[:len(i)-1]))
        except ValueError:
            lhs.append(1)
            continue
    rhs = []
    for i in m:
        try:
            rhs.append(int(i[:len(i)-1]))
        except ValueError:
            rhs.append(1)
            continue
    lhs_sum = sum(lhs)
    rhs_sum = sum(rhs)
    return lhs_sum-rhs_sum


def remove_x_quadratic(n,m):
    lhs = []
    for i in n:
        try:
            lhs.append(int(i[:len(i)-3]))
        except ValueError:
            lhs.append(1)
            continue
    rhs = []
    for i in m:
        try:
            rhs.append(int(i[:len(i)-3]))
        except ValueError:
            rhs.append(1)
            continue
    lhs_sum = sum(lhs)
    rhs_sum = sum(rhs)
    return lhs_sum-rhs_sum


def find_digit(n): #Find and return the sum of constant present 
    n = n.split('=')
    rom = re.compile(r'[+-\^]?[\d]+[x]?')
    cc = 0
    for i in rom.findall(n[0]):
        for j in i:
            if j=='^':
                cc = 1
    for i in rom.findall(n[1]):
        for j in i:
            if j=='^':
                cc = 1

    lhs = [int(i) for i in rom.findall(n[0]) if 'x' not in i and '^2' not in i]
    rhs = [int(i) for i in rom.findall(n[1]) if 'x' not in i and '^2' not in i]
    lhs_sum = sum(lhs)
    rhs_sum = sum(rhs)
    if cc==0:
        return rhs_sum-lhs_sum
    else:
        return lhs_sum-rhs_sum


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
    if n[1]==1:
        return n[0]
    else:
        return f'{n[0]}/{n[1]}'


def check_roots(a,b,c):
    D = (b**2) - (4*a*c)
    if D>0:
        if is_perfect_square(D):
            return int(math.sqrt(D))
        else:
            return f'√{D}'
    elif D==0:
        return 0
    elif D<0:
        pov = abs(D)
        if is_perfect_square(pov):
            D = str(int(math.sqrt(pov)))+'i'
            return D
        else:
            return f'√{pov}i'

if __name__=='__main__':
    n = input("Please enter your equation:")
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