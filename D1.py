def fileToArray(file):
    intArray = []
    for line in file:
        intArray.append(int(line))

    return intArray

def puzzle1(arr): 

    count = 0

    prev = 0
    for x in arr:
        if x > prev and prev != 0:
            count += 1
        prev = x


    print(count)

def puzzle2(arr):
    count = 0
    prevWindow = 0

    for index, line in enumerate(arr):
        if index < len(arr) - 2:
            window = line + arr[index + 1] + arr[index + 2]
            if window > prevWindow and prevWindow != 0:
                count += 1
            prevWindow = window
    
    print(count)


if __name__ == "__main__":
    file = open('./d1p1.txt', 'r')
    intArray = fileToArray(file)
    puzzle1(intArray)
    puzzle2(intArray)