def reorder(arr, index = [])
  i = 0;
  n = arr.length
  while i < n do
    arr[index[i]], arr[i] = arr[i], arr[index[i]]
    index[index[i]], index[i] = index[i], index[index[i]]
    i += 1
  end
  arr
end

arr = [10, 11, 12]
index = [1, 0, 2]
p reorder(arr, index)
