def main():

    N = int(input('Enter the number N: '))
    
    #initialize an empty list to store the results
    result = []
    
    #for loop
    for i in range(N+1):
        result. append(2**i)
        
    
    print(result)
        

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
