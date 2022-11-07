# Bag of Chocolates
# PrepBuddy has recently got a magical trunk. There are an infinite number of boxes in it, where 
# i-th box is connected with 
# i * (i-1)th box.
# K = no of chocolates at 0th box
# Find the no of cholates of Nth Box
def nthboxchocolate(n,k):
    if n == 0:
        return k
    else:
        return n * nthboxchocolate(n-1,k)

def main():
    t = int(input())
    while t > 0:
        n,k = map(int,input().split())
        print(nthboxchocolate(n,k))
        t -= 1
    
if __name__ == "__main__":
    main()
