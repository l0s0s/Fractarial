num = 5
def facrorial(num):
  if num == 0:
    return 1

  return facrorial(num - 1) * num



print('Факториал числа {0} равен {1}'.format(num,facrorial(num)))