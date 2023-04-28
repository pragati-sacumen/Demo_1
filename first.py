#first python file on github 

print("welcome")

def greet(a = "Employee Name"):
    return f"Hi {a}, Welcome to Team "
print(greet("Pragati"))

def reverse(a="name"):
    return a[::-1]
print(reverse(greet("esrever drow ")))

def counter(l):
    d = dict()
    c=1
    for i in l:
        if i not in d:
            d[i]=c
        else :
            d[i]+=1
    return d
#l = [1,2,3,4,5,6,1,3,3,2,4,5]
l= list(map(int, input().split()))
print(counter(l))

        
