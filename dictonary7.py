# maximum and minimum value in a dictionary.

md = {'x':500, 'y':5874, 'z': 560}

key_max = max(md.keys(), key=(lambda k: md[k]))
key_min = min(md.keys(), key=(lambda k: md[k]))

print('Maximum Value: ',md[key_max])
print('Minimum Value: ',md[key_min])
