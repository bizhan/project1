#a way of describing patterns within search strings
#checking for valid email formation
#starts with 1 more letter, number, +,_,-,. then
#AA single @sign then
#1 or more letter, number, or - then
#A single dot then
#ends with 1 or more letter, number, -, or .

# (^[a-zA-Z0-9_._-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.\+$])

#\d digit 0-9
#\w letter, digit , or undescore
#\D not a digit
#\W not. word character
#\S not a whitespace character
#. any character except line break
