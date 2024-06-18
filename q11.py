def fibonacci_sequence(n):
    fibonacci = [0, 1]  
    for i in range(2, n):
        next_number = fibonacci[i - 1] + fibonacci[i - 2]
        fibonacci.append(next_number)
    return fibonacci[:n]

n = int(input("Enter the value of n for Fibonacci sequence: "))
fib_sequence = fibonacci_sequence(n)
print("Fibonacci sequence:", fib_sequence)
