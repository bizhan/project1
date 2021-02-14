times = input("say a number ")
times = int(times)

# f string: how {time} is replaces with actual number
for time in range(times):
  print(f" time {time +1}: number")

for num in range(1,21):
  if num == 4 or num == 13:
    state = "unlucky"
  elif num % 2 == 0:
    state = "even"
  else:
    state = "odd"
  print(f"{num} is {state}")