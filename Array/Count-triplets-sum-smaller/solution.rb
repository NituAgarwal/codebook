def count_triplets(arr, sum)
	arr.sort!
	n = arr.length
	k = 0
	triplets_count = 0
	while k < n do
		i = k + 1
		j = n-1
		while (i < j) do
			if (arr[i] + arr[j] + arr[k] < sum)
				triplets_count += j - i
				i += 1
			else
				j -= 1
			end
		end
		k += 1
	end
	return triplets_count
end

arr = [5, 1, 3, 4, 7]
p count_triplets(arr, 12)
arr  = [-2, 0, 1, 3]
p count_triplets(arr, 2)