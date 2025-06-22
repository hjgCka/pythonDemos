bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

print(bicycles[2])

bicycles[0] = 'giant'
print(bicycles)

bicycles.append('honda')
print(bicycles)

bicycles.insert(0, 'suzuki')
print(bicycles)

del bicycles[0]
print(bicycles)

poped = bicycles.pop()
print(bicycles, poped)

bicycles.remove('redline')
print(bicycles)