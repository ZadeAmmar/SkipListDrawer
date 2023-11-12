def getChar(array, index):
    try:
        return array[index]
    except:
        length = len(str(array[0]))
        return " " * length

def createDashedLine(array):
    dashedLine = "---"
    for x in range(len(array)):
        temp = len(str(array[x][0]))
        dashedLine += "-" * temp
        dashedLine += "-"

    return dashedLine

def printArr(array):
    line = createDashedLine(array)
    print("\n" + line)
    maxes = []
    for x in range(len(array)):
        maxes.append(len(array[x]))

    maxLen = max(maxes)
    for x in range(maxLen-1, -1, -1):
        print(f"L{x}: ", end="")
        for y in range(len(array)):
            print(getChar(array[y], x), end = " ")
        print("")
    print(line)
            

def main():
    nums = []
    temp = []
    count = 0

    while(1):
        x = input("\nEnter the node value (or enter quit to exit): ")
        if x.lower() == "quit":
            if count == 0:
                return
            break
        try:
            x = int(x)
        except:
            print("Error. Please enter a number: ")
            continue
        
        y = input("Enter the node height: ")
        try:
            y = int(y)
        except:
            print("Error. Please enter a number: ")
            continue
            
        for i in range(y+1):
            temp.append(x)
        nums.append(temp)
        temp = []
        count += 1

    sortedArr = sorted(nums, key=lambda x: x[0])
    
    printArr(sortedArr)
    
main()