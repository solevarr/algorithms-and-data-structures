import logging
logging.basicConfig(level=logging.INFO)


def reverse(some_string):
  if not isinstance(some_string, str):
    return 'hmm that is not good'
  string_list = []
  for char in some_string:
    string_list.append(char)  
  string_list = string_list[::-1]
  reversed_string = ''.join(string_list)
  logging.info(reversed_string)
  return reversed_string

def reverse_another(some_string):
  if not isinstance(some_string, str):
    return 'hmm that is not good'
  reversed_string=  ''.join(reversed(list(some_string)))
  logging.info(reversed_string)
  return reversed_string

def reverse_fast(some_string):
    if not isinstance(some_string, str):
      return 'hmm that is not good'
    return some_string[::-1]


if __name__ == '__main__':
  some_string = 'Hello world'
  reverse_fast(some_string)
  