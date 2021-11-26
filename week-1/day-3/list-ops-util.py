data = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
print(data)

copied_data = data.copy()
print(copied_data)
data.sort()
data.append('abc')
print(data)

copied_data.clear()
print(copied_data)

print(f'Popped Item : {data.pop()}')
print(data)
