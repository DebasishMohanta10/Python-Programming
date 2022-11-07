def countFreq(arr, n):
    np = dict()

    for i in range(n):
        if arr[i] in np.keys():
            np[arr[i]] += 1
        else:
            np[arr[i]] = 1
    for x in np:
        print(x ," appears : ",np[x]," times.")

def main():
    arr = [2,4,2,6,8,2,6,5,4 ]
    n = len(arr)
    countFreq(arr, n)

if __name__ == "__main__":
    main()