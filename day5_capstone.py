numbers = [4, 8, 15, 16, 23, 42]
formatted_numbers = " ".join(str(x) for x in numbers)
def sum_list(n):
    total = 0
    for x in n:
        total += x
    return total
p = sum_list(numbers)
def avg(a, b):
    return (a/b)
q = avg(p, len(numbers))
def max(t):
    max_val = 0
    for x in t:
        if x > max_val:
            max_val = x
    return max_val
j = max(numbers)
print(f"Numbers: {formatted_numbers}")
print(f"Sum: {p}")
print(f"Average: {q:.2f}")
print(f"Max: {j}")