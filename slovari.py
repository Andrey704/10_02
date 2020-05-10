slovar = {'book': 'книга', 'bear': "медведь"}

books = {'name': ['книга 1', 'книга2'], 'year': [1234, 1987]}

for i in range(len(books['name'])):
    print(books['name'][i])
    print(books['year'][i])

slovar['desk'] = 'стол'
print(slovar)

user = {
    'id': 1,
    'name': 'Pavel',
    'surname': 'Yakupov'
}

for key, user in user.items():
    print(key + str(user))