def Fibonacci_Generator(no_of_terms):
    if no_of_terms==0 or no_of_terms==1:
        return no_of_terms
    else:
        return(Fibonacci_Generator(no_of_terms-1)+Fibonacci_Generator(no_of_terms-2))

no_of_terms=int(input("Enter numbers of terms you want to GENERATE:"))
if no_of_terms<=0:
    print("please enter a positive integer")
else:
    print("********Fibonacci sequence********\n")
    print("-----------------------------------\n")
    for i in range(no_of_terms+1):
        print(Fibonacci_Generator(i),end=" ")