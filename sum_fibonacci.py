# 9. Sum the first 50 Fibonacci sequence
def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def sum_first_50_fibonacci():
    fib_sequence = fibonacci(50)
    return sum(fib_sequence)

if __name__ == "__main__":
    sum_fibonacci = sum_first_50_fibonacci()
    print(f"Sum of the first 50 Fibonacci sequence: {sum_fibonacci}")