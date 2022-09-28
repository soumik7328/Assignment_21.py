#1. Write a recursive python function to print first N natural numbers.
def n_num(n):
    if n>0:
        n_num(n-1)
        print(n, end='')      
n_num(int(input("Enter a number:-")))    
#2. Write a recursive python function to print first N natural numbers in reverse order
def n_num_rev(n):
    if n>0:
        print(n, end='')      
        n_num(n-1)   
n_num_rev(int(input("\nEnter a number:-")))
#3. Write a recursive python function to print first N odd natural numbers  
def odd(n):
    if n>=1:
        odd(n-1)
        print((n*2)-1,end=' ')

odd(int(input("\nEnter how many odd number you want to print:-")))
#4. Write a recursive python function to print first N odd natural numbers in reverse order
def odd_rev(n):
    if n>=1:
        print((n*2)-1,end=' ')
        odd_rev(n-1)

odd_rev(int(input("\nEnter how many odd number you want to print in reverse:-")))
#5. Write a recursive python function to print first N even natural numbers.
def even(n):
    if n>=1:
        even(n-1)
        print(n*2,end=' ')

even(int(input("\nEnter how many even number you want to print:-"))) 
#6. Write a recursive python function to print first N even natural numbers in reverse order.
def rev_even(n):
    if n>0:
        print( "Even number is ",n*2)
        return rev_even(n-1)
rev_even(int(input("\nEnter how many even number you want to print in reverse:-")))             
#7. Write a recursive python function to print squares of first N natural numbers
def square(n):
    if n>0:
        
        square(n-1)
        print(n*n,end=' ')

square(int(input("\nEnter a number=")))
#8. Write a recursive python function to print cubes of first N natural numbers
def cube(n):
    if n>0:
        
        cube(n-1)
        print(n**3,end=' ')

cube(int(input("\nEnter a number=")))
#9. Write a recursive python function to print first N multiples of a given number.
def multi(m,n=10):
    if n>0:
        multi(m,n-1)
        print(n*m,end=' ')
mul_num=int(input("\nEnter a number="))
multi(mul_num)
#10. Write a recursive python function to print a number in reverse order.
def num_in_rev(a):
    if a>0:
        print((0*10)+a%10,end='')
        num_in_rev(a//10)

a=int(input("\nEnter a number="))
print("Reverse of",a,"is")
num_in_rev(a)        