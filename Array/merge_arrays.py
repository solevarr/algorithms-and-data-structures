import logging
logging.basicConfig(level=logging.INFO)


def merge_sorted_arrays(first_array, second_array):
  if not isinstance(first_array, 
  list) or not isinstance(second_array, list):
    return 'hmm that is not good'
    
  merged_array = list()
  right_length, left_length = len(first_array), len(second_array)
  left_idx = 0
  right_idx = 0
  while (left_idx < left_length and right_idx < right_length):
    if first_array[left_idx] < second_array[right_idx]:
      merged_array.append(first_array[left_idx])
      left_idx += 1
    else:
      merged_array.append(second_array[right_idx])
      right_idx += 1
  merged_array = merged_array + first_array[left_idx:] + second_array[right_idx:]
  return merged_array


if __name__ == '__main__':
  arr_one = [0,2,3]
  arr_two = [2,4,5]
  logging.info(merge_sorted_arrays(arr_one, arr_two))