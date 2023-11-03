
import random
import time
import matplotlib.pyplot as plt
def power_naive(a, n):
    result = 1
    for _ in range(n):
        result *= a
    return result

def power_divide_conquer(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        half_power = power_divide_conquer(a, n // 2)
        return half_power * half_power
    else:
        half_power = power_divide_conquer(a, (n - 1) // 2)
        return half_power * half_power * a


def run_algorithm(algorithm, a, n):
    start_time = time.time()
    algorithm(a, n)
    end_time = time.time()
    return end_time - start_time

# Perform experiments for different values of n
n_values = list(range(1, 21))  # Adjust the range as needed
execution_times_naive = []
execution_times_divide_conquer = []

for n in n_values:
    a = 2  # You can change the base as needed
    execution_time_naive = run_algorithm(power_naive, a, n)
    execution_time_divide_conquer = run_algorithm(power_divide_conquer, a, n)
    execution_times_naive.append(execution_time_naive)
    execution_times_divide_conquer.append(execution_time_divide_conquer)

# Plot the results
plt.plot(n_values, execution_times_naive, label='Naive Iterative', marker='o')
plt.plot(n_values, execution_times_divide_conquer, label='Divide and Conquer', marker='o')
plt.xlabel('Power (n)')
plt.ylabel('Execution Time (seconds)')
plt.title('Scalability of Power Calculation Algorithms')
plt.legend()
plt.show()









'''
Naive Iterative Method:

 we multiply a by itself n times in a loop. The time complexity of this method is O(n) because we perform n multiplications.

In the divide-and-conquer approach, 

T(n) = T(n/2) + O(1)

This relation represents a binary divide-and-conquer, where we split the problem into two equal parts (n/2) and perform O(1) work to combine the results.

Using the Master Theorem to solve this recurrence:

a = 1 (number of subproblems)
b = 2 (subproblem size reduction factor)
f(n) = O(1) (work done outside the recursion)

We compare f(n) to n^(log_b(a)):

f(n) = O(1)
n^(log_b(a)) = n^(log_2(1)) = n^0 = 1

Since f(n) is constant and not larger than n^(log_b(a)), we are in Case 2 of the Master Theorem.

Case 2: 

T(n) = Θ(n^0 * log^0(n)) = Θ(log(n))
1d). yes experimental results meets theoratical results 
'''

def mergesorted(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = mergesorted(left_half)
    right_half = mergesorted(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def find_pairs_with_sum(arr, target):
    arr = mergesorted(arr)
    pairs = []

    for i in range(len(arr)):
        complement = target - arr[i]
        if binary_search(arr, complement, i + 1):
            pairs.append((arr[i], complement))

    return pairs

def binary_search(arr, target, start):
    left, right = start, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


    


'''


Merge Sort, which is used for sorting, has a time complexity of O(n log n), where 'n' is the number of elements. 
Binary Search, used to find pairs, has a time complexity of O(log n).

In this combined algorithm, we first sort the array using Merge Sort (O(n log n)) and then perform Binary Search for each element in the sorted array (O(log n) per element). This results in an overall time complexity of O(n log^2 n), where the time required for Binary Search is squared in relation to the size of the array.

 the proposed algorithm's time complexity is O(n log^2 n), indicating that it becomes less efficient as the size of the input data increases.
2d). yes experimental results meets theoratical results 
'''


def run_algorithm(n):
    input_data = [random.randint(1, 1000) for _ in range(n)]
    target = random.randint(1, 1000)
    start_time = time.time()
    find_pairs_with_sum(input_data, target)  # Call the algorithm without storing results
    end_time = time.time()
    return end_time - start_time


n_values = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
execution_times = []

for n in n_values:
    execution_time = run_algorithm(n)
    execution_times.append(execution_time)


plt.plot(n_values, execution_times, marker='o', linestyle='-')
plt.xlabel('Input Size (n)')
plt.ylabel('Execution Time (seconds)')
plt.title('Scalability of the Algorithm')
plt.show()

a = 2
n = 5

result_naive = power_naive(a, n)
result_divide_conquer = power_divide_conquer(a, n)

print(f"Using Naive Iterative Method: {a}^{n} = {result_naive}")
print(f"Using Divide-and-Conquer Approach: {a}^{n} = {result_divide_conquer}")
S = [1, 2, 3, 4, 5, 6]
target = 7
pairs = find_pairs_with_sum(S, target)
print("Pairs with sum", target, "are:", pairs)





