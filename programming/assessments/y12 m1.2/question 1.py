def sum_of_even_numbers(n):
    total = 0
    for number in range(1, n+1):
        if number % 2 == 0:
            total += number
    return total
