def main():
    integers = [1, 2, 3, 4, 5, 6, 7, 8]
    result = linear_sum(integers, 8)
    print(result)

def linear_sum(S, n):
    if n == 0:
        return 0
    else:
        return linear_sum(S, n - 1) + S[n - 1]
    
main()