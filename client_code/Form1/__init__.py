from ._anvil_designer import Form1Template
from anvil import *

class function():
  @staticmethod
  def quicksort_string(input_string):
    # Chuyển chuỗi đầu vào thành một mảng các số nguyên
    arr = list(map(int, input_string.split()))

    # Hàm quicksort
    def quicksort(arr):
        if len(arr) <= 1:
            return arr
        
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        
        return quicksort(left) + middle + quicksort(right)
    
    # Sử dụng hàm quicksort để sắp xếp mảng và chuyển kết quả thành chuỗi
    sorted_array = quicksort(arr)
    sorted_string = ' '.join(map(str, sorted_array))
    return sorted_string

  @staticmethod
  def merge_sort(input_string):
    # Chuyển chuỗi đầu vào thành một mảng các số nguyên
    arr = list(map(int, input_string.split()))

    # Hàm merge_sort
    def merge_sort_helper(arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Đệ quy sắp xếp các nửa của mảng
        left_sorted = merge_sort_helper(left_half)
        right_sorted = merge_sort_helper(right_half)

        # Gộp hai nửa đã sắp xếp
        return merge(left_sorted, right_sorted)

    def merge(left, right):
        result = []
        left_index, right_index = 0, 0

        # Merge hai mảng đã sắp xếp
        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1
        
        # Thêm các phần tử còn lại từ mỗi mảng
        while left_index < len(left):
            result.append(left[left_index])
            left_index += 1
        while right_index < len(right):
            result.append(right[right_index])
            right_index += 1
        
        return result
    
    # Gọi hàm merge_sort_helper để sắp xếp mảng và chuyển kết quả thành chuỗi
    sorted_array = merge_sort_helper(arr)
    sorted_string = ' '.join(map(str, sorted_array))
    return sorted_string

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

  def btnNHAP_click(self, **event_args):
    """This method is called when the button is clicked"""
    arr = list(map(int, input().split(",")))
    self.label_MANG.text = str(arr)
    self.btnSX_click(arr)
    pass

 def insertion_sort(arr):
      for i in range(1, len(arr)):
        current_element = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current_element:
          arr[j + 1] = arr[j]
          j -= 1
        arr[j + 1] = current_element
      return arr  

  def btnSX_click(self, **event_args):
    """This method is called when the button is clicked"""
    sorted_arr = insertion_sort(arr)
    self.label_KQ = {sorted_arr}
    pass


