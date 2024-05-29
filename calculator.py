def main():
    x=float(input("What's X? "))
    y=float(input("What's Y? "))
    print(toobig(x,y))

# z=round(x+y)
# z=x/y
def toobig(a,b):
    return round(a/b, 2)

main()


