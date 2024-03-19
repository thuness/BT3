from ._anvil_designer import Form1Template
from anvil import *
  
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
    
  def btnSX_click(self, **event_args):
    """This method is called when the button is clicked"""
    def insertion_sort(arr):
      for i in range(1, len(arr)):
        current_element = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current_element:
          arr[j + 1] = arr[j]
          j -= 1
        arr[j + 1] = current_element
      return arr
  
    sorted_arr = insertion_sort(arr)
    self.label_KQ = {sorted_arr}
    pass


