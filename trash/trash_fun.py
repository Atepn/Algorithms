
def gcd(a, b):
    return a if b == 0 else gcd(b, a%b)

def factorial(n:int):
    assert n >= 0, "Error"
    if n == 0:
        return 1
    return factorial(n-1) * n

def pow(a:float, n:int):
    if n == 0:
        return 1
    elif n % 2 == 1:
        return pow(a, n-1) * a
    else:
        return pow(a*a, n//2)

def hanois_towers(a, b, n = 0,  tmp =[]):
    '''rearranges elements according to the rule hanoi's towers'''
    if n == 0:
        n = len(a)
    if n == 1:
        b.append(a[len(a)-1])
        a.pop()
        return
    hanois_towers(a, tmp, b, n-1)
    b.append(a[len(a)-1])
    a.pop()
    hanois_towers(tmp, b, a, n-1)
