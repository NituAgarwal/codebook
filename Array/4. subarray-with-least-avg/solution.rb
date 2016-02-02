def find_min_subarray(arr, n, k)
  return nil if n < k
  current_sum = arr[0..k-1].sum # sum of first sub array of size k
  min_sum = current_sum
  min_index = 0
  i = k
  while i < n
    # Add current item arr[i] and remove first item of the sub array
    current_sum += (arr[i] - arr[i-k])
    if current_sum < min_sum
      min_sum = current_sum
      min_index = (i - k + 1)
    end
    i += 1
  end
  return min_index, (min_index + k-1)
end

arr = [12, 4, 30, 11, 10, 15, 4, 22]
find_min_subarray(arr, 8, 3)