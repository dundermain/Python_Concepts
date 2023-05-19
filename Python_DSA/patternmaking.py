import numpy as np

def pattern(n,m):
  assert m > 7, "Number of coloums should be greater than 7"
  rows, cols = n ,m
  pat = []

  #printing middle welcome message
  mid = ('-'*int((cols-7)/2)+'WELCOME'+'-'*int((cols-7)/2))
  
  #upper pattern
  for i in range(int(n/2)):
    barball = (".|."*(i*2+1))

    underscore_no = int(int(m) - int(len(barball))/2)
    up = ('-'*underscore_no+barball+'-'*underscore_no)

  #lower pattern
  for i in range(int(n/2),0):
    barball = (".|."*(i*2+1))

    underscore_no = int(int(m) - int(len(barball))/2)
    down = ('-'*underscore_no+barball+'-'*underscore_no)
    print(down)