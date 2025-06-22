alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# 修改字典中的值
alien_0['color'] = 'yellow'
print(alien_0)

# 删除键值对
del alien_0['points']
print(alien_0)

favorite_languages = {
    'jack': 'python',
    'john': 'c',
    'smith': 'ruby',
    'paul': 'c++',
    'james': 'java'
}
print(favorite_languages['jack'])

# 使用get提供默认值
point_value = alien_0.get('points', 'no point value')
print(point_value)