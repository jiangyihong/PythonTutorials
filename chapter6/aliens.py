# alien_0 = {'color': 'green', 'points': '5'}
# alien_1 = {'color': 'yellow', 'points': '10'}
# alien_2 = {'color': 'red', 'points': '15'}
# aliens = [alien_0, alien_1, alien_2]
# for alien in aliens:
#     for key in alien.keys():
#         print(key)
#     for value in alien.values():
#         print(value)
aliens = []
for alien in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# print('Total number of aliens: ' + str(len(aliens)))
# for alien in aliens:
#     print(alien)
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
for alien in aliens[0:5]:
    print(alien)
