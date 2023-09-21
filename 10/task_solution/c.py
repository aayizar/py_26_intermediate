data = [
	{
		'country': 'country1',
		'city':    'city11',
	},
	{
		'country': 'country2',
		'city':    'city21',
	},
	{
		'country': 'country3',
		'city':    'city31',
	},
	{
		'country': 'country1',
		'city':    'city12',
	},
	{
		'country': 'country1',
		'city':    'city13',
	},
	{
		'country': 'country2',
		'city':    'city22',
	},
	{
		'country': 'country3',
		'city':    'city31',
	},
]

coutries: dict[list] = {}
for element in data:
    if element['country'] in coutries.keys():
        if not element['city'] in coutries[element['country']]:
            coutries[element['country']].append(element['city'])
    else:
        coutries[element['country']] = [element['city']]
        
print(coutries)