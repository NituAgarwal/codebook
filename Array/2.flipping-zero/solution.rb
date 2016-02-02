def flipping_zeros(arr, skip_count)
  i = 0
  j = 0
  skipped_zero_count = 0
  index_i = 0
  index_j = 0
  best_count = 0
  n = arr.length
  while j < n do
    if skipped_zero_count <= skip_count
      skipped_zero_count += 1 if arr[j] == 0
      j += 1
    end
    if skipped_zero_count > skip_count
      skipped_zero_count -= 1 if arr[i] == 0
      i += 1
    end

    if j - i > best_count
      best_count = j - i
      index_i = i
      index_j = j
    end
  end
  solution = []
  while index_i < index_j
    solution << index_i if arr[index_i] == 0
    index_i += 1
  end
  solution
end

arr = [1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0]
p flipping_zeros(arr, 2)
