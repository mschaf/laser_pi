len = 10

for i in range (len*2-2):
  i = i % (len*2-2)
  if i >= len:
    i = i - (i % len) * 2 - 2

  print('X' * (i % (len*2)))