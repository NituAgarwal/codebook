def majority_element(arr)
  majority_element = arr[0]
  majority_element_count = 0
  arr.each do |e|
    if e == majority_element
      majority_element_count += 1
    else
      majority_element_count -= 1
    end
    if majority_element_count == -1
      majority_element_count = 1
      majority_element = e
    end
  end
  majority_element_count = 0
  arr.each do |e|
    majority_element_count += 1 if e == majority_element
  end
  return majority_element if majority_element_count > arr.length/2
  return nil
end

arr = [3, 3, 4, 2, 4, 4, 2, 4, 4, 4]
p majority_element(arr)
