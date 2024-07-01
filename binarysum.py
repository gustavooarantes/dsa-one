def main():
    sequence = [1, 2, 3, 4, 5, 6]
    sum = binary_sum(sequence, 0, 6)
    print(sum)

def binary_sum(S, start, stop):
    if start >= stop:
        return 0
    elif start == stop - 1:
        return S[start]
    else:
        mid = (start + stop) // 2
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)
    
main()