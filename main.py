import random
from string import ascii_lowercase, ascii_uppercase


class Solution:
  def __init__(self, text):
    self.text = text
    self.setASCII = list(ascii_lowercase + ascii_uppercase)
    random.shuffle(self.setASCII)
  
  def reverseText(self, text: str = None) -> str:
    text = self.text if text is None else text
    x = text.replace("a" , "1")
    return x[::-1]

  def alterText(self) -> str:
    indeces = []
    res = self.text
    while len(indeces) != 3:
      index = random.randrange(0, len(self.text) - 1)
      if index not in indeces:
        indeces.append(index)
        res = res[:index] + random.choice(self.setASCII) + res[index + 1:]
        
    return res
    

if __name__ == "__main__":
  text = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy'
  static_res = Solution(text).alterText()
  print(static_res)