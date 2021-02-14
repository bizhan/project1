import  random
rand_num = random.randint(0,2)
if rand_num == 0:
  computer = "rock"
elif rand_num == 1:
  computer = "paper"
else:
  computer = 'sissors'

print(computer)