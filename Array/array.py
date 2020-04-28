import logging
logging.basicConfig(level=logging.DEBUG)


class MyArray():
  def __init__(self):
    self.length = 0
    self.data = {}
  
  def get_item(self, index):
    return self.data[index]
  
  def push_item(self, item):
    self.data[self.length] = item
    self.length +=1
    return self.length

  def pop_item(self):
    self.last_item = self.data[self.length - 1]
    del self.data[self.length - 1]
    self.length -= 1
    return self.last_item

  def delete_item(self, index):
    item = self.data[index]
    self.shift_items(index)
    return item
  
  def shift_items(self, index):
    for i in range(index, self.length -1):
      self.data[i] = self.data[i + 1]
    del self.data[self.length - 1]
    self.length -= 1

if __name__ == '__main__':
  my_array = MyArray()
  my_array.push_item('Hi')
  my_array.push_item('you')
  my_array.push_item('are')
  my_array.push_item('!')
  logging.info(my_array.data)
  my_array.delete_item(3)
  my_array.push_item('nice')
  logging.info(my_array.data)
