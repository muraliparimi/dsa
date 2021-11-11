def euclidGCD(a,b):
    if b==0:
        return a
    else:
        a_prime=a%b
        return euclidGCD(b,a_prime)

if __name__ == "__main__":
    #print((input().split()))
    a,b  = input().split()
    #b = int(input().split()[1])
    
    print("a: "+ str(a) + " b: "+ str(b))
    print(euclidGCD(int(a),int(b)))