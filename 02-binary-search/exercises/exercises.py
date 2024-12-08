def find_position_of_the_target(array: list[int], target: int) -> int:
	left, right = 0, len(array) - 1
	while left <= right:
		mid = left + (right - left) // 2
		if array[mid] == target:
			return mid
		elif array[mid] < target:
			left = mid + 1
		else:
			right = mid - 1
	return -1

def find_the_minimum_element_in_a_rotated_sorted_array(array: list[int]) -> int:
	left, right = 0, len(array) - 1
	while left < right:
		mid = left + (right - left) // 2
		if array[mid] > array[right]:
			left = mid + 1
		else:
			right = mid
	return array[left]

def find_the_largest_number_less_than_or_equal_to_the_target(array: list[int], target: int) -> int:
	left, right = 0, len(array) - 1
	while left <= right:
		mid = left + (right - left) // 2
		if array[mid] <= target:
			left = mid + 1
		else:
			right = mid - 1
	return array[right] if right >= 0 else -1
