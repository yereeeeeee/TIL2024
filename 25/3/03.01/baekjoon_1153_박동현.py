def get_prime_number(num):
    is_prime = [True] * (num+1)

    for i in range(2, num+1):
        if is_prime[i]:
            for j in range(i*2, num+1, i):
                is_prime[j] = False
            
    return [i for i in range(2,num+1) if is_prime[i]]

num = int(input())
prime_numbers = get_prime_number(num)

if num < 8:
    print(-1)
else:
    if num % 2:
        ans = [2,3]
        num -= 5
    else:
        ans = [2,2]
        num -= 4
    
    left, right = 0, len(prime_numbers)-1
    while left <= right:
        sums = prime_numbers[left] + prime_numbers[right]
        if sums > num:
            right -= 1
        elif sums < num:
            left += 1
        else:
            ans += [prime_numbers[left], prime_numbers[right]]
            break
    print(*ans)
