# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product


def fast_max_pairwise_product(numbers):
    n = len(numbers)
    index1=0
    
    for j in range(1,n):
        if numbers[j]>numbers[index1]:
            index1=j

    if index1==0:
        index2=1
    else:
        index2=0
    
    for j in range(1,n):
        if j !=index1 and numbers[j] > numbers[index2]:
            index2=j

    #print("Second index: "+ str(index2) + " and its corresponding value: "+ str(numbers[index2]))
    return numbers[index1]*numbers[index2] 




if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(fast_max_pairwise_product(input_numbers))
