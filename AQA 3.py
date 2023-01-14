nums = [int(i) for i in input ("Введите несколько чисел через пробел: ").split()]
def filter_nums(i):
  if(i%3)==0 and (i)!=0:
    return True
  else: return False
x = list(filter(filter_nums, nums))
if len(list(x))==0:
   print ("Отсутствуют числа кратные трем.")
else: print (list(x))
