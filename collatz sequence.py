#Python 3 program to return the number of steps in the Collatz sequence
def collatz_steps(n):
    steps=0
    #Follow steps until we reach 1
    while n!=1:
        print(n,end='')
        if n%2==0:
            n=n//2
        else:
            n=3*n+1
        steps +=1
        print(1) #Print the final 1
        return steps

#Example usage
x=int(input("Enter a number:"))
steps=collatz_steps(x)
print(f"Total steps to reach 1:{steps}")
