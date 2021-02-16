# { something for something in ...}
{x**2 for x in range(10)}
#dictionary version
{x:x**2 for x in range(10)}

set_char = {char.upper() for char in 'hello'}
print(set_char)

def are_all_vowels_in_string(string):
  return len({char for char in string if char in 'aeiou'}) == 5

print(are_all_vowels_in_string('bizhan'))
print(are_all_vowels_in_string('aeiou'))
