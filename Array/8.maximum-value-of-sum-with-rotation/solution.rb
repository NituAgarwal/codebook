def maximum_sum_with_rotation(arr)
  n = arr.length
  arr_sum = arr.inject(0){|sum,x| sum + x }
  current_rotation_sum = arr.each_with_index.inject(0){|sum,(x,i)| (sum + (x*i)) }
  max_sum = 0
  arr.each_index do |index|
    sum = current_rotation_sum - arr_sum + n * arr[index]
    current_rotation_sum = sum
    max_sum = sum if sum > max_sum
  end
  max_sum
end

arr = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
p maximum_sum_with_rotation arr
