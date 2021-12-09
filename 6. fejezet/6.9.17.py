t = int(input())
n = int(input())

def tobbszoros_e(t,n):
    if(t % n == 0):
        return "Töbszöröse"
    else:
        return "Nem töbszöröse"


print(tobbszoros_e(t,n))