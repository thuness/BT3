from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
  

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    def insertion_sort(arr):
      for i in range(1, len(arr)):
        current_element = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current_element:
          arr[j + 1] = arr[j]
          j -= 1
        arr[j + 1] = current_element
      return arr
    self.init_components(**properties)
    arr = list(map(int, input(self.txtN.split(",")))

    # Any code you write here will run before the form opens.
