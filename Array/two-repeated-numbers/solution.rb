def find_repeated_numbers(arr, n)
	dup_arr = []
	i = 0
	while(i < n) do
		index = arr[i].abs - 1
		if arr[index] > 0
			arr[index] = - arr[index]
		else
			dup_arr << (index + 1)
		end
		i += 1
	end
	dup_arr
end

arr = [2, 3, 1, 4, 4, 6, 5, 5]
find_repeated_numbers arr, 6