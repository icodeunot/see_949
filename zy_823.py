# 8.2.3
# Hourly temperature reporting.
# Write a loop to print all elements in hourly_temperature.
# Seperate elements with a -> surrounded by spaces
# Sample output for the given program:
# 90 -> 92 -> 94 -> 95
# Note: 95 is followed by a space, then a newline.

hourly_temperature = [90, 92, 94, 95] #existing code from learning source

# my code
#   |
#  \|/
#   v

arrow = '->'
ht_size = len(hourly_temperature) - 1

for temp in hourly_temperature[0:ht_size]:
    print(temp, '{}'.format(arrow), end=' ')
print(hourly_temperature[ht_size], ' ')


