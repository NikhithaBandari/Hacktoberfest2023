class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        n = len(arr)
        distinctORs = set()  # Use set for O(1) lookup

        currentORs = set()  # Store the distinct OR values ending at index i

        for i in range(n):
            newORs = set()  # Store the new distinct OR values at index i

            for val in currentORs:
                newORs.add(val | arr[i])

            newORs.add(arr[i])  # Add the current element itself

            currentORs = newORs  # Update the currentORs set

            for val in currentORs:
                distinctORs.add(val)

        return len(distinctORs)


# The approach used in the provided Python code is to efficiently count the number of distinct bitwise ORs of all non-empty subarrays in the input array arr. Here's a short explanation of the approach:

# 1. Initialize two sets, distinctORs to keep track of the distinct OR values and currentORs to store the distinct OR values ending at the current index.

# 2. Iterate through the elements of the input array arr from left to right.

# 3. For each element at index i, create a new set newORs to store the distinct OR values that can be formed by combining the element at arr[i] with the values in currentORs.

# 4. Iterate through the values in currentORs and compute the bitwise OR with arr[i], adding the results to newORs.

# 5. Add the current element arr[i] to the newORs set to account for the OR value formed with the element itself.

# 6. Update currentORs with the values in newORs to represent the distinct OR values ending at index i.

# 7. Finally, add the values in currentORs to the distinctORs set to maintain the running count of distinct OR values.

# 8. The result is the size of the distinctORs set, which represents the number of distinct bitwise ORs of all non-empty subarrays in the input array.

# This approach efficiently counts the distinct OR values without explicitly computing all subarrays, and it uses sets for quick deduplication and lookup, resulting in a time complexity of O(n * 32) in the worst case.
